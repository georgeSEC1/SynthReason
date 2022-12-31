# SynthReason - Synthetic Dawn - intelligent symbolic manipulation system
# BSD 2-Clause License
# 
# Copyright (c) 2022, GeorgeSEC1 - George Wagenknecht
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
import math
partition = 32
recursion = 320
work = 8
targetNgramSize = 3
token = "."
def convert(lst):
    return (lst.split())
def gather(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    sentences = text.split(token)
    for word in words:
        for sentence in sentences:
            if sentence.find(" " + word + " ") > -1:
                output += sentence + "." 
    return output 
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
        data = convert(gather(user,file.strip()))
        procA = np.arange(start=1, stop=3000, step=2)
        procB = np.arange(start=1, stop=2000, step=30)
        result = np.convolve(procA, procB)
        sync = ""
        for i in reversed(result):
            try:
                sync += data[i-1] + " "+data[i] + " "+data[i+1] + " "
            except:
                False
        if len(convert(sync)) >= partition:                  
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