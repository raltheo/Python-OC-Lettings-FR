# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_DEBUG=False
ENV DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,p13.raltheo.fr
# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    git

# Create and set the working directory
WORKDIR /app

COPY . /app

RUN mv /app/nginx.conf /etc/nginx/sites-enabled/default

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Collect static files
RUN python /app/manage.py collectstatic --noinput

# Expose the port that Nginx will listen on
EXPOSE 80

# Start Nginx and Gunicorn
CMD service nginx start && gunicorn oc_lettings_site.wsgi:application -b 0.0.0.0:8000