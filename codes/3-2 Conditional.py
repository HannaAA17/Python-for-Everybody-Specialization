hrs = input("Enter Hours:")
rph = input("Enter Rate per Hour:")
hrs = float(hrs)
rph = float(rph)

if hrs <= 40:
    Pay = hrs * rph
else:
    Pay = 40 * rph + 1.5 * (hrs-40) * rph

print(Pay)