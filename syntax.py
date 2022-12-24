# SynthReason - Synthetic Dawn - discovery
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
size = 16
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
   