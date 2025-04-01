from installer import setup_runner
from machineConfig import *
from machine import *


res = inputer()
push(res)

try:
    machine_list = []
    with open("infra-Automation/configs/instances.json", "r") as file:
        file = file.read()
        fil = json.loads(file)
        for i in fil:
            machine = Machine(i["name"], i["os"], i["cpu"], i["ram"])
            machine.loger()
            machine_list.append(machine)
            logger("machine added to the list")
except Exception as e:
    logger(f'ERROR: {e}', "error")


for i in machine_list:
    dic = i.get_dict()
    setup_runner(dic["name"])

logger("done installing")