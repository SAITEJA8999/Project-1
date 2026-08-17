import logging
import os
from datetime import datetime

LOG_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_file)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(levelname)s-%(message)s",
    level=logging.INFO,
    
)

##if __name__=="__main__":
# to check the logger class is working or not we can run the below code in the same filef
## logging.info("Logging has started")