# Log levels 연습

import logging
import sys

for lvl in  (
    logging.DEBUG,
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
    logging.CRITICAL,
):
    print(
        f"{logging.getLevelName(lvl):8} = {lvl}"
    )
    
# Two 스테이지 필터링
    
filter_logger = logging.getLogger("demo.filter")
filter_logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)


filter_logger.addHandler(stream_handler)

filter_logger.info("INFO: will not be shown")
filter_logger.error("ERROR: will be shown")

# Configuring logs and handlers

data_logger = logging.getLogger("demo.data")
data_logger.setLevel(logging.DEBUG)

data_sh = logging.StreamHandler(sys.stdout)
data_sh.setLevel(logging.ERROR)

data_fh = logging.FileHandler("process.log","w")
data_fh.setLevel(logging.INFO)



data_logger.addHandler(data_fh)
data_logger.addHandler(data_sh)

data_logger.debug("DEBUG: will be dropped")
data_logger.info("INFO:file only")
data_logger.warning("WARNING:file only")
data_logger.error("file and console")
data_logger.critical("file and console 치명")



