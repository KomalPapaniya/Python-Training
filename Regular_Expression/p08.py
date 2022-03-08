import re

string = 'firecatlioncatcatcatbearcatcatparrot'
lst = re.split('(?:cat)+', string)
print(lst)
