import re

# from datetime import datetime
print('WARNINGS: ')
with open('rsvp_agent_log.dat', 'r') as file:
    for line in file:
        line = line.rstrip()
        if re.search('WARNING:', line):
            pattern = re.compile(r'WARNING:.....mailslot_create:')
            new_line = re.sub(pattern, '--', line)
            print(new_line)




#             print(line)
#
# pattern = re.compile(r'')
#
# # pattern = re.compile(r'....')
# # matches = pattern.finditer()
# # for line in matches:
# #     print(line)
