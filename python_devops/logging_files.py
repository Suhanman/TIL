# Basic logging with FileHandler
import logging
import os
import logging.handlers
import time

def cleanup_log_files(base_name: str):
    for file_name in os.listdir("."):
        if file_name.startswith(base_name):
            os.remove(file_name)

print("Basics logging with FileHandler")
print("------------------\n")

logger = logging.getLogger("file.basic")
logger.setLevel(logging.DEBUG)

basic_fh = logging.FileHandler("basicfile.log", delay = True, encoding="utf-8")
basic_fh.setLevel(logging.INFO)

logger.addHandler(basic_fh)

logger.info("INFO : will be written to file")


#Size-based log rotation with RotatingFileHandler

print("Size-based log rotation with RotatingFileandelr")
print("-----------\n")

rotating_logs_filename = "rotatingfile.log"

cleanup_log_files(rotating_logs_filename)
        
rotating_logger = logging.getLogger("file.rotating")
rotating_logger.setLevel(logging.DEBUG)

rotating_fh = logging.handlers.RotatingFileHandler(
    rotating_logs_filename,
    maxBytes=500,
    backupCount=2,
    encoding="utf-8",
)

rotating_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)

rotating_logger.addHandler(rotating_fh)

for i in range(30):
    rotating_logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.05)
    
    
print("---------------------")

timed_rotating_logs_filename = "timedrotatingfile.log"
cleanup_log_files(timed_rotating_logs_filename)

timed_rotating_logger = logging.getLogger("file.rotating")
timed_rotating_logger.setLevel(logging.DEBUG)


timed_rotating_fh = logging.handlers.TimedRotatingFileHandler(
    timed_rotating_logs_filename,
    when="S",
    interval=3,
    backupCount=2,
    encoding="utf-8",
)

timed_rotating_fh.setFormatter(
    logging.Formatter("%(levelname)-8s %(message)s")
)


timed_rotating_logger.addHandler(timed_rotating_fh)

for i in range(30):
    timed_rotating_logger.info(f"Entry {i}: {'Z' * 50}")
    time.sleep(0.2)
    