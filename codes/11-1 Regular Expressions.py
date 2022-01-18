h = open(r"D:\courses\Python\Projects\files\mbox.txt")
import re
regex = input("Enter a regular expression:")
cont = 0
for line in h:
    line = line.rstrip()
    if re.search(regex,line):
        cont += 1
print("mbox.txt had",cont,"lines that matched",regex)
