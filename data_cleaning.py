import pandas as pd
import numpy as np


class DataCleaning:
    """
    This class is used to clean the data extracted from the different data sources
    """

    # methods   
    def clean_user_data(self, legacy_users_data):
        """
        This function is used to clean the user data.
        """
        # Replacing 'NULL' values with NaN
        legacy_users_data.replace('NULL', np.nan, inplace = True)
        legacy_users_data.dropna(inplace = True)
        
        # Dropping the rows with missing values in key columns
        legacy_users_data.dropna(subset = ['date_of_birth', 'email_address', 
                                           'user_uuid'], how = 'any', axis = 0, inplace = True)

        # Converting the date columns to datetime format
        legacy_users_data['date_of_birth'] = pd.to_datetime(legacy_users_data['date_of_birth'], errors = 'ignore')
        legacy_users_data['join_date'] = pd.to_datetime(legacy_users_data['join_date'],errors = 'coerce')
        legacy_users_data = legacy_users_data.dropna(subset = 'join_date')
        
        # Dropping the rows with missing values in the 'join_date' column
        legacy_users_data = legacy_users_data.dropna(subset = ['join_date'])
        
        # Cleaning the 'phone_number' column
        legacy_users_data.loc['phone_number'] = legacy_users_data['phone_number'].str.replace('/W', '')
        
        # Removing the duplicate entries based on 'email_address'
        legacy_users_data = legacy_users_data.drop_duplicates(subset = ['email_address'])
        need_to_replace = ['.', ' ']
        for i in need_to_replace:
            legacy_users_data['phone_number'] = legacy_users_data['phone_number'].str.replace(i,'')

        # Cleaning up the wrongly typed values
        legacy_users_data = legacy_users_data.drop_duplicates(subset=['email_address'])
        need_to_replace = ['.', ' ']
        for i in need_to_replace:
            legacy_users_data['phone_number'] = legacy_users_data['phone_number'].str.replace(i,'')

        # Dropping the first column (index column)
        legacy_users_data.drop(legacy_users_data.columns[0], axis = 1, inplace = True)

        return legacy_users_data
    
    
    def clean_card_data(self, card_data_table):
        """
        This function is used to clean the card data extracted from AWS S3 PDF file.
        """
        # Replacing the 'NULL' values with NaN
        card_data_table.replace('NULL',np.nan, inplace = True)
        
        # Dropping the rows with missing values in the 'card_number' column
        card_data_table.dropna(subset = ['card_number'], how = 'any', axis = 0, inplace = True)

        # Removing the rows where 'card_number' contains letters or '?'
        card_data_table['card_number'] = card_data_table['card_number'].apply(str)
        card_data_table = card_data_table[~card_data_table['card_number'].str.contains('[a-zA-Z?]', na = False)]
        
        return card_data_table
    
    
    def clean_store_data(self, store_data_table):
        """
        This function is used to clean the store data table
        """
        # Resetting the index to prevent duplicating indices after data manipulation
        store_data_table = store_data_table.reset_index(drop = True)
        
        # Replacing 'NULL' values with NaN
        store_data_table.replace('NULL', np.nan, inplace = True)
        store_data_table.drop(store_data_table.columns[0], axis=1,inplace=True)
        store_data_table.drop(columns='lat',inplace=True)
        
        # Converting 'opening_date' column to datetime format
        store_data_table['opening_date'] = pd.to_datetime(store_data_table['opening_date'], errors = 'coerce')
        
        store_data_table.loc[[31, 179, 248, 341, 375], 'staff_numbers'] = [78, 30, 80, 97, 39] 
        
        # Converting the 'staff_numbers' to numeric, drop rows with missing values
        store_data_table['staff_numbers'] = pd.to_numeric(store_data_table['staff_numbers'], errors = 'coerce')
        store_data_table.dropna(subset=['staff_numbers'], axis = 0, inplace = True)
        
        # Cleaning the 'continent' column
        store_data_table['continent'] = store_data_table['continent'].str.replace('eeEurope','Europe')
        store_data_table['continent'] = store_data_table['continent'].str.replace('eeAmerica','America')

        return store_data_table
    
    
    def convert_product_weights(self,weight):
        """
        This function is used to clean up the weight: converts the weights into kg
        """
        if 'kg' in weight:
            weight = weight.replace('kg', '')
            weight = float(weight)
        elif 'g' in weight:
            weight = weight.replace('g', '')
            weight = float(weight) / 1000
        elif 'ml' in weight:
            weight = weight.replace('ml', '')
            weight = float(weight) / 1000
        elif 'oz' in weight:
            weight = weight.replace('oz', '')
            weight = float(weight) * 0.0283495
        
        return weight
    
    
    def clean_products_data(self, s3_data_table):
        """
        This function is used to clean up erroneous values in the Products DataFrame.
        """
        # Replacing 'NULL' values with NaN
        s3_data_table.drop(s3_data_table.columns[0], axis = 1, inplace = True)

        s3_data_table.replace('NULL', np.nan, inplace = True)
        s3_data_table.dropna(inplace = True)
        
        # Converting 'date_added' column to datetime format
        s3_data_table['date_added'] = pd.to_datetime(s3_data_table['date_added'], errors = 'coerce')
        
        # Dropping rows with missing values in 'date_added'
        s3_data_table.dropna(subset = ['date_added'], how = 'any', axis = 0, inplace = True)
        
        # Converting the 'weight' column to string
        s3_data_table['weight'] = s3_data_table['weight'].astype(str)
        
        # Removing the the spaces after the dots in the 'weight' column
        s3_data_table['weight'] = s3_data_table['weight'].apply(lambda x: x.replace(' .',''))

        # Extracting the numeric values from 'weight' column where it contains 'x' 
        temp_columns = s3_data_table.loc[s3_data_table.weight.str.contains('x'), 
                                         'weight'].str.split('x', expand = True)
        
        # Splitting the suffix from the weight
        weights = temp_columns[1].str.split('(\d+\.?\d*)',expand=True)
        
        nums = temp_columns.apply(lambda x: pd.to_numeric(x.str.extract('(\d+\.?\d*)', expand=False)))
        
        new_weight = nums.prod(axis=1)
        
        # Total weight + Suffix
        final_weight = new_weight.astype(str) + weights[2]
        
        # Replacing the weight with the final weight
        s3_data_table.loc[s3_data_table.weight.str.contains('x'), 'weight'] = final_weight

        # Converting the weight into kg
        s3_data_table['weight'] = s3_data_table['weight'].apply(lambda x: self.convert_product_weights(x))

        return s3_data_table
    
    def clean_orders_data(self,orders_table):
        """
        This function is used to clean up the orders table data.
        """
        orders_table.drop(columns = 'first_name', axis = 1, inplace = True)
        orders_table.drop(columns = 'last_name', axis = 1, inplace = True)
        orders_table.drop(columns = '1', axis = 1, inplace = True)
        orders_table.drop(columns = 'level_0', axis = 1, inplace = True)
        orders_table.drop(orders_table.columns[0], axis = 1, inplace = True)

        return orders_table
    
    def clean_date_table(self,date_table):
        """
        This function is used to clean up the date times data.
        """
        date_table['year'] = pd.to_datetime(date_table['year'], errors = 'coerce').dt.year.convert_dtypes()
        date_table['month'] = pd.to_datetime(date_table['month'], errors = 'coerce', format ='%m').dt.month.convert_dtypes()
        date_table['day'] = pd.to_datetime(date_table['day'], errors = 'coerce', format = '%d').dt.day.convert_dtypes()
        date_table['timestamp'] = pd.to_datetime(date_table['timestamp'], errors = 'coerce', format = '%H:%M:%S').dt.time
        date_table.dropna(inplace = True)

        return date_table