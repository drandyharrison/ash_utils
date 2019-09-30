import pandas as pd
from sqlalchemy import create_engine

class sqliteHandler:
    """Class for handling the sqlite databases"""
    # members
    __dbname = None     # name of the sqlite database
    __engine = None     # sqlite db engine

    # constructor methods
    def __init__(self, dbname : str):
        if not (isinstance(dbname, str)):
            raise TypeError("@creator: {} is not a string".format(dbname))
        __dbname = dbname
        __engine = create_engine("sqlite:///"+__dbname)

    # destructor method
    def __del__(self):
        print("{} died".format(self.__class__.__name__))

    def csv_to_sqlite(csv_name : str, db_name : str, table_name : str):
        """Populate a sqlite DB from a CSV
        :param csv_name: str
            name of CSV file to be read
        :param db_name: str
            name of sqlite database file - create and populate or append if already exists
        :param table_name: str
            name of table to populate with contents of CSV
        """
        csv_df = pd.read_csv(csv_name)
        print(csv_df.head())
        csv_df.to_sql('mpg', __engine, if_exists='append', index=False)


    def sqlite_to_df(db_name: str, table_name: str):
        """Populate Dataframe from a table in a SQlite database
        :param db_name: str
            name of database to read from
        :param table_name: str
            name of table to populate the DataFrame from
        """
        df = pd.read_sql("SELECT * FROM " + table_name, __engine)
        # also see read_sql_query() and read_sql_table()

        return df
