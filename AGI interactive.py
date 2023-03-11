# SynthReason - Synthetic Dawn - AGI - intelligent symbolic manipulation system - 1.95
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
import math
token = "."
tries = 25
size = 75
def convert(lst):
    return (lst.split())
def statFind(sentence,arr):
      var = 0
      for word in arr:
         try:
            if sentence.count(" " + word + " ") > 0:
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
def getRandNGram(data,i):
      output = []
      i = round(i)
      output.append((data[i] + " " + data[i+1] + " " + data[i+2]).lower())
      if len(output) == 1:
          return output
def syllable_count(mode,word):
    word = word.lower()
    count = 0
    vowels = mode
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count
with open("fileList.conf", encoding='ISO-8859-1') as f:
    files = f.readlines()
print("SynthReason - Synthetic Dawn")
with open("questions.conf", encoding='ISO-8859-1') as f:
	questions = f.readlines()
filename = "Compendium#" + str(random.randint(0,10000000)) + ".txt"
random.shuffle(questions)
while(True):
          user_input = re.sub('\W+',' ',input("USER: " ).lower())
          random.shuffle(files)  
          for file in files:
                input_text = gather(file.strip(),user_input)
                data= convert(input_text)
                output = ""
                if len(input_text) > 0:
                    for i in range(tries):
                          if len(convert(output)) >= size:
                              break
                          rand = np.random.default_rng().uniform(0,len(data)-3,10000)
                          for target_word in convert (input_text):
                                 if len(convert(output)) >= size:
                                      	break
                                 for i in rand[::13]:
                                 		if len(convert(output)) >= size:
                                 			break
                                 		try:
                                	 		ngramsA = getRandNGram(data,i)
                        	         		ngramsB = getRandNGram(data,i+4)
                        	         		ngrams_str = ' '.join(ngramsA) + " " + ' '.join(ngramsB) + " "
                        	         		syllables_matching_word_countA = syllable_count(user_input, ngrams_str)
                        	         		syllables_matching_word_countB = syllable_count(target_word,user_input)
                        	         		word_occurrence_count = ngrams_str.count(target_word)
                        	         		word_index = ngrams_str.find(target_word),
                        	         		if syllables_matching_word_countA+syllables_matching_word_countB >  syllables_matching_word_countB and math.sqrt(syllables_matching_word_countA * syllables_matching_word_countB)  < ngrams_str.rfind(target_word):
                        	         		       output+= ngrams_str
                        	         		       ngramsA = getRandNGram(data,i+8)
                        	         		       ngramsB = getRandNGram(data,i+12)
                        	         		       
                                 		except:
                                 			False
                    if len(convert(output)) >= size:
                            print()
                            print("using " , file.strip() ,  " answering: " , user_input)
                            print("AI:" , output)
                            print()
                            print()
                            f = open(filename, "a", encoding="utf8")
                            f.write("\n")
                            f.write("using " + file.strip() + " answering: " + user_input)
                            f.write("\n")
                            f.write(output)
                            f.write("\n")
                            f.close()
                            if len(convert(output)) >= size:
                                break