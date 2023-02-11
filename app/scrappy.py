import logging
import sys
from os import walk
from tools import *
from scripts import *

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
            scrapMeList = next(walk('./scripts'), (None, None, []))[2]
            scrapMeList.remove('__init__.py')

        for scriptName in scrapMeList:
            try:
                if scriptName.endswith('.py'):
                    scriptName = scriptName[:-3]
                else:
                    continue

                klass = globals()[scriptName]
                scrapMe = klass()

                logging.info('[SCRAPPY] "' + scriptName + '" scrapping started')
                scrapMe.scrap()
                logging.info('[SCRAPPY] "' + scriptName + '" scrapping ended')
            except Exception:
                logging.exception('[SCRAPPY] An exception occured during "' + scriptName + '" scrapping')

        logging.info('[SCRAPPY] Scrapping ended')

if __name__ == '__main__':
    scrapMeList = sys.argv[1:]

    scrappy = Scrappy()
    scrappy.run(scrapMeList)
