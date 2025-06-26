# Dockerfile
FROM python:3.13-slim

# Create app directory
WORKDIR /home

# Copy files
COPY . /home

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Streamlit on port 8080
EXPOSE 8080

# Streamlit environment variables
ENV STREAMLIT_SERVER_PORT=8080 \
    STREAMLIT_SERVER_HEADLESS=true \
    PYTHONUNBUFFERED=1

# Run Streamlit app
CMD ["streamlit", "run", "app.py"]