from itemadapter import ItemAdapter
import sqlite3
import datetime
from decimal import Decimal
import pdb


class ScrapytutorialPipeline(object):

	# init method to initialize the database and
	# create connection and tables
	def __init__(self):
		
		# Creating connection to database
		self.create_conn()
		
		# calling method to create table
		self.create_table()

	# create connection method to create database
	# or use database to store scraped data
	def create_conn(self):
		
		# connecting to database.
		self.conn = sqlite3.connect("n11.db")
		
		# collecting reference to cursor of connection
		self.curr = self.conn.cursor()


	# Create table method using SQL commands to create table
	def create_table(self):
		self.curr.execute("""DROP TABLE IF EXISTS product""")
		self.curr.execute("""CREATE TABLE IF NOT EXISTS PRODUCTS(Id INTEGER PRIMARY KEY AUTOINCREMENT, 
																Title TEXT, 
																Price REAL, 
																Link TEXT, 
																Store TEXT,
																Market TEXT,
																CreateDate TIMESTAMP)""")

	# store items to databases.
	def process_item(self, item, spider):
		self.putitemsintable(item)
		return item

	def putitemsintable(self, item):
		
		currentDateTime = datetime.datetime.now()
		for i in range(len(item['title'])):
		# extracting item and adding to table using SQL commands.
			self.curr.execute("""INSERT INTO PRODUCTS (Title, Price, Link, Store, Market, CreateDate)VALUES (?,?,?,?,?,?)""", (
				item['title'][i],
				item['price'][i],
				item['link'][i],
				item['store'],
				item['market'],
				currentDateTime
			))
		self.conn.commit() # closing the connection.