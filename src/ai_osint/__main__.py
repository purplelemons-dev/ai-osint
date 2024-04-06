from . import ai_osint
import argparse


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

    args = parser.parse_args()
    if args.stream:
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
