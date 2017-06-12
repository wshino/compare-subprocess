import subprocess
from easyprocess import EasyProcess
import subprocess32

timeout = 3

print "#### use subprocess ####"
# use subprocess
# timeout can not set
# stdout is display in realtime
command = ['ping', 'localhost', '-t', '5']
child = subprocess.Popen(command)
# s = child.communicate(timeout=timeout)[0] timeout can not set
s = child.communicate()[0]


print "#### use easyprocess ####"
# use easyprocess
# timeout can set
# stdout is display when finished
s = EasyProcess('ping localhost -t 5').call(timeout=timeout).stdout
print(s)


print "#### use subprocess32 ####"
# use subprocess32
# timeout can set
# stdout is display in realtime
command = ['ping', 'localhost', '-t', '5']
child = subprocess32.Popen(command)
try:
    s = child.communicate(timeout=timeout)[0]
except subprocess32.TimeoutExpired:
    print "timeout"