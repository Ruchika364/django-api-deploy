# syntax=docker/dockerfile:1.4

FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-dev \
    bash \
    pkgconfig

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose port
EXPOSE 8000

# Run using gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi:application"]
