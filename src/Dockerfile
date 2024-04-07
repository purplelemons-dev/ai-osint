FROM python:3.12.2-slim-bookworm

WORKDIR /app

RUN apt update && apt upgrade -y && apt install -y

RUN apt install -y chromium

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Get the browser "warmed up" (e.g. download the webdriver)
RUN python -m ai_osint.osint.tps

# evil wtf run #2
#RUN python -m ai_osint.osint.tps

# Run the application
# Container should be run as a command. entrypoint is python -m ai_osint [options]
ENTRYPOINT ["python", "-m", "ai_osint"]

# Default command is to run the application
CMD ["--api"]
