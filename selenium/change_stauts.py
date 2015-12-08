# -*- coding: utf-8 -*-
#auto change status of project
from selenium import webdriver
import time, logging, os, functools
#init log
logging.basicConfig(filename = os.path.join(os.getcwd(), "log_status.txt"), 
	level = logging.DEBUG, 
	filemode ="w", 
	format = "%(asctime)s - %(levelname)s: %(message)s")

#decorator function
def log_maker(func):
	@functools.wraps(func)
	def log_wrapper(*args, **kw):
		callmsg = "call %s(): "% func.__name__
		logging.debug(callmsg)
		#
		func(*args, **kw)
		#
		closemsg = "close %s()! "% func.__name__
		logging.debug(closemsg)
		return True
	return log_wrapper

@log_maker
def init_browser():
	#init driver
	driver = webdriver.Chrome()
	#init browser
	return driver


@log_maker
def login(user, pwd):
	driver.find_element_by_id("loginname").clear()
	driver.find_element_by_id("loginname").send_keys(user)
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys(pwd)
	driver.find_element_by_id("button").click()

#close browser
# driver.close()

#close log

if __name__ == "__main__":
	try:
		init_browser.get("http://gix5-stag.glodon.com")
		login("mpc01@126.com", "123123")
	except Exception, e:
		logging.exception(e)
	finally:
		init_browser.close()
	

