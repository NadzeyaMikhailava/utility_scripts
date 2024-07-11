#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
import os

# the script converts HEX string to text representation and copies resulting text into the clipboard
# non-printable bytes are shown in HEX representation enclosed in angle brackets

if __name__ == "__main__":
	try:
		hex_string = sys.argv[1]
	except:
		print('The script converts HEX string to text representation and copies resulting text into the clipboard.')
		print('Run script with a valid HEX string as a first argument:\nx 313233')
		sys.exit(0)

	if len(hex_string) % 2 != 0:
		print('Run script with a valid HEX string as a first argument')
		sys.exit(0)

	for c in hex_string:
		# check that string contains only valid hex digits
		ascii_num = ord(c)
		if (
			ascii_num < 48 or
			(ascii_num > 57 and ascii_num < 65) or
			(ascii_num > 70 and ascii_num < 97) or
			ascii_num > 102
		):
			print('Run script with a valid HEX string as a first argument')
			sys.exit(0)

	print()
	result_string_for_print = ''		# may contain ANSI escape codes 
	result_string_for_clipboard = ''	# same string but without ANSI escape codes, if any

	for i in range(0, len(hex_string), 2):
		character = int(hex_string[i:i+2], 16)
		if character >= 32 and character < 127:
			# printable characters set
			result_string_for_print = result_string_for_print + chr(character)
			result_string_for_clipboard = result_string_for_clipboard + chr(character)
		else:
			result_string_for_print = result_string_for_print + '\x1B[3m\x1B[34m<' + hex_string[i:i+2] + '>\x1B[0m\x1B[27m'
			result_string_for_clipboard = result_string_for_clipboard + '<' + hex_string[i:i+2] + '>'

	print(result_string_for_print)
	# copy converted text to clipboard
	os.system("qdbus org.kde.klipper /klipper setClipboardContents \"{}\"".format(result_string_for_clipboard))
	