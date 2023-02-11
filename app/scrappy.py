import logging
import sys
from os import walk
from ScrapMe import *

class Scrappy:

    def __init__(self) -> None:
        self.initLoggers()

    def initLoggers(self) -> None:
        # STDOUT logger
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        stdoutHandler = logging.StreamHandler(sys.stdout)
        stdoutHandler.setLevel(logging.DEBUG)
        stdoutFormatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s] - %(message)s - [%(module)s/%(filename)s::%(funcName)s:%(lineno)d]')
        stdoutHandler.setFormatter(stdoutFormatter)

        root.addHandler(stdoutHandler)

    def run(self, scrapMeList = []) -> None:
        logging.info('[SCRAPPY] Scrapping started')

        # when no scrap list given, load&run all scrap files
        if not scrapMeList:
            scrapMeList = next(walk('./ScrapMe'), (None, None, []))[2]
            scrapMeList.remove('__init__.py')
            scrapMeList.remove('ScrapMe.py')
            scrapMeList = [n[:-3] for n in scrapMeList]

        for classname in scrapMeList:
            try:
                klass = globals()[classname]
                scrapMe = klass()

                logging.info('[SCRAPPY] "' + classname + '" scrapping started')
                scrapMe.scrap()
                logging.info('[SCRAPPY] "' + classname + '" scrapping ended')
            except Exception:
                logging.exception('[SCRAPPY] An exception occured during "' + classname + '" scrapping')

        logging.info('[SCRAPPY] Scrapping ended')

if __name__ == '__main__':
    scrapMeList = sys.argv[1:]

    scrappy = Scrappy()
    scrappy.run(scrapMeList)
