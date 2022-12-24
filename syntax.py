# SynthReason - Synthetic Dawn - syntax discovery
# BSD 2-Clause License
import random
import re
size = 16
def convert(lst):
    return (lst.split())
with open("fileList.conf", encoding='ISO-8859-1') as x:
    files = x.readlines()
    random.shuffle(files)
    for file in files:
        with open(file.strip(), encoding='ISO-8859-1') as f:
            text = f.read()
            data = convert(text)
        array = list(set(data))
        n = 0
        while (n < len(array)-1):
            fileX = re.sub('\W+',' ',array[n])
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
                y = open(fileX+".dat", "a", encoding="utf8")
                y.write('\n'.join(list(set(db))) + "\n")
                y.close()
                print(list(set(db)))
            n+=1