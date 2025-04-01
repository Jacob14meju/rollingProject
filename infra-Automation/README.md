# rollingProject
Python Infrastructure Automation Script
Description:
This Python script is designed to automate the provisioning and configuration of virtual machines (VMs) with a set of predefined parameters. It performs the following key functions:

Input Machine Configurations: Prompts the user to input details about different machines.

Validate JSON Schema: Validates the machine configurations using a predefined JSON schema.

Save Configurations: Writes the valid machine configurations to a JSON file.

Install Services: Allows the user to install services on the provisioned machines.

Logging: Logs various actions to a log file for tracking purposes.

Requirements
Python 3.x

Required Python libraries:

json

logging

jsonschema

File Structure
infra-Automation/configs/instances.json: JSON file that stores machine configuration data.

infra-Automation/logs/provisioning.log: Log file to track the progress and errors of the script.

Usage
1. Setup Virtual Environment
It is recommended to set up a virtual environment to run the script:

bash:
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows
2. Install Required Packages
Install the required packages by running:

bash:
pip install jsonschema
3. Running the Script
To run the script, simply execute the Python file:

bash:
python infra_simulator.py
The script will:

Prompt you to enter the name, operating system, CPU, and RAM for the machine configurations.

Validate the configurations against a predefined schema.

Save the configurations in the instances.json file.

Install services on the provisioned machines.

4. Configuration File (instances.json)
The instances.json file contains the machine configurations in the following format:

json:
[
  {
    "name": "docker",
    "os": "ubuntu",
    "cpu": "2 CPUs",
    "ram": "4GB"
  },
  {
    "name": "kubernetes",
    "os": "centos",
    "cpu": "4 CPUs",
    "ram": "8GB"
  }
]
5. Logging
All actions performed by the script, including errors, will be logged in infra-Automation/logs/provisioning.log. The log will include details such as machine provisioning and service installation.

Code Flow
Inputer Function: Prompts the user for machine configuration inputs (e.g., name, OS, CPU, RAM) and validates the inputs. If the user enters "done," the process ends, and the list of machines is returned.

Writter Function: Writes the list of machine configurations to the instances.json file in JSON format.

Push Function: Validates the machine configurations using the predefined JSON schema and then calls the writter function to save the valid data.

Setup Runner Function: Simulates the installation of services on the provisioned machines.

Machine Class: A class that represents a machine and provides methods for logging and getting machine details as a dictionary.

Logging: All actions and errors are logged into the provisioning.log file using the logging module.

Machine Instantiation: After reading the instances.json file, the script instantiates Machine objects for each configuration and performs logging for each machine provisioned.

Service Installation: The script installs services on each provisioned machine by calling the setup_runner function.

Example
When running the script, you will be prompted to enter machine details:


please enter machine name ("done" for exit): docker
please enter the os: ubuntu
please enter the CPU: 2 CPUs
please enter the RAM: 4GB
please enter machine name ("done" for exit): kubernetes
please enter the os: centos
please enter the CPU: 4 CPUs
please enter the RAM: 8GB
please enter machine name ("done" for exit): done
The machine configurations will then be validated, saved, and logged.

Error Handling
The script will display error messages and log errors to the provisioning.log file if:

Invalid machine names or OS types are provided.

JSON schema validation fails.

There is an issue with writing the configuration to the JSON file.

Any issue occurs during service installation.

License
This script is provided under the MIT License.