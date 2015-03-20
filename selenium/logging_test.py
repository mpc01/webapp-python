#-*- coding:utf-8 -*-
#logging test

import logging, os

#init logger
logger = logging.getLogger("logmaker")
logger.setLevel(logging.DEBUG)

#set formatter
log_formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")

#write to file:log.txt
log_file = logging.FileHandler(os.path.join(os.getcwd(), "log.txt"))
log_file.setLevel(logging.DEBUG)
log_file.setFormatter(log_formatter)

#display log on console
console_display = logging.StreamHandler()
console_display.setLevel(logging.DEBUG)
console_display.setFormatter(log_formatter)

#add file and stream handler to logger
logger.addHandler(log_file)
logger.addHandler(console_display)

if __name__ == '__main__':
	logger.debug("debug message!")
	logger.info("info message!")
