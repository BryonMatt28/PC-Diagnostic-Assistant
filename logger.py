import logging

logging.basicConfig(
    filename="cpudiag.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("PC Diagnostic Assistant started")
logging.warning("High CPU usage detected")
logging.error("Unable to retrieve GPU information")