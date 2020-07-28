import sqlite3
from flask import Flask, render_template, jsonify, request

def dict_factory(cursor, row):
	'''
	Function to convert sqlite queries to dictionaries.
	'''
	new_dict = {}
	for k,v in enumerate(cursor.description):
		new_dict[v[0]] = row[k]

	return new_dict

def get_db_connection(db_name):
	'''
	Establishes connection to sqlite3 database.
	
	Input: name of sqlite3 database
	Return: sqlite cursor and connection
	'''
	conn = sqlite3.connect(db_name)
	conn.row_factory = dict_factory
	return conn.cursor(), conn

class CustomFlask(Flask):
	'''
	Custom Flask class to eliminate issues with Vue.js and Flask sharing command characters.
	'''
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
		block_start_string='(%',
		block_end_string='%)',
		variable_start_string='((',
		variable_end_string='))',
		comment_start_string='(#',
		comment_end_string='#)',
	))

app = CustomFlask(__name__)

@app.route('/search/get', methods=['GET'])
def search_get():
	'''
	GET method to retrieve currently selected properties.

	Return: Dictionary of selected properties converted to special JSON format using flask.jsonify()
	'''
	cursor, conn = get_db_connection('properties.db')
	selected_properties = cursor.execute('SELECT PIN, FULL_ADDRESS, CLASS_DESCRIPTION FROM PROPERTIES WHERE SELECTED = 1').fetchall()
	conn.close()
	print(jsonify(selected_properties))
	return jsonify(selected_properties)

@app.route('/search/new', methods=['POST'])
def search_new():
	'''
	POST method that updates the database with a new selected property.

	Return: jsonify'd 'ok' status
	'''
	cursor, conn = get_db_connection('properties.db')
	if request.json:
		pin = request.json['PIN']
		
		sql = 'UPDATE PROPERTIES SET SELECTED = {} WHERE PIN = {}'.format(1, pin).format(1, pin)
		cursor.execute(sql)
		conn.commit()
		conn.close()
	return jsonify(status='ok')

@app.route('/search/delete', methods=['POST'])
def search_delete():
	'''
	POST method that updates database when a selected property is removed.

	Return: jsonify'd 'ok' status
	'''
	cursor, conn = get_db_connection('properties.db')
	pin = request.json['PIN']
	if request.json:
		sql = 'UPDATE PROPERTIES SET SELECTED = {} WHERE PIN = {}'.format(0, pin)
		cursor.execute(sql)
		conn.commit()
		conn.close()
	return jsonify(status='ok')

@app.route('/search/data', methods=['GET'])
def search_data():
	'''
	GET method that gets the PIN and address of all properties to populate the autocomplete.

	Return: jsonify'd dictionary of properties
	'''
	cursor, conn = get_db_connection('properties.db')
	properties = cursor.execute('SELECT PIN as link, FULL_ADDRESS as value FROM PROPERTIES').fetchall()
	conn.close()
	
	return jsonify(properties)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	'''
	Function that renders index.html regardless of which protocol is called.
	'''
	return render_template("index.html")