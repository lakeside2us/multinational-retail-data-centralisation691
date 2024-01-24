from database_utils import DatabaseConnector
import pandas as pd
import tabula 
import requests
import boto3
import os


class DataExtractor:
    """

    This class is used to extract the data from different data sources

    Attributes:
        db: the yaml file that contains the credentials needed to connect to the databases.
        rds_db: the rds file that contains the credentials
        api.key
    """
    
    # class constructor
    
    def __init__(self):
        
        # attributes
        self.db = DatabaseConnector()
        self.rds_db = self.db.init_db_engine()
        self.api_key ={'x-api-key':'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
    
    # methods
    def read_rds_table(self, db_connector, table_names):
        """
        This function is used to extract the table containing user data to a pandas DataFrame.
        """
        engine = db_connector.init_db_engine()
        query = f"SELECT * FROM {table_names}"
        df = pd.read_sql(query, engine)
        return df
    
    def retrieve_pdf_data(self, link):
        """
        This function is used to extract data from the PDF file in the AWS S3 bucket.
        """
        data_pdf = tabula.read_pdf(link, pages = 'all')
        pdf_df = pd.concat(data_pdf)
        return pdf_df
    
    def list_number_of_stores(self, endpoint, header):
        """
        This function is used to return the number of stores.
        """
        stores = requests.get(endpoint, headers = header)
        num_of_stores = stores.json().get('number_stores')
        return num_of_stores
    
    def retrieve_stores_data(self, retrieve_store_endpoint, headers, num_stores):
        stores_data = []

        for store_number in range(1, num_stores + 1):
            store_endpoint = f"{retrieve_store_endpoint}/{store_number}"

            try:
                response = requests.get(store_endpoint, headers=headers)

                if response.status_code == 200:
                    store_info = response.json()
                    stores_data.append(store_info)
                else:
                    print(f"Error: Unable to retrieve store {store_number}. Status code: {response.status_code}")

            except Exception as e:
                print(f"Error: {e}")

        stores_df = pd.DataFrame(stores_data)
        return stores_df
    
    def extract_from_s3(self, s3_address):
        s3_client = boto3.client('s3')
        products_data = None

        # Parsing the S3 address
        bucket_name, key = s3_address.split('//')[1].split('/', 1)
        
        # Downloading the S3 file
        local_file_name = 'products.csv'
        s3_client.download_file(bucket_name, key, local_file_name)
        
        # Reading the CSV to a DataFrame
        products_data = pd.read_csv(local_file_name)

    
        # Cleaning up/Closing the local file
        products_data.to_csv(local_file_name, index = False)
        products_data = pd.read_csv(local_file_name)
        
        # Removing the local file
        os.remove(local_file_name)
        
        return products_data
    
        
    
    
    
    
        
