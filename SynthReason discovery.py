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
partition = 32
recursion = 32
targetNgramSize = 3
token = " the "
def convert(lst):
    return (lst.split())
def gather(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    sentences = text.split(token)
    for sentence in sentences:
        for word in words:
            if sentence.find(" " + word + " ") > -1:
                output += sentence + token
    return output 
def process(text,iota):
    sentences = convert(text)
    if len(convert(text)) > partition*(targetNgramSize*iota):
        sentences = np.array(sentences)
        sentences = sentences[:partition*(targetNgramSize*iota)].reshape(partition, targetNgramSize*iota)
        sync = ""
        np.sort(sentences, axis=1)
        np.sort(sentences, axis=0)
        for sentence in list(set(map(tuple,sentences))):
            for proc in sentence:
                sync += proc + " "
        return sync + " "
    return text
def getSentence(sync):
    sentences = sync.split(".")
    try:
        return '.'.join(sentences[:-1]) + "."
    except:
        return sync
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.readlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
random.shuffle(questions)
var = []
var.append("+")
var.append("-")
var.append("*")
var.append("/")
var.append("n")
var.append("m")
var.append("ord(sync[n])")
var.append("ord(sync[m])")
var.append("(")
var.append(")")
while(True):
    for question in questions:
        user = re.sub('\W+',' ',question)
        random.shuffle(files)
        length = random.randint(5,25)
        equation = ""
        for i in range(length):
            equation += var[random.randint(0,len(var)-1)]
        #equation = "round(ord(sync[n])/(m+1))"
        try:
            print("Trying: ", equation)
            Exit = False
            success = False
            for file in files:
                selection = []
                with open(file.strip(), encoding='ISO-8859-1') as f:
                    text = f.read()
                sync = gather(user,file.strip())
                for m in reversed(range(recursion)):
                    for n in range(recursion):
                        test = eval(equation)  
                        if test >= targetNgramSize:
                            sync = process(sync,test)
                            success = True
                    if Exit == True:
                        break
                if Exit == True:
                    break
                check = convert(sync)
                checkVar = random.randint(0,len(check)-1)
                stat = 0
                for i in range(partition):
                    checkX = ""
                    for cycle in range(targetNgramSize-1):
                        checkX += check[checkVar+cycle] + " "
                    if text.find(checkX) > -1:
                        stat += 1
                if len(convert(sync)) >= partition and success == True and stat > partition/4:                  
                    print()
                    print("using " , equation,  "in" , file.strip() ," answering: " , user)
                    print("AI:" ,getSentence(sync))
                    print()
                    print()
                    f = open(filename, "a", encoding="utf8")
                    f.write("\n")
                    f.write("using " + equation+ " in " + file.strip() +" answering: " + user)
                    f.write("\n")
                    f.write(getSentence(sync))
                    f.write("\n")
                    f.close()
                    if len(convert(sync)) >= 0:
                        break
        except:
            False