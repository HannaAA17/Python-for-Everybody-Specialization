def computepay(h, r)
    if h<=40:
        pay = h * r
    else:
        pay = 40 * r + 1.5 * (h-40) * r
    return pay

hrs = input("Enter Hours:")
try:
    hrs = float(hrs)
except:
    print("Bad Input in Hours Value")
    quit()

rph = input("Enter Rate per Hour:")

try:
    rph = float(rph)
except:
    print("Bad Input in Rate per Hour Value")
    quit()

p = computepay(hrs, rph)
print("Pay", p)