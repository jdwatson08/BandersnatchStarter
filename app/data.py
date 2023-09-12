from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def __init__(self):
        """Instantiates the Database class and connects to the mongodb client"""
        load_dotenv()
        self.client = MongoClient(getenv("DB_URL"), tlsCAFile=where())
        self.db = self.client["Datasets"]
        self.collection = self.db['monsters']

    def seed(self, count=1000):
        """Fills the mongodb database with 1000 random instances of the monster class"""
        doc = [Monster().to_dict() for _ in range(count)]
        self.collection.insert_many(doc)

    def reset(self):
        """Deletes every instance of the Monster class from the mongodb database"""
        self.collection.drop()

    def count(self) -> int:
        """Counts the number of entries in the mongodb database"""
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """Takes oll of the entries in the mongodb database and stores them in database format. Returns the dataframe"""
        df = DataFrame(self.collection.find())
        return df

    def html_table(self) -> str:
        """Takes oll of the entries in the mongodb database and stores them in html format. Returns the html table"""
        df = self.dataframe()
        del df[df.columns[0]]
        return df.to_html()
