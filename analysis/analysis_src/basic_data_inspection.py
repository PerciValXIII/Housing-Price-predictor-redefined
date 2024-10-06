from abc import ABC, abstractmethod
import pandas as pd


class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        Performs specific type of data inspection
        Parameters:  pd.Dataframe - The dataframe which is to be inspected
        Returns: None

        """
        pass


class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nData Types and non-null count : ")
        print(df.info())

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\nDataset Summary Statistics - Numerical Features : ")
        print(df.describe())
        print("\nDataset Summary Statistics - Categorical Features : ")
        print(df.describe(include=["0"]))



# Context Class that uses a DataInspectionStrategy
# ------------------------------------------------
# This class allows you to switch between different data inspection strategies.
class DataInspector:
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the DataInspector with a specific inspection strategy.
        Parameters: strategy (DataInspectionStrategy): The strategy to be used for data inspection.
        Returns: None

        """
        self._strategy = strategy

    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.
        Parameters: strategy (DataInspectionStrategy): The new strategy to be used for data inspection.
        Returns: None

        """
        self._strategy = strategy

    def execute_inspection(self, df: pd.DataFrame):
        """
        Executes the inspection using the current strategy.
        Parameters: df (pd.DataFrame): The dataframe to be inspected.
        Returns: None: Executes the strategy's inspection method.

        """
        self._strategy.inspect(df)

# Example usage
if __name__ == "__main__":
    # Example usage of the DataInspector with different strategies.

    # Load the data
    # df = pd.read_csv('../extracted-data/AmesHousing.csv')

    # Initialize the Data Inspector with a specific strategy
    # inspector = DataInspector(DataTypesInspectionStrategy())
    # inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    # inspector.execute_inspection(df)
    pass
