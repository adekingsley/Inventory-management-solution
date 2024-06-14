FROM python:3.10-slim

# Prevents pyc files from being copied to the container
ENV PYTHONDONTWRITEBYTECODE 1

# Ensures that python output is logged in the container's terminal
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    # Dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # Cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file from the local build context to the container's file system.
COPY ./requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install -r /requirements.txt --no-cache-dir

# Set the working directory
WORKDIR /app

# Copy the entire project directory to the container's file system
COPY . /app

# Set correct permissions for the database file directory
RUN mkdir -p /app/db && chown -R www-data:www-data /app/db

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
