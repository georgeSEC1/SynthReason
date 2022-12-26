# SynthReason - Synthetic Dawn - intelligent symbolic manipulation system
# BSD 2-Clause License
# 
# Copyright (c) 2022, GeorgeSEC1 - George Wagenknecht
# All rights reserved.
import random
import re
import numpy as np
partition = 128
targetNgramSize = 3
work = 8
token = "."
def processB(proc, line):
    stat = 0
    for i in range(work):
        if line.find(" " + proc[random.randint(0,len(proc)-1)] + " ") > -1:
            stat += 1
    if stat >= work:
        return True
    return False
def convert(lst):
    return (lst.split())
def gather(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    data = convert(text)
    for word in words:
        for wordX in data:
            proc = ""
            try:
                with open(word + ".dat", encoding='ISO-8859-1') as f:
                    proc = f.read().split("\n")
                sentences = text.split(" " + proc[random.randint(0,len(proc)-1)] + " ")
                for line in sentences:
                    if line.find(wordX) < line.find("ion")  and processB(proc,line) != processB(word,line) == False :
                        return line 
            except:
                False
    return output
def process(text):
    data = convert(text)
    if len(convert(text)) >= partition*(targetNgramSize):
        chunkPos = random.randint(0,len(data)-(partition*(targetNgramSize)))
        sentences = np.array(data[chunkPos:chunkPos+(partition*(targetNgramSize))])
        sentences = sentences[:partition*(targetNgramSize)].reshape(partition,targetNgramSize)
        sync = ""
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
for question in questions:
    user = re.sub('\W+',' ',question)
    random.shuffle(files)
    for file in files:
        sync = gather(user,file.strip())
        sync = process(sync)
        if len(convert(sync)) >= partition:                  
            print()
            print("using " , file.strip() ,  " answering: " , user)
            print("AI:" ,getSentence(sync))
            print()
            print()
            f = open(filename, "a", encoding="utf8")
            f.write("\n")
            f.write("using " + file.strip() + " answering: " + user)
            f.write("\n")
            f.write(getSentence(sync))
            f.write("\n")
            f.close()
            if len(convert(sync)) >= 0:
                break