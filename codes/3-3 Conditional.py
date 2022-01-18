score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Bad Input")
    exit()
if score>1 or score<0:
    print("Out of Range")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6:
    print("F")