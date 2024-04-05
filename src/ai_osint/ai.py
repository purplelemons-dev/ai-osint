from openai import OpenAI
from .osint.types import DataSource, Query
import json

# i assume you have api key set in your env vars. look at openai docs for more info
client = OpenAI()


def generate(model: str, query: Query, *data_source: DataSource, debug: bool = False):
    if debug:
        print("Generating AI OSINT report...")
    return client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": """You are an OSINT research assisant.
                    You will generate a report on a person using data.
                    Your report will be written using JSON ONLY. Use the following format and only respond with JSON:
                    {
                        names: string[];
                        emails: string[];
                        phones: string[];
                        addresses: string[];
                        usernames: string[];
                        passwords: string[];
                        domains: string[];
                        ips: string[];
                        hashes: string[];
                    }""",
            },
            {"role": "user", "content": query.dump()},
            *[
                {
                    "role": "user",
                    "name": source.origin,
                    "content": json.dumps(source.data),#, indent=2),
                }
                for source in data_source
            ],
        ],
    )
