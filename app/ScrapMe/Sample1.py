from ScrapMe.ScrapMeInterface import ScrapMeInterface

class Sample1(ScrapMeInterface):

    def scrap(self):
        print('Scrapping from', __class__.__name__)
