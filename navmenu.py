#!/usr/bin/env python

import os
import threading
import time

try:
    import keyboard
except ModuleNotFoundError:
    os.system('pip3 install keyboard')


__author__ = 'zoony'
__copyright__ = 'Copyright 2020, Lifty Community'
__version__ = '1.0.1'


if __name__ != '__main__':
    os.system('cls')

    class Menu:
        """Supported keys: SPACE, ENTER, ARROW_UP and ARROW_DOWN."""

        colors = {
            'red': '\u001b[41;1m',
            'green': '\u001b[42;1m',
            'yellow': '\u001b[43;1m',
            'blue': '\u001b[44;1m',
            'magenta': '\u001b[45;1m',
            'cyan': '\u001b[46;1m'
        }
        selected_option = 1
        selecting = True

        def display(prefix: str, indent: int, color: str, suffix: str, options: dict):
            """Available colors: red, green, yellow, blue, magenta and cyan."""

            try:
                Menu.color = Menu.colors[color.lower()]
            except KeyError:
                print(
                    'NevMenu: The available colors are: red, green, yellow, blue, magenta and cyan.'
                )
            else:
                print(prefix)
                for i, option in enumerate(options.keys(), start=1):
                    if i == 1:
                        print(f'{" " * indent}{Menu.color}[{i}] {option}\u001b[0m')
                    else:
                        print(f'{" " * indent}[{i}] {option}')
                print(suffix)

                Menu.prefix = prefix
                Menu.indent = indent
                Menu.options = options
                Menu.suffix = suffix
                threading.Thread(target=Menu.check).start()

        def check():
            while Menu.selecting:
                update = False

                if keyboard.is_pressed('down'):
                    if Menu.selected_option != len(list(Menu.options)):
                        Menu.selected_option += 1
                        update = True

                elif keyboard.is_pressed('up'):
                    if Menu.selected_option != 1:
                        Menu.selected_option -= 1
                        update = True

                elif keyboard.is_pressed('enter') or keyboard.is_pressed('space'):
                    os.system('cls')
                    list(Menu.options.values())[Menu.selected_option - 1]()
                    Menu.selecting = False

                if update:
                    os.system('cls')
                    print(Menu.prefix)
                    for i, option in enumerate(Menu.options.keys(), start=1):
                        if Menu.selected_option == i:
                            print(f'{" " * Menu.indent}{Menu.color}[{i}] {option}\u001b[0m')
                        else:
                            print(f'{" " * Menu.indent}[{i}] {option}')
                    print(Menu.suffix)
                    time.sleep(0.15)
