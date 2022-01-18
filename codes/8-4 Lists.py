fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = (line.rstrip()).split()
    for word in line:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)