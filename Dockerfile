FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install -r req.txt

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0", "--port=5000"]