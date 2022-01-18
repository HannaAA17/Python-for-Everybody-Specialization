name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
line = list()
count = dict()
for line in handle:
  	if not line.startswith("From "):
  		continue
  	else:
  		temp = (((line.split())[5]).split(":"))[0]
  		count[temp] = count.get(temp,0) + 1
Hhh = sorted([(k,v) for k,v in count.items()])
for t,tt in Hhh:
	print(t,tt)