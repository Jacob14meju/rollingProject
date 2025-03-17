import json
import sys
sys.path.append('/users/בית/rollingProject/infra-Automation/src')
from src.logger import loger
import logging


# scripts to configure machines
print("loffing test")
loger("test")

# def inputer():
#     while True:
#         machine_list = []
#         machines = ["docker", "kubernetes", "linux", "windows"]
#         name = str(input("please enter machine name (\"done\" for exit): "))
#         if name.lower() != "done":
#             return machine_list
#         elif name.lower() not in machines:
#             print(f'machine {name} does not exist')
#             continue
#         else:
#             os_list = ["ubuntu", "centos"]
#             os = str(input("please enter the os: "))
#             if os.lower() not in os_list:
#                 print("os does not exist, please try again: ")
#                 continue
#             cpu = str(input("please enter the CPU: "))
#             ram = str(input("please enter the RAM:"))
#             adding = {"name": name,
#                       "os": os,
#                       "cpu": cpu,
#                       "ram": ram}
#             machine_list.append(adding)

# # write it on the file

# res = inputer()
# try:
#     with open("users/בית/rollingProject/infra-Automation/configs/instances.json", "w") as file:
#         file.write(json.dumps(res))

# except Exception as e:
#     print(f'ERROR: {e}')
    
# print("configuration succesfully saved")
        
