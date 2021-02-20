from forcuanteller.main import loader, transformer, reporter, sender
from forcuanteller.main.utils.gmail import validate_gmail
from forcuanteller.main.utils.logger import logger
from forcuanteller.main.utils.runner import runner
import schedule
import time


def task(sender_address, sender_password, receiver_address):
    run_id = runner.run_id
    logger.info("Run ID : {}".format(run_id))

    logger.info("Running loader...")
    loader.main(run_id)
    logger.info("Finishing loader...")

    logger.info("Running transformer...")
    transformer.main(run_id)
    logger.info("Finishing transformer..")

    logger.info("Running reporter...")
    reporter.main(run_id)
    logger.info("Finishing reporter...")

    logger.info("Running sender...")
    sender.main(run_id, sender_address, sender_password, receiver_address)
    logger.info("Finishing sender...")


def main():
    sender_address = input("Input your sender gmail address: ")
    sender_password = input("Input your sender gmail password: ")
    receiver_address = input("Input your receiver gmail address: ")

    validate_gmail(sender_address)
    validate_gmail(receiver_address)

    schedule.every(60).seconds.do(
        task, sender_address=sender_address, sender_password=sender_password, receiver_address=receiver_address
    )
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
