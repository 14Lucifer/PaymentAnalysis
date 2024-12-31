FROM flink:latest

# Copy connector jar files
COPY flink-sql-connector-kafka-3.3.0-1.20.jar /opt/flink/lib/

# install python3 and pip3
RUN apt-get update -y && apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN pip3 install apache-flink
