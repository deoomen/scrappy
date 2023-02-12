import logging
from dotenv import dotenv_values
import pymongo

ENV_FILE = 'tools/.env.mongo'

class DatabaseMongo:
    __databaseClient = None
    __database = None

    def connectToDatabase(self) -> None:
        envs = dotenv_values(ENV_FILE)
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

    def insert(self, collectionName: str, document: dict) -> str | None:
        insertedId = None

        try:
            insertedId = self.__database[collectionName].insert_one(document).inserted_id
        except pymongo.errors.DuplicateKeyError as exception:
            logging.warning('[SCRAPPY][ScrapMe] Duplicate index key in database in collection "%s", id: %s' % (collectionName, str(document['id'])))

        return insertedId

    def deleteById(self, collectionName: str, id: str):
        self.__database[collectionName].delete_one({ '_id': id })
