from database_utils import DatabaseConnector
import pandas as pd
import tabula 


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
        
    
    
    
    
        
