text = "X-DSPAM-Confidence:    0.8475"
pl = text.find(".")
print(float(text[text.find(":")+1:]))