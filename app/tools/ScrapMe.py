import logging
import requests
import requests_random_user_agent
from bs4 import BeautifulSoup
from dotenv import dotenv_values
import pymongo

class ScrapMe:
    __requests = None
    __databaseClient = None
    __database = None

    def scrap(self) -> None:
        raise NotImplementedError('Method "scrap" must be implemented')

    def _startSession(self) -> None:
        self.__requests = requests.Session()

    def _loadPage(self, url: str) -> BeautifulSoup:
        if None is self.__requests:
            self.__requests = requests

        response = self.__requests.get(url)
        # contentType = response.headers['Content-Type'].lower().strip()
        parser = 'html.parser'

        # if 'text/html' in contentType:
        #     parser = 'lxml'
        # elif 'application/json' in contentType:
        #     parser = 'html.parser'
        # else:
        #     raise Exception('Unexpected Content-Type', contentType)

        return BeautifulSoup(response.content, parser)

    def _connectToDatabase(self) -> None:
        envs = dotenv_values('tools/.env.mongo')
        connectionString = 'mongodb://%s:%s@%s:%s/?authSource=%s' % (
            envs['DB_USER'],
            envs['DB_PASSWORD'],
            envs['DB_HOST'],
            envs['DB_PORT'],
            envs['DB_NAME']
        )

        try:
            self.__databaseClient = pymongo.MongoClient(connectionString)
            self.__databaseClient.server_info()
            self.__database = self.__databaseClient[envs['DB_NAME']]
        except Exception as exception:
            logging.exception('[SCRAPPY][ScrapMe] Cannot connect to MongoDB')
            raise exception

    def _insert(self, collectionName: str, document: dict) -> str | None:
        insertedId = None

        try:
            insertedId = self.__database[collectionName].insert_one(document).inserted_id
        except pymongo.errors.DuplicateKeyError as exception:
            logging.warning('[SCRAPPY][ScrapMe] Duplicate index key in database in collection "%s", id: %s' % (collectionName, str(document['id'])))

        return insertedId
