import logging
import sys
from os import walk
from ScrapMe import *

if __name__ == '__main__':
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

    logging.info('Scrapping started')

    filenames = next(walk('./ScrapMe'), (None, None, []))[2]
    filenames.remove('__init__.py')
    filenames.remove('ScrapMeInterface.py')

    for filename in filenames:
        classname = filename[0:-3]
        klass = globals()[classname]
        s = klass()

        try:
            s.scrap()
        except Exception as exception:
            logging.error('An exception occured during "' + classname + '" scrapping')


    logging.info('Scrapping ended')
