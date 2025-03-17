import logging

def setup_log():
    logging.basicConfig(
        filename="users/בית/rollingProject/infra_Automation/logs/provisioning.log.txt",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

logg = setup_log()