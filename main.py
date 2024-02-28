# # from src.mlproject.config import configuration   # for checking setup.py 
#-----------------------------
# #for logging
# from mlproject import logger

# logger.info("HA HA HAhahahahahahhahahhahahah ")
# # StreamHandler cone shown in terminal,fileHandler other saved in logs folder 
#-------------------------------------------
# from src.mlproject.logging import logger

# logger.info("Short Import using __init__ of mlproject")


#--------------------------------

# Data_ingestion

from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f'>>>>> stage{STAGE_NAME} started <<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage ={STAGE_NAME} completed <<<<<\n\n X================X")
except Exception as e:
        logger.exception(e)
        raise e