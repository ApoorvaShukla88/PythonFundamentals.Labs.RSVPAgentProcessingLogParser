import re
#from datetime import datetime

file = open('rsvp_agent_log.dat')

for line in file:
    line = line.rstrip()
    if re.search('WARNING:', line):
        print(line[0:14]+' -- '+ line[45:])
    else:
        pass
