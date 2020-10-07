# Create a program that backs up all our important files

# PROGRAM DESIGN
# 1. files and directories to be copied to the list
# 2. backups should be stored in the main reserve directory
# 3. files are placed in a zip-archive
# 4. the name for the zip-archive is the current date and time
# 5. download command zip for Windows

import os
import time


source = ['C:\\rat', 'C:\\rabbit']

target_dir = 'C:\\backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.rar'

rar_command = "rar a {0} {1}".format(target, ' '.join(source))

print(rar_command)

if os.system(rar_command) == 0:
	print('backup created successfully in', target)
else:
	print('backup failed')

