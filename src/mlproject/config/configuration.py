from mlproject.constants import *
from mlproject.utils.common import read_yaml , create_directories
#extra added except notebook:
from mlproject.entity.config_entity import DataIngestionConfig
# creating a config manager class 

class ConfigurationManager :
    def __init__(
            self, 
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig: # the entity i prepared above 
        config = self.config.data_ingestion

        create_directories([config.root_dir]) # as data inside data ingestion folder not artifact(root)

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL= config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
        

