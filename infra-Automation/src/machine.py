

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
    
    def logger(self):
        print(f'New machine just made, name: {self.__name}, os: {self.__os}, cpu: {self.__cpu}, ram: {self.__ram}')