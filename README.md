# Data Analytical Lab Setup

This repository provides scripts and resources to build a complete Data Analytical Lab, including:
- **Step 1:** Linux Environment Setup (Docker, Portainer, Apache Superset).
- Future components: ClickHouse, Flink, and a demo application.
<br></br>

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
   git clone https://github.com/14Lucifer/PaymentAnalysis.git
   cd PaymentAnalysis/Prepare_Env/
   ```

2. Run the script with sudo.
   ``` bash
   sudo ./ubuntu22_prepare.sh
   ```

3. Follow the on-screen instructions.
   ``` bash
   This script will perform the following actions:
   1. Install Docker and remove conflicting packages.
   2. Set up Portainer for Docker management.
   3. Install Apache Superset for data visualization.
   4. Restart containers to apply changes where necessary.
    
   Do you want to proceed? (yes/no):
   
   ```
