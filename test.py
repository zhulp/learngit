#!/usr/bin/python

import httplib
import time
from time import clock

import logging
import logging.config
logging.config.fileConfig("logging.conf")
#create logger
logger = logging.getLogger("root")

print "hello"
logger.info("count:" + "hello" + " status:" + "world")
logger.info("count1:" + "hello" + " status:" + "world")
logger.info("count2:" + "hello" + " status:" + "world")
print "world"
exit()
