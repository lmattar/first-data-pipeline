FROM python:3.8.8-slim

WORKDIR /usr/src/app

COPY requirements.txt  requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# expose the port that uvicorn will run the app
EXPOSE 8001


WORKDIR /usr/src 


CMD ["uvicorn", "app.main:app","--roload","--workers","1" , "--host", "0.0.0.0", "--port", "8001"]

