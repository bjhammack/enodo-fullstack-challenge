'''
STEPS FOR GENERATING A DATABASE:

from database_controller import Database
import pandas as pd
db = Database('properties.db')
db.close_connection()
'''

import sqlite3
import pandas as pd

class Database(object):
	def __init__(self, db_name):
		'''
		Creates a sqlite3 connection (or fires error if it cannot), converts excel file to DataFrame, adds the SELECTED column,
		converts DataFrame to database tabel via function call.
		'''
		conn = None

		try:
			conn = sqlite3.connect(db_name)
			print(sqlite3.version)
		except sqlite3.Error as e:
			print(e)
		finally:
			if conn:
				self.conn = conn

				full_df = pd.read_excel('data/Enodo_Skills_Assessment_Data_File.xlsx').rename(columns={'Full Address':'FULL_ADDRESS'\
					,'Latitude':'LATITUDE','Longitude':'LONGITUDE','Zip':'ZIP'})
				full_df['SELECTED'] = 0
				self._generate_db_from_excel(full_df)

	def close_connection(self):
		'''
		Closes connection to database instance.
		'''
		if self.conn:
			self.conn.close()

	def _generate_db_from_excel(self, df):
		'''
		Takes previously generated DataFrame and sends to the established database connection, overwriting the table specified.
		'''
		df.to_sql('PROPERTIES', self.conn, if_exists='replace', index = False)