# Use a lightweight base image
FROM python:3.11-slim-bookworm

# Prevent Python from writing .pyc files and buffer logs for better visibility
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy source code
COPY . .

# Create writable logs directory
RUN mkdir -p /app/logs && chmod -R 777 /app/logs

# Update system packages and clean up
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 7860

# Launch the app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the default Streamlit port
EXPOSE 7860

# Launch the app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
