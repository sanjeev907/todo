# FROM python:3.10.6-slim-buster

# WORKDIR /todo

# COPY requirements.txt requirements.txt

# RUN pip install -r requirements.txt

# COPY . .

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]



# Dockerfile

# FROM python:3.10-slim

# # ENV PYTHONDONTWRITEBYTECODE 1
# # ENV PYTHONUNBUFFERED 1

# WORKDIR /todo-lastest

# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install -r requirements.txt

# COPY . .

# RUN mkdir -p /vol/web/media /vol/web/static

# COPY ./entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# CMD ["/entrypoint.sh"]


############################# development ready using docker  ##
#FROM python:3.10.6-slim-buster

# Set working directory
#WORKDIR /todo-app

# Copy project files
#COPY . .

# Install dependencies
#RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Collect static files and run the server
#CMD sh -c "python manage.py collectstatic --noinput  && python manage.py runserver 0.0.0.0:8000"



####### coolify ###########
FROM python:3.10-slim-bookworm

# Set working directory
WORKDIR /app

# Prevent Python from writing pyc files and enabling buffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Coolify will bind to
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "todo.wsgi:application", "--bind", "0.0.0.0:8000"]
