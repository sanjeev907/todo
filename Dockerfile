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



FROM python:3.10.6-slim-buster

# Set working directory
WORKDIR /todo-app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Collect static files and run the server
CMD sh -c "python manage.py collectstatic --noinput  && python manage.py runserver 0.0.0.0:8000"
