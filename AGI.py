# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 1.47
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
def statFind(sentence,arr):
      var = 0
      for word in arr:
         try:
            if sentence.find(" " + word + " ") > -1:
               var += 1
         except:
               False
      return var
def gather(file,user):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    output = ""
    words = convert(user)
    sentences = text.split(token)
    for sentence in sentences:
                    if statFind(sentence,words) > len(words)/2:
                          output += sentence + token
    return output
def getRandNGram(data):
   output = []
   while(True):
      i = random.randint(3,len(data)-3)
      if data[i][0].isupper() == False and ( data[i] + " " + data[i+1] + " " + data[i+2]).lower().isprintable() == True:
            output.append((data[i] + " " + data[i+1] + " " + data[i+2]).lower())
      if data[i][0].isupper() == True and ( data[i-1] + " " + data[i] + " " + data[i+1]).lower().isprintable() == True:
            output.append((data[i-1] + " " + data[i] + " " + data[i+1]).lower()) 
      if len(output) == 4:
          return output
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.readlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
random.shuffle(questions)
with open("verbs.txt", encoding='ISO-8859-1') as f:
	verb = f.readlines()
with open("nouns.txt", encoding='ISO-8859-1') as f:
	nouns = f.readlines()
for question in questions:
          user = re.sub('\W+',' ',question)
          random.shuffle(files)  
          for file in files:
                text = gather(file.strip(),user)
                data= convert(text)
                output = ""
                if len(text) > 0:
                      for count in range(tries):             
                        ngramsA = getRandNGram(data)
                        ngramsB = getRandNGram(data) 
                        ngramsC = getRandNGram(data) 
                        for word in convert(text):
                                    try:
                                       if convert( (' '.join(verb) + " " +' '.join(ngramsB) + " " + ' '.join(ngramsC))).index(word) >-1 <  ((' '.join(ngramsA) + " " +' '.join(nouns) + " " + ' '.join(ngramsC))).index(word) > -1:
                                          output+= (' '.join(ngramsA) + " " + ' '.join(ngramsB) + " " + ' '.join(ngramsC) + " ")               
                                          ngramsA = getRandNGram(data)
                                          ngramsB = getRandNGram(data)
                                          ngramsC = getRandNGram(data) 
                                    except:
                                       False
                                    if len(convert(output)) >= size:
                                        break
                        if len(convert(output)) >= size:
                                        break
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
                            f.write(output)
                            f.write("\n")
                            f.close()
                            if len(convert(output)) >= 1:
                                break