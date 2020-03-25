import re

# from datetime import datetime
print('WARNINGS: ')
with open('rsvp_agent_log.dat', 'r') as file:
    for line in file:
        line = line.rstrip()
        if re.search('WARNING:', line):
            #print(line)
            print(re.sub(r'WARNING:\S+:', '--', line))
