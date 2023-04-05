# Python-project

1. The content of the project directory consists of the following files:
• Filmy.py – main program
• Lista.txt – a file containing data to be loaded into our database

2. Introduction
The database was created to collect and organize information about movies. Upon running the program, a menu with various options to choose from will be presented in the terminal.

3. Loading from file and displaying as a table
At the beginning of the menu, there is an option to load pre-made movies with data using the function load_data_from_file(). The program will display the number of records in the file. This function, along with the function display_data_in_table_format(), allows us to display all movies in the order specified in the list.txt file.

4. Sorting
After choosing this option, the program will present us with sorting methods based on criteria. This is very useful if we want the data to be presented in chronological order. A comparison function is created for each criterion.

5. Search
In order to avoid unnecessary searching in a large database, the search option will help us find a specific movie. This is option number 4 in the menu. After selecting this option, the program will ask for the search method, such as title, category, year of release, and length of the movie. A keyword should be entered after selecting the search option. If there is no movie in our database that meets the given criterion, the program will display a message about their absence. Otherwise, it will be displayed in table format.

6. Adding a movie to the database
The function responsible for adding a movie to the database is add_record(). The program will ask for such data as: movie title, category, production year, and movie length. Unfortunately, when entering data, be careful not to enter Polish characters (this leads to table widening in a given row) and in the case of a multi-part movie title, enter the movie title together or use "_" instead of a space. This can lead to the movie title being split into several columns.

7. Deleting a movie from the database
The function responsible for deleting a movie from the database is delete_record(). It completely removes all data from a given record. If we enter the wrong record (non-existent or already deleted), the message "No record to delete" will be displayed. In case of a correctly made choice, we will see "Record successfully deleted". To see the effect, we must display the table before and after the operation.

8. Saving and exiting the program
After choosing option number 7, we have the option to save our changes to a file using the function save_data_to_file(). The file we want to create with our data can be named arbitrarily. If everything is correct, the message "Successfully saved to file" will pop up. At this point, we can be sure that our data has been saved correctly and exit the terminal safely.
