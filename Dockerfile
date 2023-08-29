FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y ffmpeg && \
    pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["src/main.py"]
