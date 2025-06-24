FROM python:3.9

COPY ./requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

COPY ./ ./

ENTRYPOINT [ "python" ]
CMD [ "bot.py" ]