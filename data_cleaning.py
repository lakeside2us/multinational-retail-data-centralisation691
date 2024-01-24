import pandas as pd
import numpy as np


class DataCleaning:
    """

    This class is used to clean the data extracted from the different data sources

    Attributes:
        
    """
    
    # class constructor
    
    def __init__(self, df = None):
        
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
        self.df = self.df.dropna(subset = key_columns)

        # Removing the rows where date_of_birth is in the future
        self.df = self.df[self.df['date_of_birth'] <= pd.Timestamp.now()]
        
        return self.df
    
    def clean_card_data(self):
        """
        This function is used to clean the card data extracted from AWS S3 PDF file.
        """
        if self.dataframe is None:
            raise ValueError('DataFrame not provided to DataCleaning instance')

        # Removing the rows with 'NULL' in card_number
        clean_data = self.df[self.df['card_number'] != 'NULL'].copy()

        # Converting the expiry_date to datetime format with specified format
        clean_data.loc[:, 'expiry_date'] = pd.to_datetime(clean_data['expiry_date'], format = '%m/%y', errors = 'coerce')

        # Validating date_payment_confirmed using the validate function
        clean_data.loc[:, 'date_payment_confirmed'] = pd.to_datetime(clean_data['date_payment_confirmed'], errors = 'coerce')

        # Dropping the rows with invalid date_payment_confirmed
        clean_data = clean_data.dropna(subset = ['date_payment_confirmed'])

        return clean_data
    
    def clean_store_data(self, store_data):
        """
        This function is used to clean the data from API.
        """
        # Resetting the index to prevent duplicating indices after data manipulation
        store_data = store_data.reset_index(drop = True)

        # Replacing 'NULL' values with NaN
        store_data.replace('NULL', np.NaN, inplace = True)

        # Converting 'opening_date' column to datetime format
        store_data['opening_date'] = pd.to_datetime(store_data['opening_date'], errors ='coerce')

        store_data.loc[[31, 179, 248, 341, 375], 'staff_numbers'] = [78, 30, 80, 97, 39] 

        # Converting the 'staff_numbers' to numeric, drop rows with missing values
        store_data['staff_numbers'] = pd.to_numeric(store_data['staff_numbers'], errors = 'coerce')
        store_data.dropna(subset = ['staff_numbers'], axis = 0, inplace = True)

        # Cleaning the 'continent' column
        store_data['continent'] = store_data['continent'].str.replace('eeEurope', 'Europe').str.replace('eeAmerica', 'America')

        return store_data
    
    def convert_product_weights(self, products_df):
        """
        This function is used to clean up the weight.
        """
       # Converting the product weights
        def convert_weight(weight):
            try:
                unit_factors = {'g': 1, 'ml': 0.001, 'k': 1000}
                return float(weight) if isinstance(weight, (int, float)) else float(weight[:-1]) * unit_factors.get(weight[-1], 1)
            except (ValueError, TypeError):
                return None

        products_df['weight'] = products_df['weight'].apply(convert_weight)
        return products_df

    def clean_products_data(self, products_data):
        """
        This function is used to clean up erroneous values in the Products DataFrame.
        """
        # Replacing 'NULL' values with NaN
        products_data.replace('NULL', np.NaN, inplace = True)

        # Converting 'date_added' column to datetime format
        products_data['date_added'] = pd.to_datetime(products_data['date_added'], errors = 'coerce')

        # Dropping rows with missing values in 'date_added'
        products_data.dropna(subset = ['date_added'], how = 'any', axis = 0, inplace = True)

        # Converting the 'weight' column to string
        products_data['weight'] = products_data['weight'].astype(str)

        # Removing the the spaces after the dots in the 'weight' column
        products_data['weight'] = products_data['weight'].apply(lambda x: x.replace(' .', ''))

        # Extracting the numeric values from 'weight' column where it contains 'x'
        temp_cols = products_data.loc[products_data.weight.str.contains('x'), 'weight'].str.split('x', expand = True)
        numeric_cols = temp_cols.apply(lambda x: pd.to_numeric(x.str.extract('(\d+\.?\d*)', expand = False)), axis = 1)
        final_weight = numeric_cols.prod(axis = 1)
        products_data.loc[products_data.weight.str.contains('x'), 'weight'] = final_weight

        # Lowercase and strip whitespace in 'weight' column
        products_data['weight'] = products_data['weight'].apply(lambda x: str(x).lower().strip())

        # Dropping the first column (index column)
        products_data.drop(products_data.columns[0], axis = 1, inplace = True)

        return products_data
    
    def clean_orders_data(self, orders_data):
        """
        This function is used to clean up the orders table data.
        """
        # Dropping columns that are not needed.
        orders_data.drop("level_0", axis=1, inplace=True) 
        orders_data.drop("1", axis=1, inplace=True) 
        orders_data.drop(orders_data.columns[0], axis=1, inplace=True)
        orders_data.drop('first_name', axis=1, inplace=True)
        orders_data.drop('last_name', axis=1, inplace=True)
        
        return orders_data
    
    def clean_date_times_data(self, data):
        """
        This function is used to clean up the date times data.
        """
        # Converting dictionary to a DataFrame
        data = pd.DataFrame.from_dict(data)

        # Converting the 'year' column to numeric, and drop rows with missing values
        data['year'] = pd.to_numeric(data['year'], errors = 'coerce')
        data.dropna(subset = ['year'], how = 'any', axis = 0, inplace = True)

        return data
   