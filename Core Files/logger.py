import logging

class LoggerSystem:

    def __init__(self):
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename="log_files/cpudiag.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def log_startup(self):
        logging.info("PC Diagnostic Assistant started")

    def log_diagnostics(self, cpu_usage_perc, ram_usage):
        logging.info("CPU Usage: %s%%", cpu_usage_perc)
        logging.info("RAM Usage: %s%%", ram_usage)