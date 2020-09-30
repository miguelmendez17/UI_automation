import locale
from subprocess import Popen
import pyautogui
import time


# docs
# https://pyautogui.readthedocs.io/en/latest/
# https://winaero.com/useful-calculator-keyboard-shortcuts-in-windows-10/

class Automation:
    def __init__(self):
        # defining here as global, so here we can handle all the .exe, in case that the name changes in the future
        # and then only have to change the) value
        self.programs_dict = {'calc': 'calc.exe',
                              'notepad': 'notepad.exe'}
        self.desktop_path = 'C:\\Users\\pc\\Desktop\\'
        self.language = None
        self.app_titles = None
        self.calculator_app = None
        self.notepad_app = None
        self.pause_each_call = 1.5
        self.pause_to_write = 0.25

    def main(self):
        # general pause for each pyautogui call
        pyautogui.PAUSE = self.pause_each_call

        # this is to launch the standard Windows 10 Calculator.
        Popen(self.programs_dict.get('calc'))
        # to have time to launch the next app without possible issues
        time.sleep(self.pause_each_call)
        # this is to launch the notepad application
        Popen(self.programs_dict.get('notepad'))
        # to be sure that both apps are open
        time.sleep(self.pause_each_call)

        # define both apps info, with these variables we can handle different actions for each app
        self.calculator_app = pyautogui.getWindowsWithTitle(self.app_titles.get('calc'))[0]
        self.notepad_app = pyautogui.getWindowsWithTitle(self.app_titles.get('notepad'))[0]

        self.basic_operations()

        self.scientific_operations()

    def basic_operations(self):

        # log the operation first in the file
        pyautogui.write('2 + 2 = ', interval=self.pause_to_write)

        self.activate_window(self.calculator_app)

        # Add 2 + 2. We want to use this in different lines to be able to visualize what is happening while is running
        pyautogui.press('2'), pyautogui.press('+'), pyautogui.press('2')
        pyautogui.press('=')
        # this is to copy the result
        pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)

        # paste the result of the addition
        pyautogui.hotkey('ctrl', 'v')

        # press enter to new line and write the operation in the file with the previous result
        pyautogui.press('enter')

        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(' * 5 = ', interval=self.pause_to_write)

        self.activate_window(self.calculator_app)

        pyautogui.press('*'), pyautogui.press('5')
        # this is the '=' button
        pyautogui.press('=')
        # this is to copy the result
        pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)

        # write the result and change the line
        pyautogui.hotkey('ctrl', 'v')

        pyautogui.press('enter')
        # write the operation in the file with the previous result
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.write(' - 10 = ', interval=self.pause_to_write)

        self.activate_window(self.calculator_app)

        pyautogui.press('-'), pyautogui.press(['1', '0'], interval=self.pause_each_call)
        # this is the '=' button
        pyautogui.press('=')
        # this is to copy the result
        pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)

        # write the result and change the line
        pyautogui.hotkey('ctrl', 'v')

        # save the file in the Desktop with the specific name (Results1.txt)
        pyautogui.hotkey('ctrl', 'g')
        pyautogui.write(self.desktop_path + 'Results1.txt', interval=self.pause_to_write)
        pyautogui.press('enter')

        # close the notepad file
        self.notepad_app.close()

        time.sleep(self.pause_each_call)

    def scientific_operations(self):

        # this is to launch the notepad application
        Popen(self.programs_dict.get('notepad'))
        time.sleep(self.pause_each_call)

        # re-define de notepad app info
        self.notepad_app = pyautogui.getWindowsWithTitle(self.app_titles.get('notepad'))[0]

        self.activate_window(self.calculator_app)

        # Clear the calculator
        pyautogui.press('del')
        # switch it to scientific mode
        pyautogui.hotkey('alt', '2')

        # Change the computation mode from degree (DEG) to radian (RAD)
        pyautogui.press('f4')

        # this is to get and copy the value of pi from calculator
        pyautogui.press('p'), pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)

        # log the operation with pi that comes from the calculator.
        pyautogui.write('cos('), pyautogui.hotkey('ctrl', 'v'), pyautogui.write(') = ')

        self.activate_window(self.calculator_app)

        # Select cos in Scientific mode.
        pyautogui.press('o')
        pyautogui.press('=')

        # this is to copy the result of the cosine of pi
        pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)

        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.write('abs('), pyautogui.hotkey('ctrl', 'v'), pyautogui.write(') = ')

        self.activate_window(self.calculator_app)

        # Take the absolute value of the result
        pyautogui.press('|'), pyautogui.press('=')

        # this is to copy the result of the absolute value
        pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)
        pyautogui.hotkey('ctrl', 'v'), pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v'), pyautogui.write(' / 2 = ')

        self.activate_window(self.calculator_app)

        # Divide the result by 2
        pyautogui.press('/'), pyautogui.press('2')
        pyautogui.press('=')
        # this is to copy the result of the division
        pyautogui.hotkey('ctrl', 'c')

        self.activate_window(self.notepad_app)
        pyautogui.hotkey('ctrl', 'v')

        # Save the .txt file to the Desktop as Results2.txt
        pyautogui.hotkey('ctrl', 'g')
        pyautogui.write(self.desktop_path + 'Results2.txt', interval=self.pause_to_write)
        pyautogui.press('enter')

        # Close the calculator and notepad
        self.calculator_app.close()
        self.notepad_app.close()

    def activate_window(self, window_to_activate):
        """
        This method is to avoid the repeating of code, because when we want to activate again a window,
        we need to have a pause.
        :param window_to_activate: windows that we want to activate
        :return: the app activated
        """
        time.sleep(self.pause_each_call)
        window_to_activate.activate()
        time.sleep(self.pause_each_call)

    def get_app_titles(self):
        """
        This method is to return the right name of the actual programs according to the system language,
        in this way, we avoid future possible issues.
        :return: the right dict
        """
        if self.language == 'english':
            self.app_titles = {
                'calc': 'Calculator',
                'notepad': 'Notepad'
            }
        else:
            self.app_titles = {
                'calc': 'Calculadora',
                'notepad': 'Bloc de notas'
            }

    def get_system_language(self):
        """
        This method is to detect the system language, in this way, we can avoid to use hard code to refer
        to title or program. We can add different languages, but for now we are going to use Eng and Spanish
        :return: the specific language
        """
        language = locale.getdefaultlocale()[0]

        if 'en' in language or 'EN' in language:
            self.language = 'english'
        else:
            self.language = 'spanish'


if __name__ == '__main__':
    automation = Automation()
    automation.get_system_language()
    automation.get_app_titles()
    automation.main()
