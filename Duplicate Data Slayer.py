import PySimpleGUI as sg
import pandas as pd
import os


def remove_duplicates(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Count the initial number of rows
    initial_rows = len(df)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Count the number of rows removed
    rows_removed = initial_rows - len(df)

    # Save the cleaned DataFrame to a new CSV file
    cleaned_file_name = os.path.basename(file_path).replace('.csv', '_cleaned.csv')
    cleaned_file_path = os.path.join(os.getcwd(), cleaned_file_name)
    df.to_csv(cleaned_file_path, index=False)

    # Save the report to a text file
    report_file_name = os.path.basename(file_path).replace('.csv', '_report.txt')
    report_file_path = os.path.join(os.getcwd(), report_file_name)
    with open(report_file_path, 'w') as f:
        f.write(f'Number of duplicate rows removed: {rows_removed}')

    return cleaned_file_path, report_file_path


# GUI layout
layout = [
    [sg.Text('Select a CSV file to clean:')],
    [sg.Input(key='-FILE-', enable_events=True), sg.FileBrowse()],
    [sg.Button('Remove Duplicates'), sg.Button('Exit')]
]

window = sg.Window('Data Cleaning Wizard', layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == '-FILE-':
        file_path = values['-FILE-']

    if event == 'Remove Duplicates':
        if 'file_path' not in locals():
            sg.popup('Please select a CSV file first!')
        else:
            try:
                cleaned_file_path, report_file_path = remove_duplicates(file_path)
                sg.popup(
                    f'Duplicates removed!\nCleaned file saved as:\n{cleaned_file_path}\nReport saved as:\n{report_file_path}')
                window.close()  # Close the window after displaying the popup
            except Exception as e:
                sg.popup(f'An error occurred: {e}')
                window.close()  # Close the window after displaying the error popup

window.close()



