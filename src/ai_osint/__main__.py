from . import ai_osint
import argparse
import json


def main():
    parser = argparse.ArgumentParser(description="AI OSINT")
    parser.add_argument("--name", type=str, help="Name of the person")
    parser.add_argument("--phone", type=str, help="Phone number")
    parser.add_argument("--email", type=str, help="Email address")
    parser.add_argument("--username", type=str, help="Username")
    parser.add_argument("--address", type=str, help="Address")
    parser.add_argument("--ip", type=str, help="IP address")
    parser.add_argument("--domain", type=str, help="Domain")
    parser.add_argument("--password", type=str, help="Password")
    parser.add_argument("--hash", type=str, help="Hashed password")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Run the program in debug mode and print progress",
    )
    parser.add_argument(
        "--stream",
        action="store_true",
        help="Stream the output instead of returning it all at once",
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Print the report only, without the data",
    )
    parser.add_argument(
        "--api", action="store_true", help="Serve the app as a RESTful API"
    )

    args = parser.parse_args()
    if args.api:
        from .serve_api import run

        run()
    elif args.report_only:
        ai_response = (
            ai_osint(
                name=args.name,
                phone=args.phone,
                email=args.email,
                username=args.username,
                address=args.address,
                ip=args.ip,
                domain=args.domain,
                password=args.password,
                hashed_password=args.hash,
                debug=args.debug,
            )
            .choices[0]
            .message.content
        )
        try:
            parsed = json.loads(ai_response)
            print(parsed["report"])
        except:
            print("There was an error parsing the report. Here is the raw data:")
            print(ai_response)

        return
    elif args.stream:
        for choice in ai_osint(
            name=args.name,
            phone=args.phone,
            email=args.email,
            username=args.username,
            address=args.address,
            ip=args.ip,
            domain=args.domain,
            password=args.password,
            hashed_password=args.hash,
            debug=args.debug,
            stream=args.stream,
        ):
            print(choice.choices[0].delta.content, end="")
        return
    print(
        ai_osint(
            name=args.name,
            phone=args.phone,
            email=args.email,
            username=args.username,
            address=args.address,
            ip=args.ip,
            domain=args.domain,
            password=args.password,
            hashed_password=args.hash,
            debug=args.debug,
            stream=args.stream,
        )
        .choices[0]
        .message.content
    )


if __name__ == "__main__":
    main()
