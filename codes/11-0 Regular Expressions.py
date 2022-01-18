h = open(r"C:\Users\Alberto\Downloads\Video\regex_sum_1320825.txt")
import re
hh = h.read()
lists = re.findall("[0-9]+",hh)
indx = 0
sumv = 0
for ind in lists:
    lists[indx] = int(lists[indx])
    sumv += lists[indx]
    indx += 1
print(sumv)