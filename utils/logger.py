import logging
import os
from datetime import datetime

LOGFILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

LOG_DIR = os.path.join(os.getcwd(), "logs", LOGFILE)

os.makedirs(LOG_DIR)

LOGFILE_CUR = os.path.join(LOG_DIR, LOGFILE)

logging.basicConfig(
    filename=LOGFILE_CUR,
    format = " [ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)