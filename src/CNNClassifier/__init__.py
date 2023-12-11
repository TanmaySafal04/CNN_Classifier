
import os
import sys
import logging

logging_str = "[ %(asctime)s:  %(levelname)s:     %(module)s]:      %(message)s" 
'''               TIME          LOGGING LEVEL      WHICH MODULE      ERROR MESSAGE
                                INFO               ERROR IS COMING 
                                DEBUG etc.         FROM
'''
log_dir="logs"

log_filepath = os.path.join(log_dir,"running_logs.log")

os.makedirs(log_filepath, exist_ok=True)

logging.basicConfig(

   level = logging.INFO,
   format = logging_str,
   handlers = [  
               logging.FileHandler() ,
               logging.StreamHandler(sys.stdout)
               ]
)
logging.getLogger("CNNClassifier")
logger = logging