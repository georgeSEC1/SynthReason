# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 3.6
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
import wikipedia
token = "."
size = 125
tries = 25
def convert(lst):
    return (lst.split())
def statFind(sentence,arr):
      var = 0
      for word in arr:
         try:
            if sentence.count(" " + word + " ") > 1:
               var += 1
               count += 1
         except:
               False
      return var
def gather(user):
    output = ""
    words = convert(user)
    for word in words:
        try:
            string =  wikipedia.search(word)
            data = wikipedia.page(string[random.randint(0,len(string)-1)])
            output += data.content
        except:
            False
    return output
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
random.shuffle(questions)
while(True):
          user = re.sub('\W+',' ',input("USER: "))
          text = gather(user)
          output = ""
          if len(text) > 0:
                    for j in range(tries):
                    	for words in text.split(token):
                    	  	words = convert(words)
                    	  	symploces = []
                    	  	for i in range(len(words)-10):
                    	      		if words[i].isalpha() and words[i+1].isalpha() and words[i+2].isalpha():
                    	      		   if words[i].lower() == words[i+4].lower():
                    	      		       string = words[i] + " " + words[i+1]+ " " + words[i+2]+ " " + words[i+3]
                    	      		       if output.find(string) == -1 :
                    	      		           output += string + " "
                    	if len(output)>= size:
                    	    break
          if len(output)>= size: 
                            print()
                            print(" answering: " , user)                            
                            print("AI:" ,output)
                            print()
                            print()
                            f = open(filename, "a", encoding="utf8")
                            f.write("\n")
                            f.write( " answering: " + user)
                            f.write("\n")
                            f.write(output)
                            f.write("\n")
                            f.close()