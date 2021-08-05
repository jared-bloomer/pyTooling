#!/usr/bin/env python3

import sys
import logging

class logs:
  def __init__ (self, file):
    loggerFormat=logging.Formatter('%(asctime)s - %(message)s')
    self.log=logging.getLogger(file)
    self.log.setLevel(logging.DEBUG)
    self.log.propagate = False # Disable Logging to stdout
    #  create file handler which logs even debug messages
    fh = logging.FileHandler(file+'.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler(stream=None)
    ch.setLevel(logging.ERROR)
    ch.propagate = False # Disable Logging to stdout
    fh.setFormatter(loggerFormat)
    ch.setFormatter(loggerFormat)
    # add the handlers to the logger
    self.log.addHandler(fh)
    self.log.addHandler(ch)

  def write_log(self, level, message, *args, **kwargs):
    if(level=="DEBUG" or level =="debug"):
      self.log.debuginfo("DEBUG - "+message, *args, **kwargs)
    elif(level=="INFO" or level =="info"):
      self.log.info("INFO - "+message, *args, **kwargs)
    elif(level=="WARN" or level =="warn"):
      self.log.warning("WARN - "+message, *args, **kwargs)
    elif(level=="ERROR" or level =="error"):
      self.log.error("ERROR - "+message, *args, **kwargs)
    elif(level=="CRITICAL" or level =="critical"):
      self.log.critical("CRIT - "+message, *args, **kwargs)
    elif(level=="EXCEPTION" or level =="exception"):
      self.log.exception(message, *args, **kwargs)



