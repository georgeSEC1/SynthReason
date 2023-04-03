# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 4.5
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
token = " of the "
tries = 1500
size = 1500
def convert(lst):
    return (lst.split())
def statFind(sentence,arr):
      var = 0
      for word in arr:
         try:
            if sentence.count(" " + word + " ") > 1:
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
                    if statFind(sentence,words) > len(words)/4:
                          output += sentence + token
    return output
def getRandNGram(data):
   output = []
   while(True):
      i = random.randint(3,len(data)-3)
      output.append((data[i] + " " + data[i+1] + " " + data[i+2]).lower())
      if len(output) == 1:
          return output
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count *= 2
    for index in range(1, len(word)):
        if word[index] not in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    return count
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
                    for word in range(tries):   
                        for i in range(len(data)):
                                    ngramsA = getRandNGram(data)
                                    try:
                                      if convert(' '.join(ngramsA))[2] == data[i+syllable_count(' '.join(ngramsA) )]:
                                          output+= (' '.join(ngramsA)+ " ")
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