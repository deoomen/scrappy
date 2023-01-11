from ScrapMe.ScrapMe import ScrapMe

class Sample1(ScrapMe):

    def scrap(self) -> None:
        print('Scrapping from', __class__.__name__)
