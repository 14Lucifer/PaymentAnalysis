# Data Analytical Lab Setup

This repository provides scripts and resources to build a complete Data Analytical Lab, including:
- **Step 1:** Linux Environment Setup (Docker, Portainer, Apache Superset).
- Future components: ClickHouse, Flink, and a demo application.

### Step 1. Linux Environment Setup Script

A simple script to:
- Installs Docker and dependencies.
- Deploys Portainer and Superset as Docker containers.
- Ensures Superset container is ready, installs required Python packages, and restarts containers for changes to take effect.

### Requirements
- Ubuntu 22.04 LTS
- Sudo privileges

### How to Use
1. Clone the repository.
   ``` bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the script with sudo.
   ``` bash
   sudo ./setup-script.sh
   ```

3. Follow the on-screen instructions.
