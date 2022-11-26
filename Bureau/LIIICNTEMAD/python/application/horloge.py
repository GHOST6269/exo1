import time 

s = 0
min = 0
h = 0

while True:
    if s<60 :
        s += 1
        time.sleep(1)
    if s == 60:
        s = 0
        min +=1
    if min == 60:
        min = 0
        h += 1
    print(h,"h",min,"min",s,"s")
