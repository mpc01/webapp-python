#-*- coding: utf-8 -*-
#verify the new user who come from different branches

from selenium import webdriver
import time

#setup broswer
def setUp(website):
	driver = webdriver.Chrome()
	driver.get(website)


#simulated users click the different branch link , register, login,
def branchLink():
	pass


#check the database if this new users take marks from the branch
def checkBranch():
	import mysql.connector

#teardown broswer
def tearDown():
	driver.close()

if __name__ == '__main__':
	main()