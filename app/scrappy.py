from datetime import datetime
from os import walk
from ScrapMe import *

if __name__ == '__main__':
    print('Scrapping started at', datetime.now())

    filenames = next(walk('./ScrapMe'), (None, None, []))[2]
    filenames.remove('__init__.py')
    filenames.remove('ScrapMeInterface.py')

    for filename in filenames:
        klass = globals()[filename[0:-3]]
        s = klass()
        s.scrap()

    print('Scrapping ended at', datetime.now())
