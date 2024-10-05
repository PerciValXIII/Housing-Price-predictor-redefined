import os 
import zipfile
from abc import ABC, abstractmethod
import pandas as pd


# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, filepath: str) -> pd.DataFrame
    """ Abstract Method to Ingest data from a given data file"""
    
    