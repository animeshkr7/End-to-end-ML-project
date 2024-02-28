#data ingestion config 

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)  # a dectorator , frozer =true -> will not take any extra variable
class DataIngestionConfig:
    root_dir : Path
    source_URL : str 
    local_data_file : Path
    unzip_dir : Path