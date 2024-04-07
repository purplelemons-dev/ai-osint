from openai import OpenAI
from .osint.types import DataSource, Query
import json

# i assume you have api key set in your env vars. look at openai docs for more info
try:
    client = OpenAI()
except:
    from .osint.env import OPENAI_API_KEY, OPENAI_ORG_ID

    client = OpenAI(api_key=OPENAI_API_KEY, organization=OPENAI_ORG_ID)


def generate(
    model: str,
    query: Query,
    *data_source: DataSource,
    debug: bool = False,
    stream: bool = False,
):
    if debug:
        print("Generating AI OSINT report...")
    return client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": """You are an OSINT research assisant.
                    You will write a report on a person using the provided data. You are trying to identify one person out of many.
                    Aim for one to two paragraphs briefing the user on your findings.
                    Your job is to find the needle in the haystack and provide a report on the person.
                    Your report will be written using PURELY JSON ONLY. You will not wrap your response in ```.
                    Use the following format and only respond with JSON:
                    {
                        report: string;
                        names: string[];
                        emails: string[];
                        phones: string[];
                        addresses: string[];
                        usernames: string[];
                        passwords: string[];
                        ips: string[];
                        hashes: string[];
                    }""",
            },
            {"role": "user", "name": "query", "content": query.dump()},
            *[
                {
                    "role": "user",
                    "name": source.origin,
                    "content": json.dumps(source.data),  # , indent=2),
                }
                for source in data_source
            ],
        ],
        stream=stream,
    )
