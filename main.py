# This is a sample Python script.

import os
import csv

import PySimpleGUI as sg
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import json
from fastparquet import write
from datetime import datetime


def config_handler():
    df = pd.read_json("user_config.json")
    if not df.any:
        window = sg.Window("There is no user config")
        window.close()
    filepath = df.at["filepath", 'config']
    return filepath


path = "" + config_handler()


def fixparquet(filename):
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_parquet(path + "/" + filename[0], engine='fastparquet')  # Press ⌘F8 to toggle the breakpoint.
    df.fillna(0)
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    write('transformed_' + str(current_date) + '.parquet', df)
    df.to_csv('transformed_' + str(current_date) + '.csv', sep=',', index=False)
    df = df.describe()
    df.to_csv('dataanalysis_' + str(current_date) + '.tsv', sep='\t', index=True)


def createguisearchbar(files):
    filename = ""
    layout = [[sg.Text('Listbox with search for files')],
              [sg.Input(do_not_clear=True, size=(120, 11), enable_events=True, key='_INPUT_')],
              [sg.Listbox(files, size=(120, 24), enable_events=True, key='_LIST_')],
              [sg.Button('Exit')]]

    window = sg.Window('Listbox with Search for files').Layout(layout)
    # Event Loop
    while True:
        event, values = window.Read()
        if event is None or event == 'Exit':  # always check for closed window
            break
        if values['_INPUT_'] != '':  # if a keystroke entered in search field
            search = values['_INPUT_']
            new_values = [x for x in files if search in x]  # do the filtering
            window.Element('_LIST_').Update(new_values)  # display in the listbox
        else:
            window.Element('_LIST_').Update(files)  # display original unfiltered list
        if event == '_LIST_' and len(values['_LIST_']):  # if a list item is chosen
            filename = values['_LIST_']
            sg.Popup('Selected ', values['_LIST_'])

    window.Close()
    return filename


def findfile():
    os.listdir(path)

    res = []

    # Iterate directory
    for file_path in os.listdir(path):
        # check if current file_path is a file
        if os.path.isfile(os.path.join(path, file_path)) and "parquet" in os.path.join(path, file_path):
            # add filename to list
            res.append(file_path)

    return res


def configurefile():
    files = findfile()
    # print(files)
    filename = createguisearchbar(files)
    fixparquet(filename)


def create_mock_parquet():
    df = pd.read_csv("mock_data.csv")
    write('mock_data.parquet', df)
    print("Created mock parquet")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_mock_parquet()
    configurefile()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
