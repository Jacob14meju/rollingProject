import json
import sys
sys.path.append('infra-Automation/src')
from logger import logger
from jsonschema import validate

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




# scripts to configure machines
logger("the machineConfig script is running")

def inputer():
    machine_list = []
    while True:
        machines = ["docker", "kubernetes", "linux", "windows"]
        name = str(input("please enter machine name (\"done\" for exit): "))
        if name.lower() == "done":
            logger("machine list is updated")
            return machine_list
        elif name.lower() not in machines:
            logger(f'ERROR: machine {name} does not exist', "error")
            continue
        else:
            os_list = ["ubuntu", "centos"]
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

def writter(res):
    logger("adding changes to the file")
    try:
        with open("infra-Automation/configs/instances.json", "w") as file:
            file.write(json.dumps(res))
            logger("configuration succesfully saved")

    except Exception as e:
        logger(f'ERROR: {e}', "error")


def push(res):
    try:
        validate(instance=res, schema=schema)
        writter(res)

    except Exception as e:
        logger(f'ERROR: {e}', "error")



# write it on the file
if __name__ == "__main__":

    res = inputer()
    try:
        validate(instance=i, schema=schema)
        writter(res)

    except Exception as e:
        logger(f'ERROR: {e}', "error")







        
