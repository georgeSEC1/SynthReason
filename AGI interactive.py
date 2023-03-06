# SynthReason - Synthetic Dawn - expert knowledge system - 1.66
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
size = 50
def convert(lst):
    return (lst.split())
def gather(file,user):
    with open(file, encoding='ISO-8859-1') as f:
        text = f.read()
    data = convert(text)
    output = ""
    wordlist = convert(user)
    wordfreq = []
    for w in wordlist:
           wordfreq.append(data.count(w))
    words = list(zip(wordlist, wordfreq))
    res = sorted(words, key = lambda x: x[1]) 
    sentences= text.split(token)
    for word in res:
          for sentence in sentences:
                if sentence.find(" " + word[0] + " ") > -1:
                      output += sentence + " "
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
                           output= ' '.join(data[:200])
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