fhandle = open('mbox-short.txt')
#read = fhandle.read()
counter = 0
value = 0
for line in fhandle:
    if "X-DSPAM-Confidence:" in line:
        z = line.find(":")
        x = line[z+2:]
        fl = float(x)
        counter = counter + 1
        value = value + fl
print("Average spam confidence:", value/counter)
