FROM python:3.11

WORKDIR /usr/src/Template

# CASH FAYLLARNI SAQLAMASLIK UCHUN
ENV PYTHONNONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

