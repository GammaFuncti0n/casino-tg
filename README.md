Project with tg casino bot

Right now only available slot machine

For build docker image:
```bash
docker build -t casino:v1 .
```
For launch container:
```bash
docker run --rm -v $(pwd)/data:/app/data casino:v1
```