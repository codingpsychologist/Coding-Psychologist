This script provides a simple graphical user interface (GUI) for removing duplicate rows from a CSV file. 
It utilizes the PySimpleGUI library for creating the GUI and the pandas library for data manipulation.

Inspiration
One of my first projects using PySimpleGUI was in 2019, when I created my first psych report assistant. Ever
since, I have been fascinated with GUIs in Python. So after learning about the pandas library, I decided to 
try out this feature in the data analytics field, and in my amazement, it worked. I am excited about my Python
journey and hope to share it with the world.

Prerequisites
Python 3.x
PySimpleGUI library
pandas library

Usage
Make sure you have Python 3.x installed on your system.
Install the required libraries by running the following command:

pip install PySimpleGUI pandas
Save the code provided in a Python file (e.g., data_cleaning_wizard.py).

Run the script by executing the following command:

python data_cleaning_wizard.py
The Data Cleaning Wizard window will appear.

Click the Browse button and select the CSV file you want to clean.

Click the Remove Duplicates button to start the cleaning process.
If you haven't selected a CSV file, a message will pop up asking you to select a file first.
If an error occurs during the cleaning process, an error message will be displayed.
After the cleaning is complete, a message will pop up showing the paths to the cleaned CSV file and the report file.

Click the Exit button or close the window to exit the application.

How it Works
The script imports the necessary libraries: PySimpleGUI and pandas.
The remove_duplicates function is defined. It takes a file path as input and performs the following steps:
Loads the CSV file into a pandas DataFrame.
Counts the initial number of rows.
Removes duplicate rows from the DataFrame.
Counts the number of rows removed.
Saves the cleaned DataFrame to a new CSV file.
Generates a report file with the number of duplicate rows removed.
The GUI layout is defined using PySimpleGUI. It consists of a text label, an input field for file selection, and two buttons: Remove Duplicates and Exit.

The script creates a PySimpleGUI window with the defined layout.
The event loop starts, waiting for user interactions.
If the window is closed or the Exit button is clicked, the event loop breaks, and the application exits.
If a file is selected using the input field, the file path is stored in a variable.
If the Remove Duplicates button is clicked, the script checks if a file is selected. If not, a popup message is displayed. If a file is selected, the remove_duplicates function is called with the file path.
If the cleaning process is successful, a popup message shows the paths to the cleaned CSV file and the report file.
If an error occurs during the cleaning process, an error popup is displayed.
The PySimpleGUI window is closed at the end of the event loop.

License
This script is released under the MIT License. See the LICENSE file for more information.# Coding-Psychologist
