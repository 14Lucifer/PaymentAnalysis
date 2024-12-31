# Flink with Kafka Connector and PyFlink Setup

## Overview
This repository provides a setup for Apache Flink 1.20.0 with a Kafka connector for the Table API and PyFlink. The setup includes custom Docker configurations and a Docker Compose file to create and manage a Flink session cluster.

## Features
1. **Custom Docker File**: Builds a Flink image with the Kafka connector for the Table API and PyFlink.
2. **Docker Compose**: Sets up a session cluster with three containers:
   - Job Manager
   - Task Manager
   - SQL Client

## Prerequisites
Ensure that you have the following installed:
- Docker
- Docker Compose

## Versions Used
- **Flink**: 1.20.0
- **Python**: 3.10.12
- **Apache Flink Libraries**: 1.20.0
- **Kafka Connector JAR**: `flink-sql-connector-kafka-3.3.0-1.20.jar`

## Commands to Verify Versions
```bash
$ flink --version
Version: 1.20.0, Commit ID: b1fe7b4

$ python --version
Python 3.10.12

$ pip list | grep apache-flink
apache-flink           1.20.0
apache-flink-libraries 1.20.0
```

## Usage
1. Build and start the cluster:
   ```bash
   docker compose up --build jobmanager taskmanager -d
   ```
2. Access the SQL Client:
   ```bash
   docker compose run sql-client
   ```

## Notes
- Ensure compatibility between Flink, Kafka connector, Python, and PyFlink packages.
- Adjust resource allocations (e.g., memory and CPU) in `docker-compose.yml` as needed for your environment.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

