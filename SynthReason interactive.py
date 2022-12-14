# SynthReason - Synthetic Dawn - intelligent symbolic manipulation system
# BSD 2-Clause License
# 
# Copyright (c) 2023, GeorgeSEC1 - George Wagenknecht
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import random
import re
import numpy as np
token = "the"
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
def convert(lst):
    return (lst.split())
def gather(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    for word in words:
        sentences = text.split(".")
        for sentence in sentences:
            if sentence.find(" " + word + " ") > -1:
                output += sentence
    return output 
def removeConsecutive(result):
    previous_value = None
    new_lst = []
    for elem in result:
        if elem != previous_value:
            new_lst.append(elem)
            previous_value = elem
    return new_lst
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.readlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
random.shuffle(questions)
while(True):
    user = re.sub('\W+',' ',input("USER: "))
    random.shuffle(files)
    for file in files:
        text = gather(user,file.strip())
        data = convert(text)
        if len(data) > 0:
            g1 = random.randint(0,102400)
            g2 = random.randint(0,320)
            g1 = 82401
            g2 = 112
            pos = random.randint(0,len(data)-1)
            procA = np.arange(start=1, stop=30000, step=3)
            procB = np.arange(start=1, stop=20000, step=1)
            procX = np.geomspace(1, g1, num=g2, dtype=int)
            result = np.sort(np.convolve(procB, np.concatenate((procX, procA))))
            sync = ""
            var = 0
            try:
                var = data.index(token,pos)
            except:
                False
            for i in range(len(result)):
                try:
                    if len(re.sub('\W+',' ',data[var+result[i]-1] + " " + data[var+result[i]] + " " + data[var+result[i]+1] + " ")) > len(data[var+result[i]-1] + " " + data[var+result[i]] + " " + data[var+result[i]+1] + " ")-2:
                        sync += data[var+result[i]-1] + " " + data[var+result[i]] + " " + data[var+result[i]+1] + " "
                except:
                    False
            sync = ' '.join(removeConsecutive(convert(sync)))
            if len(convert(sync)) >= 1:   
                print("Geometry:\ng1 =",g1,"\ng2 =",g2)
                print()
                print("using " , file.strip() ,  " answering: " , user)
                print("AI:" ,sync)
                print()
                print()
                f = open(filename, "a", encoding="utf8")
                f.write("\n")
                f.write("using " + file.strip() + " answering: " + user)
                f.write("\n")
                f.write(sync)
                f.write("\n")
                f.close()
                if len(convert(sync)) >= 0:
                    break