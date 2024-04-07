# AI-OSINT

basically information density theory

throw enough data at an AI and it'll eventually figure out what you're looking for

## Download/run

### Python
```bash
git clone https://github.com/purplelemons-dev/ai-osint.git
cd ai-osint/src
python -m ai_osint --email "someone@example.com"
```

### Docker
```bash
git clone https://github.com/purplelemons-dev/ai-osint.git
docker compose run --rm ai-osint --email "someone@example.com"
```

### API
```bash
git clone https://github.com/purplelemons-dev/ai-osint.git
cd ai-osint
docker compose up -d
curl -X POST -H "Content-Type: application/json" -d '{"email": "someone@example.com"}' http://localhost:10021/
```
