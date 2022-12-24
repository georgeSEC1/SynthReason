# SynthReason - Synthetic Dawn - syntax discovery
# BSD 2-Clause License
import random
import re
size = 16
def convert(lst):
    return (lst.split())
with open("xaa", encoding='ISO-8859-1') as f:
    text = f.read()
    data = convert(text)
array = list(set(data))
n = 0
while (n < len(array)-1):
    file = re.sub('\W+',' ',array[n])
    proc = text.split(" " + re.sub('\W+',' ',array[n]) + " ",size)
    db = []
    m = 0
    while (m < len(proc)-1):
        try:
            if convert(proc[m])[0].find(":") == -1:
                db.append(convert(proc[m])[0])
        except:
            False
        m+=1
    if len(db) > 1:
        f = open(file+".dat", "a", encoding="utf8")
        f.write('\n'.join(list(set(db))) + "\n")
        f.close()
        print(list(set(db)))
    n+=1
   