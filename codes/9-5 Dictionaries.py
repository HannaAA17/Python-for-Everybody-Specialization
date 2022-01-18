name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
#print(handle.read())
count=dict()
maxname = ""
maxnum = 0
for line in handle:
    temp = []
    if not line.startswith("From "):
        continue
    else:
        temp = (((line.split())[1]).split("@"))[1]
        count[temp] = count.get(temp,0) + 1
        if maxname == "" or maxnum < count[temp]:
            maxname = temp
            maxnum = count[temp]

print(maxname,maxnum)