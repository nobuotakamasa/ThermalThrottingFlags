import time
import os
import datetime

def rdmsr(reg, cpu):
    filename = "/dev/cpu/" + str(cpu) + "/msr"
    with open(filename, 'rb') as f:
        f.seek(reg)
        v = f.read(4)
    #value = int(v[0]) + (int(v[1]) << 8) + (int(v[2]) << 16) + (int(v[3]) << 24)
    return v


cpus = os.listdir(path="/dev/cpu")
ncore = 0
for cpu in cpus:
    try:
        n = int(cpu[0])
        ncore +=1
    except:
        pass
print(ncore, "cores")

print(",", end='')
for i in range(ncore):
    print(str(i)+",,", end='')
print("")
print(",", end='')
for i in range(ncore):
    print("flag,degree,", end='')
print("")

while True:
    value = []
    for i in range(ncore):
        value.append(rdmsr(0x19c, i))
    print(datetime.datetime.today(),",",end='')
    for v in value:
        flag = v[0] & 1
        temp = 100 - int(v[2] & 0x7f)
        print(str(flag)+","+str(temp)+",", end='')
    print("")
    time.sleep(1)
