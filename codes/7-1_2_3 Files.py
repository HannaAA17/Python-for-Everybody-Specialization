# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    fh = open(fname)
except:
    print("File cannot be opened:",fname)
    quit()


count = 0
addition = 0
count1 = 0
for line in fh:
    count1 += 1
    if not line.startswith("X-DSPAM-Confidence:"):
        #print((line.rstrip()).upper())
        continue
    #print((line.rstrip()).upper())
    temp = 0
    temp = float(line[line.find(":")+1:])
    count += 1
    addition += temp
print("Average spam confidence:",addition/count)
#print(f"There were {count1} subject lines in {fname}")