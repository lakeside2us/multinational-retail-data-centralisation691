import pandas as pd
import numpy as np


class DataCleaning:
    def __init__(self, dataframe=None):
        self.dataframe = dataframe

    # Cleaning the legacy user data
    def clean_user_data(self, legacy_users_table):
        legacy_users_table = legacy_users_table.copy()  # To avoid SettingWithCopyWarning warning

        # Replacing the 'NULL' values with NaN
        legacy_users_table.replace('NULL', np.NaN, inplace = True)

        # Dropping the rows with missing values in key columns
        legacy_users_table.dropna(subset = ['date_of_birth', 'email_address', 
                                            'user_uuid'], how = 'any', axis = 0, inplace = True)

        # Converting the date columns to datetime format
        legacy_users_table['date_of_birth'] = pd.to_datetime(legacy_users_table['date_of_birth'], 
                                                             errors = 'ignore')
        legacy_users_table['join_date'] = pd.to_datetime(legacy_users_table['join_date'], 
                                                         errors = 'coerce')

        # Dropping the rows with missing values in the 'join_date' column
        legacy_users_table = legacy_users_table.dropna(subset = ['join_date'])

        # Cleaning the phone_number column
        legacy_users_table['phone_number'] = legacy_users_table['phone_number'].str.replace('/W', '')

        # Removing the duplicate entries based on email_address
        legacy_users_table = legacy_users_table.drop_duplicates(subset = ['email_address'])

        # Dropping the first column (index column)
        legacy_users_table.drop(legacy_users_table.columns[0], axis = 1, inplace = True)

        return legacy_users_table 
    
    # Cleaning the card data
    def clean_card_data(self, card_data_table):
        
        # Replacing the 'NULL' values with NaN
        card_data_table.replace('NULL', np.NaN, inplace = True)

        # Dropping the rows with missing values in the card_number column
        card_data_table.dropna(subset = ['card_number'], how = 'any', axis = 0, inplace = True)

        # Removing the rows where card_number contains letters or '?'
        card_data_table = card_data_table[~card_data_table['card_number'].str.contains('[a-zA-Z?]', na = False)]

        return card_data_table
    
    # Cleaning the store data
    def clean_store_data(self, store_data):
        
        # Resetting the index to avoid duplicate indices after manipulation
        store_data = store_data.reset_index(drop = True)

        # Replacing the 'NULL' values with NaN
        store_data.replace('NULL', np.NaN, inplace = True)
        
        # Dropping the rows with missing values in the opening_date column
        store_data.dropna(subset = ['opening_date'], how = 'any', axis = 0, inplace = True)

        # Converting the opening_date column to datetime format
        store_data['opening_date'] = pd.to_datetime(store_data['opening_date'], errors = 'coerce')

        store_data.loc[[31, 179, 248, 341, 375], 'staff_numbers'] = [78, 30, 80, 97, 39]

        # Converting the staff_numbers to numeric, and dropping the rows with missing values
        store_data['staff_numbers'] = pd.to_numeric(store_data['staff_numbers'], errors = 'coerce')
        store_data.dropna(subset = ['staff_numbers'], axis = 0, inplace = True)

        # Cleaning the continent column
        store_data['continent'] = store_data['continent'].str.replace('eeEurope', 
                                                                      'Europe').str.replace('eeAmerica', 'America')

        return store_data
    
    # Converting the product weights
    def convert_product_weights(self,weight):
        """
        This function converts the weights into kg
        """
        if 'kg' in weight:
            weight = weight.replace('kg','')
            weight = float(weight)
        elif 'g' in weight:
            weight = weight.replace('g','')
            weight = float(weight) / 1000
        elif 'ml' in weight:
            weight = weight.replace('ml','')
            weight = float(weight) / 1000
        elif 'oz' in weight:
            weight = weight.replace('oz','')
            weight = float(weight) * 0.0283495
        
        return weight
    
    # Cleaning the products data
    def clean_products_data(self,s3_data_table):
        """
        This function cleans the products data table
        """
        s3_data_table.drop(s3_data_table.columns[0], axis = 1, inplace = True)

        s3_data_table.replace('NULL', np.nan, inplace = True)
        s3_data_table.dropna(inplace = True)

        s3_data_table['date_added'] = pd.to_datetime(s3_data_table['date_added'],errors = 'coerce')
        s3_data_table.dropna(subset = ['date_added'],inplace = True)

        s3_data_table['weight'] = s3_data_table['weight'].apply(lambda x: x.replace(' .',''))

        # Using a temporary columns to calculate the weight of objects to give the weigh as 12 x 100g 
        temp_columns = s3_data_table.loc[s3_data_table.weight.str.contains('x'), 
                                         'weight'].str.split('x',expand = True)
        
        # Splitting the suffix from the weight
        weights = temp_columns[1].str.split('(\d+\.?\d*)', expand = True)
        
        # Extracting the numbers 
        nums = temp_columns.apply(lambda x: pd.to_numeric(x.str.extract('(\d+\.?\d*)', expand = False)))
        
        # Total weight
        weight_new = nums.prod(axis =1 )
        
        # Total weight + suffix
        weight_final = weight_new.astype(str) + weights[2]
        
        # Replacing the weight with final weight
        s3_data_table.loc[s3_data_table.weight.str.contains('x'), 'weight'] = weight_final

        # Converting the weight into kg
        s3_data_table['weight'] = s3_data_table['weight'].apply(lambda x: self.convert_product_weights(x))

        return s3_data_table
    
    # Cleaning the date times data
    def clean_date_table(self, data_table):
        # Convert dictionary to a DataFrame
        data_table = pd.DataFrame.from_dict(data_table)

        # Convert 'year' column to numeric, drop rows with missing values
        data_table['year'] = pd.to_numeric(data_table['year'], errors='coerce')
        data_table.dropna(subset=['year'], how='any', axis=0, inplace=True)

        return data_table
    
    # Clean orders data
    def clean_orders_data(self, data):
        
        # Dropping the unnecessary columns
        data.drop("level_0", axis=1, inplace = True)
        data.drop("1", axis=1, inplace = True) 
        data.drop(data.columns[0], axis=1, inplace = True)
        data.drop('first_name', axis=1, inplace = True)
        data.drop('last_name', axis=1, inplace = True)
        
        return data