import logging
import logging.config
from typing import Any, Dict
import json
# print("Declarartvie confiurartion using ini files")
# print("==========\n")

# config_path = "./declarative-config.ini"

# logging.config.fileConfig(
    
#     fname = config_path,
# )

# app_logger = logging.getLogger("app")
# app_logger.debug("INI-style fileConfig is working!")


# print("---------------\n")

# dict_config : Dict[str, Any] = {
#     "version" : 1,
#     "disable_existing_loggers":False,
#     "formatters" : {
#         "simple": {
#             "format": "%(levelname) -8s - %(message)s"
#         }
#     },
#     "handlers":{
#         "console":{
#             "class":"logging.StreamHandler",
#             "level":"INFO",
#             "formatter":"simple",
#             "stream":"ext://sys.stdout",
#         }
#     },
#     "loggers":{
#         "config.dict":{
#             "level":"DEBUG",
#             "handlers":["console"],
#         }
#     },
# }

# logging.config.dictConfig(dict_config)
# config_logger = logging.getLogger("config.dict")
# config_logger.debug("dictConfig setup successfully")
# config_logger.info("Info goes to console")

config_path = "declarative-config.json"
with open(config_path, "r") as config_file:
    json_config = json.load(config_file)
    
    
logging.config.dictConfig(json_config)
config_logger = logging.getLogger("config.json")
config_logger.debug("json Config setup successfully")
config_logger.info("Info goes to console")

# Dynamic building config

base_config: Dict[str, Any] = {
    "version":1,
    "disable_existing_loggers": True,
    "handlers":{},
    "formatters":{},
    "loggers":{},
    
    
}

base_config["formatters"]["simple"] = {
    "format": "%(levelname) -8s - %(message)s"
}

base_config["handlers"]["console"] = {
    "class":"logging.StreamHandler",
    "level":"DEBUG",
    "formatter":"simple",
    "stream":"ext://sys.stdout"
    
}

base_config["loggers"]["config.dynamic"] = {
    "level" : "WARNING",
    "handlers":["console"],
}
def is_debug():
    return True

if is_debug():
    for logger, _config in base_config["loggers"].items():
        base_config["loggers"][logger]["level"] = "DEBUG"



logging.config.dictConfig(base_config)
config_logger = logging.getLogger("config.dynamic")
config_logger.debug("Dynamic Config setup successfully")
config_logger.info("Info goes to console")