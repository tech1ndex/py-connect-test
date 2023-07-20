FROM python:3.10-alpine
WORKDIR /app
COPY src .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "-u", "py-connect-test.py"]