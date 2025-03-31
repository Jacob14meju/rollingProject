import logging

logging.basicConfig(
        filename="/users/בית/OneDrive/שולחן העבודה/finalWork/rollingProject/infra-Automation/logs/provisioning.log.txt",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

class Machine:
    def __init__(self, name, os, cpu, ram):
        self.__name = name
        self.__os = os
        self.__cpu = cpu
        self.__ram = ram

    def get_dict(self):
        return {"name": self.__name,
                "os": self.__os,
                "cpu": self.__cpu,
                "ram": self.__ram}
    
    def loger(self):
        logging.info(f'provisioning: {self.__name}, {self.__os}, {self.__cpu}, {self.__ram}')
        print(f'provisioning: {self.__name}, {self.__os}, {self.__cpu}, {self.__ram}')