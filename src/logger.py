import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #log file
log_path=os.path.join(os.getcwd(),'logs')#Creates logs/ folder if it doesn’t exist.If it already exists → does nothing 
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE) #This is the  full path of your log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s',
    level=logging.INFO
)