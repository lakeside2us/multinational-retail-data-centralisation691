import yaml
import sqlalchemy
from sqlalchemy import create_engine, inspect
import psycopg2

class DatabaseConnector:
    """
    This class is used to connect to both local database and relational AWS database
    
    Attributes:
        yaml_file(str): the yaml file that contains the credentials needed to connect to the databases.
    """
    
    # class constructor
    
    def __init__(self, yaml_file):
        
        # attributes
        self.yaml_file = yaml_file
        self.credentials = self.read_db_creds
        
    # methods
    def read_db_creds(self):
        """
        This function is used to read the credentials in the yaml file.
        """
        
        with open(self.yaml_file, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    
    def init_db_engine(self):
        """
        This function is used to initialise the db engine using the credentials in the yaml file.
        """
        
        # Extracting the credentials
        credentials = self.read_db_creds()
        
        database = credentials['RDS_DATABASE']
        host = credentials['RDS_DATABASE']
        port = credentials['RDS_PORT']
        user = credentials['RDS_USER']
        password = credentials['RDS_PASSWORD']
        
        # Database connection URL
        db_conn_url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        
        # Creating and returning the sqlalchemy engine
        engine = sqlalchemy.create_engine(db_conn_url)
        return engine
        
        
    def list_db_tables(self):
        """
        This function is used to list all the tables in the database.
        """
        # Connecting to the database
        engine = self.init_db_engine()
        
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names
    
    def upload_to_db(self, df, table_names):
        """
        This function is used to upload data into the database.
        """
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = 'lak3sid3'
        DATABASE = 'sales_data'
        PORT = 5432
        engine_2 = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        df.to_sql(table_names, engine_2, index = True, if_exists = 'replace')
        
v = DatabaseConnector()

    
    
        

        
    
        
        
        
        
        
        
        
        