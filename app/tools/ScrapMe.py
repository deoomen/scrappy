import requests
import requests_random_user_agent
from bs4 import BeautifulSoup

class ScrapMe:
    __requests = None

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
