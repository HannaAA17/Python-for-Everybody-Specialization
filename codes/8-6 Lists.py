lst = list()
while True:
    num = input("Enter a number:")
    if num in ["Done", "done"]:
        break
    try:
        num = float(num)
    except:
        print("ERROR, Un valid Value:",num)
        continue
    lst.append(num)
    print(lst)
print("Maximum:",max(lst))
print("Minimum:",min(lst))