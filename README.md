# Enodo Fullstack Engineering Challenge

This README will provide a brief overview of the project structure and how to run the project yourself.

## Project Structure
- property_search (the folder where the core of the code is located)
	- static (contains the css file used for the project)
	- templates (contains index.html, the only webpage used in the project. index.html also contains the javascript used in this project, to keep the whole project concise)
	- tests (contains several test.py files for testing)
	- app.py (the Flask backend of the project)
	- database_controller.py (script to conver the Excel data into a sqlite3 database)
	- properties.db (the sqlite3 database used for this project)
	- data (contains the Excel file with property data)
- requirements.txt (file of required libraries for running the project)

## Running the project
- After ensuring all the required libraries are installed, FLASK_APP needs to be pointed towards this application [(the process varies based on your system)](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/).
- Once that is complete, navigate to the property_search folder using your CLI and run `flask run`.
- When the CLI indicates that the localhost is up and running, navigate to http://localhost:5000/search/ where you should be able to see and interact with the application.
![cli](https://github.com/bjhammack/enodo-fullstack-challenge/blob/master/screenshots/cli_server.png?raw=true "CLI Server")
- If you wish to start with a completely fresh database, open the database_controller.py file, copy the directions at the top of the file, and paste them into your command line. This will generate a new `.db` file of the name you indicate.

## Results
- When first launched, the webpage only contains the title, search bar, and table headers.
![blank](https://github.com/bjhammack/enodo-fullstack-challenge/blob/master/screenshots/blank_page.png?raw=true "Blank Page")
- Navigating to the search bar, then beginning to type an address triggers the autocomplete functionality to display.
![autocomplete](https://github.com/bjhammack/enodo-fullstack-challenge/blob/master/screenshots/autocomplete.png?raw=true "Autocomplete")
- Once one of the suggested addresses is selected, it is updated in the database and appears in the "Selected" table.
![selected](https://github.com/bjhammack/enodo-fullstack-challenge/blob/master/screenshots/selected.png?raw=true "Selected")
- This can be done continuously, searching and selecting different addresses, filling up the "Selected" table.
![selected2](https://github.com/bjhammack/enodo-fullstack-challenge/blob/master/screenshots/selected_multiple.png?raw=true "Selected 2")
- When you wish to remove a selected property, clicking the trash can to the right of that property will remove it.
![deselect](https://github.com/bjhammack/enodo-fullstack-challenge/blob/master/screenshots/deselect_hover.png?raw=true "Deselect Hover")
