import subprocess
import sys

commandList = []
for x in range(1,len(sys.argv)):
	commandList.append(sys.argv[x])

print(commandList)
completed = subprocess.call(commandList)
print('returncode:',completed)
