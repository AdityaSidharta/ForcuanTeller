from forcuanteller.main import loader, transformer, reporter
from forcuanteller.main.utils.logger import logger
from forcuanteller.main.utils.runner import runner


def main():
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
    sender.main(run_id)
    logger.info("Finishing sender...")

if __name__ == "__main__":
    main()
