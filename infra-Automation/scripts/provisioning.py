import json
import sys
sys.path.append('infra-Automation/src')
from logger import logger
from jsonschema import validate

# json validate schema

schema = {
    "type": "array",
    "properties": {
        "name": {"type": "string"},
        "os": {"type": "string"},
        "cpu": {"type": "string"},
        "ram": {"type": "string"}
    },
    "required": ["name", "os", "cpu", "ram"]
}




# scripts to input machines

logger("the machineConfig script is running")

def inputer():
    machine_list = []
    while True:
        machines = ["docker", "kubernetes"]
        name = str(input("please enter machine name (\"done\" for exit): "))
        if name.lower() == "done":
            logger("machine list is updated")
            return machine_list
        elif name.lower() not in machines:
            logger(f'ERROR: machine {name} does not exist', "error")
            continue
        else:
            os_list = ["ubuntu", "centos", "linux", "windows"]
            os = str(input("please enter the os: "))
            if os.lower() not in os_list:
                logger("ERROR: os does not exist, please try again", "error")
                continue
            else:
                cpu = str(input("please enter the CPU: "))
                ram = str(input("please enter the RAM:"))
                adding = {"name": name,
                        "os": os,
                        "cpu": cpu,
                        "ram": ram}
                machine_list.append(adding)
                logger("new machine just added to the list")

#script to write it on file

def writter(res):
    logger("adding changes to the file")
    try:
        with open("infra-Automation/configs/instances.json", "w") as file:
            file.write(json.dumps(res))
            logger("configuration succesfully saved")

    except Exception as e:
        logger(f'ERROR: {e}', "error")


#script to validate and call for writting function
def push(res):
    try:
        validate(instance=res, schema=schema)
        writter(res)

    except Exception as e:
        logger(f'ERROR: {e}', "error")



# check for working script

if __name__ == "__main__":

    res = inputer()
    try:
        validate(instance=i, schema=schema)
        writter(res)

    except Exception as e:
        logger(f'ERROR: {e}', "error")







        
