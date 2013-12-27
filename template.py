#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging


class Sample(object):
# magic methods
    def __init__(self):
        logging.debug(u'__init__')
        pass

    def __del__(self):
        logging.debug(u'__del__')
        pass

# public methods
    def start(self):
        logging.debug(u'Sample.start() started.')

        logging.debug(u'Sample.start() ended.')

    def increment(self, x):
        return x+1


if __name__ == "__main__":
    logging.basicConfig(
        # filename='sample.log', level=logging.DEBUG),
        format=u'[%(asctime)s] [%(levelname)s] [%(threadName)s] %(message)s',
        level=logging.DEBUG,
        stream=os.sys.stdout
    )
    logging.info(u'test started.')

    sample = Sample()
    logging.info(sample.increment(1))

    logging.info(u'test ended.')
