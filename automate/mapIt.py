# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open('https://www.google.com/maps/place/'+address)
