# Use the official Python image
FROM python:3.12.11-slim-bullseye

# Set environment variables using recommended format
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8000

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Run the application using JSON-form CMD for signal safety
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]

# Expose port
EXPOSE 8000
