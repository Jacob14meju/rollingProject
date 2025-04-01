import logging

logging.basicConfig(
        filename="/users/בית/OneDrive/שולחן העבודה/finalWork/rollingProject/infra-Automation/logs/provisioning.log.txt",
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