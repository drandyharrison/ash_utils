import pandas as pd
from sqlalchemy import create_engine

# add decorator to make a singleton class
@singleton
class sqliteHandler:
    """Class for handling the sqlite databases"""
    # members

    # constructor methods
        pass

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
        engine = create_engine("sqlite:///"+db_name)
        csv_df.to_sql('mpg', engine, if_exists='append', index=False)

# TODO query contents of the database, as a check