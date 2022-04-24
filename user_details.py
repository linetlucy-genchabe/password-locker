import pyperclip
import random
import string



class User:
	'''
	Class to create user accounts and save their information
	'''

	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

        
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)

		
class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	
	credentials_list =[]
	user_credentials_list = []