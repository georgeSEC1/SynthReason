# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 1.65
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
token = "."
tries = 25
size = 50
def convert(lst):
    return (lst.split())
def statFind(sentenceA,sentenceB,arr,threshold):
      var = 0
      for word in arr:
         try:
            if sentenceA.find(" " + word + " ")< sentenceB.rfind(" " + word + " ")>threshold:
               var += sentenceA.find(" " + word + " ") + sentenceB.find(" " + word + " ")
         except:
               False
      return var
def gather(file,user):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    sentencesA= text.split(token)
    sentencesB= text.split(token)
    for threshold in reversed(range(100)):
                 for word in words:
                          sentenceA = sentencesA[ random.randint(0,len(sentencesA)-1)]
                          sentenceB = sentencesB[ random.randint(0,len(sentencesB)-1)]
                          if statFind(sentenceA,sentenceB,words,threshold) > threshold and len(sentenceA) > 25 and len(sentenceB) > 25 and sentenceA.find(word) > -1 and sentenceB.find(word) > -1:
                                          output+= sentenceA + token 
                                          output+= sentenceB + token 
    return output
def getRandNGram(data):
   output = []
   while(True):
      i = random.randint(3,len(data)-4)
      if len(data[i]) % 2 == 0 and len(data[i+2]) % 2 == 1 or len(data[i]) % 2 == 1 and len(data[i+2]) % 2 == 0:
            output.append((data[i] + " " + data[i+1] + " " + data[i+2]).lower())
      if len(output) >= 4:
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
                text = gather(file.strip(),user)
                data= convert(text)
                output = ""
                if len(text) > 0:
                   for n in range(10):
                      for word in convert(text)[:100]:
                            if data.index(word,data.index(word)) - data.index(word) == n:
                                  output += word + " "
                if len(convert(output)) >= size:
                            print()
                            print("using " , file.strip() ,  " answering: " , user)
                            print("AI:" ,output)
                            print()
                            print()
                            f = open(filename, "a", encoding="utf8")
                            f.write("\n")
                            f.write("using " + file.strip() + " answering: " + user)
                            f.write("\n")
                            f.write("AI: " + output)
                            f.write("\n")
                            f.close()
                            if len(convert(output)) >= 1:
                                break