import pandas as pd
import numpy as np


class DataCleaning:
    """

    This class is used to clean the data extracted from the different data sources

    Attributes:
        
    """
    
    # class constructor
    
    def __init__(self, df=None):
        
        # attributes
        self.df = df
        
    # methods
    def clean_user_data(self):
        """
        This function is used to clean the user data.
        """
        if self.df is None:
            raise ValueError('DataFrame not provided to DataCleaning instance')

        # Replacing the NULL values with NaN
        self.df = self.df.replace('NULL', np.nan)

        # Converting the date columns to datetime format
        date_columns = ['date_of_birth', 'join_date']
        self.df[date_columns] = self.df[date_columns].apply(pd.to_datetime, errors='coerce')

        # Dropping the rows with missing/incorrect values in key columns
        key_columns = ['first_name', 'last_name', 'user_uuid']
        self.df = self.df.dropna(subset=key_columns)

        # Removing the rows where date_of_birth is in the future
        self.df = self.df[self.df['date_of_birth'] <= pd.Timestamp.now()]

        return self.df


    
    

    
    
   