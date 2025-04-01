import logging

#script to build a machine class

logging.basicConfig(
        filename="infra-Automation/logs/provisioning.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

class Machine:

    #constractor
    def __init__(self, name, os, cpu, ram):
        self.__name = name
        self.__os = os
        self.__cpu = cpu
        self.__ram = ram

    #function to return object properties in dict format
    def get_dict(self):
        return {"name": self.__name,
                "os": self.__os,
                "cpu": self.__cpu,
                "ram": self.__ram}
    
    # logger for machine making
    def loger(self):
        logging.info(f'provisioning: {self.__name}, {self.__os}, {self.__cpu}, {self.__ram}')
        print(f'provisioning: {self.__name}, {self.__os}, {self.__cpu}, {self.__ram}')