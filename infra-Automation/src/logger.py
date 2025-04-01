import logging

#script to configure logging

logging.basicConfig(
        filename="infra-Automation/logs/provisioning.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def logger(msg, level="info"):
    if level == "error":
        logging.ERROR
        print(msg)
    else:
        logging.info(msg)
        print(msg)

if __name__ == "__main__":
    logger("example")