from bs4 import BeautifulSoup
from urllib.request import urlopen
class ScrapMe:

    def scrap(self) -> None:
        raise NotImplementedError('Method "scrap" must be implemented')

    def _loadPage(self, url: str) -> BeautifulSoup:
        html = urlopen(url).read().decode("utf-8")

        return BeautifulSoup(html, "html.parser")
