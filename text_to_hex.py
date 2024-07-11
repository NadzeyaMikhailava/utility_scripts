#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import os

# the script converts text string into HEX representation 
# and copies the resulted HEX string into clipboard

if __name__ == "__main__":
	try:
		text_string = sys.argv[1]
	except:
		print('The script converts text string into HEX representation and copies the resulted HEX string into clipboard.')
		print('Run script with a string as a first argument:\nt 123')
		sys.exit(0)

	result_string = ''
	for c in text_string:
		result_string = result_string + format(ord(c), 'X')

	print()
	print(result_string)

	# copy converted text to clipboard
	os.system("qdbus org.kde.klipper /klipper setClipboardContents \"{}\"".format(result_string))
