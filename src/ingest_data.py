import os 
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, filepath: str) -> pd.DataFrame:
        """ Abstract Method to Ingest data from a given data file"""
        pass


# Implement a concrete class for ZipIngestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, filepath: str) -> pd.DataFrame:
        """Extracts data from a zip file and returns the contents in a pandas dataframe"""
        # Check if the file is .zip
        if(filepath.endswith(".zip") == False):
            raise ValueError("The provided file is not a zip file")
        
        # extract the zip file 
        with zipfile.ZipFile(filepath, "r") as zipf:
            zipf.extractall("extracted_data")
        
        # Find all the csv files from the extracted list
        extracted_files = os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV Files were located in the extracted data")
        elif len(csv_files) > 1:
            raise ValueError("Multiple CSV Files found, please specify which oen to use")
        
        # Read the CSV into a dataframe 
        csv_file_path = os.path.join("extracted_data",csv_files[0])
        df = pd.read_csv(csv_file_path)

        # Return the dataframe
        return df
    

# Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(filepath: str) -> DataIngestor:
        """ Return the appropriate DataIngestor based on file extension """
        if filepath.endswith(".zip"):
            return ZipDataIngestor()
        else:
            raise ValueError(f"No Ingestor found for the file type: {filepath}")

    
# Example Usage
if __name__ == "__main__":
    # #specify the filepath
    # filepath = "/Users/percival/Work/Housing Data Project/data/archive.zip"

    # #get the appropraite  DataIngestor
    # data_ingestor = DataIngestorFactory.get_data_ingestor(filepath)
    
    # #ingest the data and load into a dataframe 
    # df = data_ingestor.ingest(filepath)

    # print(df.head())
