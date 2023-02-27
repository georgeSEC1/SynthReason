# SynthReason - Synthetic Dawn - intelligent symbolic manipulation system - 78.3
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
threshold= 300
size = 200
token = "."
def statFind(sentence,arr):
      var = 0
      for word in arr:
         try:
            if sentence.find(" " + word + " ") < sentence.rfind(" " + word + " ")  :
               var += sum(list(map(ord,sentence)))
            if (sentence+token).find(" " + word + token) > (sentence+token).rfind(" " + word + token):
               var += sum(list(map(ord,sentence)))
         except:
               False
      return var
def gather(user,file):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    sentences = text.split(token)
    for sentence in reversed(sentences):
            if statFind(sentence,words) > threshold:
                    output += sentence + token
    return output
def pos(i):
      try:     
                 items = convert("is of and")
                 if data[i][0].isupper() == False and (data[i] + " " + data[i+1] + " " + data[i+2] + " ").lower().isprintable() == True:
                       return (data[i] + " " + data[i+1] + " " + data[i+2] + " ").lower()
                 if data[i][0].isupper() == True and (data[i-1] + " " + data[i] + " " + data[i+1] + " ").lower().isprintable() == True and data[i] in items:
                       return (data[i-1] + " " + data[i] + " " + data[i+1] + " ").lower()
      except:
            return data[random.randint(0,len(data)-1)].lower()
def posB(word):
         try:
               x =  random.randint(1,len(data)-2)      
               db = np.append(data.index(word,x)-1,data.index(word,x),data.index(word,x)+1)
               return db
         except: 
              True
def convert(lst):
    return (lst.split())
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
              text = gather(user,file.strip())
              data = convert(text)
              if len(data) > 0: 
                  db =  list(map(posB,data[:size]))
                  db = [i for i in db if i is not None]
                  db =  list(map(pos,db))
                  db = [i for i in db if i is not None]
                  sync =  ' '.join(db)
                  if len(convert(sync)) >= 1:
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