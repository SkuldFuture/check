import os
import time


source = ['C:\\rat', 'C:\\rabbit']

target_dir = 'C:\\backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter comment --> ')
if len(comment) == 0:
	target = today + os.sep + now + '.rar'
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.rar'

if not os.path.exists(today):
	os.mkdir(today)
print('Dict created', today)

rar_command = "rar a {0} {1}".format(target, ' '.join(source))

print(rar_command)

if os.system(rar_command) == 0:
	print('backup created successfully in', target)
else:
	print('backup failed')