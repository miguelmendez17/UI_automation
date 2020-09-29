from subprocess import Popen
import pyautogui
import time

from utils import get_app_titles, get_system_language


def automation():

    # defining here as global, so here we can handle all the .exe, in case that the name changes in the future
    # and then only have to change the) value
    programs_dict = {'calculator': 'calc.exe',
                     'notepad': 'notepad.exe'}

    # this is to launch the notepad application
    Popen(programs_dict.get('notepad'))

    # this is to launch the standard Windows 10 Calculator.
    Popen(programs_dict.get('calculator'))

    # to be sure that both apps are open
    time.sleep(3)

    # right dict according to the system language
    app_titles = get_app_titles(get_system_language())

    calculator_info = pyautogui.getWindowsWithTitle(app_titles.get('calc'))[0]
    notepad_info = pyautogui.getWindowsWithTitle(app_titles.get('notepad'))[0]


if __name__ == '__main__':
    automation()
