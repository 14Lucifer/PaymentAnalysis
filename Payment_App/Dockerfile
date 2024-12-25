# Use Python 3.10.12 slim image
FROM python:3.10.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and configuration file
COPY transaction_producer.py /app/
COPY config.yml /app/

# Install Python packages directly using pip
RUN pip install --no-cache-dir kafka-python pycountry pyyaml

# Command to execute the Python script
CMD ["python", "transaction_producer.py"]
