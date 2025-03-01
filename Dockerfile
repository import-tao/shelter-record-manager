FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/requirements_production.txt requirements/requirements_production.txt
COPY requirements/requirements_local.txt requirements/requirements_local.txt
RUN pip install --no-cache-dir -r requirements/requirements_production.txt
RUN pip install --no-cache-dir -r requirements/requirements_local.txt

# Copy project
COPY . .

# Run entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"] 