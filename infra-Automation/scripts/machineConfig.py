import json
import sys
sys.path.append('/users/בית/OneDrive/שולחן העבודה/finalWork/rollingProject/infra-Automation/src')
from logger import logger


# scripts to configure machines
logger("the script is running")

def inputer():
    while True:
        machine_list = []
        machines = ["docker", "kubernetes", "linux", "windows"]
        name = str(input("please enter machine name (\"done\" for exit): "))
        if name.lower() == "done":
            logger("machine list is updated")
            return machine_list
        elif name.lower() not in machines:
            logger(f'machine {name} does not exist')
            continue
        else:
            os_list = ["ubuntu", "centos"]
            os = str(input("please enter the os: "))
            if os.lower() not in os_list:
                logger("os does not exist, please try again")
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



# write it on the file

res = inputer()

def writter():
    logger("adding changes to the file")
    try:
        with open("/users/בית/OneDrive/שולחן העבודה/finalWork/rollingProject/infra-Automation/configs/instances.json", "w") as file:
            file.write(json.dumps(res))

    except Exception as e:
        print(f'ERROR: {e}')

    else:
        logger("configuration succesfully saved")
    

        
