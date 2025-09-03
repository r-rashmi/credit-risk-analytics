import kagglehub
import pandas as pd
from pathlib import Path
import gzip

def download_dataset(logger, dataset_name):
    """
    Download a dataset from Kaggle.
    
    Args:
        logger: Logger instance for logging messages
        dataset_name: Kaggle dataset name 
    
    Returns:
        str: Path where dataset was downloaded
    """
    logger.info(f"⬇️ Downloading dataset: {dataset_name}")
    dataset_path = kagglehub.dataset_download(dataset_name)
    logger.info(f"✅ Dataset downloaded to: {dataset_path}")
    return dataset_path

def load_data_files_to_dataframes(logger, dataset_path):
    """
    Load gzip files from a dataset directory into pandas DataFrames.
    
    Args:
        logger: Logger instance for logging messages
        dataset_path: Path to the dataset directory
    
    Returns:
        dict: Dictionary with filename as key and DataFrame as value
    """
    logger.info(f"�� Loading data files from: {dataset_path}")
    
    path = Path(dataset_path)
    dataframes = {}
    
    gzip_files = list(path.glob("*.gz")) + list(path.glob("*.gzip"))
    for gzip_file in gzip_files:
        logger.info(f"Loading file: {gzip_file.name}")
        
        # .gzip files that are .csv files 
        try:
            df = pd.read_csv(gzip_file)
            dataframes[gzip_file.name] = df
            logger.info(f"✅ Loaded {gzip_file.name} as CSV with name {gzip_file.name}: {df.shape[0]} rows, {df.shape[1]} columns")
        except:
            # .gzip files
            try:
                df = pd.read_csv(gzip_file, compression='gzip')
                dataframes[gzip_file.name] = df
                logger.info(f"✅ Loaded {gzip_file.name} as gzip: {df.shape[0]} rows, {df.shape[1]} columns")
            except Exception as e:
                logger.warning(f"⚠️ Could not load {gzip_file.name}: {str(e)}")
    
    logger.info(f"✅ Successfully loaded {len(dataframes)} data files")
    return dataframes