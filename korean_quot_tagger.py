#Copyright 2018 UNIST under XAI Project supported by Ministry of Science and ICT, Korea

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#   https://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
#!/usr/bin/env python

import os
import time
import codecs
import optparse
import numpy as np
from loader import prepare_sentence
from utils import create_input, iobes_iob, zero_digits
from model import Model
from multiprocessing import Process, Queue
import copy
import re

class korean_quot_tagger(object):
    def to_bigram(self,input_line, line_num):
    
        bigram =''
        line = input_line.strip()
        #pattern = re.compile(' ')
        line = re.sub(' ', '^', line)
        #line = '^' + line
        #print(line)
        #first_line_start = 0
        #if line_num == 1: first_line_start = 1

        #print line
        for word_idx in range(len(line)):
            if word_idx == 0:
                prev = '^'
            else:
                prev = line[word_idx-1]
            bigram += prev+line[word_idx]+' '
	        
        #pattern = re.compile('\^') 
        #bigram = re.sub(pattern, 'whitespace', bigram)
        bigram += '\r\n'

        #print(bigram)
        return bigram
    def bigrams_to_unigrams(self,bigrams):
        unigrams = []
        for bigram in bigrams:
            if bigram.startswith('^'):
                unigrams+=[bigram[1]]
                #print bigram[1]
            else :
                if bigram.find('^')!=-1:
                    unigrams+=[' ']
                    #print ' '
                else :
                    unigrams+=[bigram[1]]
                    #print bigram[1]
        return unigrams


        
    def __init__(self,
                 model_path='models/tag_scheme=iob,lower=False,zeros=False,char_dim=25,char_lstm_dim=25,char_bidirect=True,word_dim=50,word_lstm_dim=100,word_bidirect=True,pre_emb=bi_emgedding_50.out,all_emb=False,cap_dim=0,crf=True,dropout=0.5,lr_method=adam-lr_.0002/'):
        self.model = Model(model_path=model_path)
        model = self.model
        self.parameters = model.parameters
        
        self.word_to_id,self.char_to_id,self.tag_to_id = [
            {v: k for k, v in x.items()}
            for x in [model.id_to_word, model.id_to_char, model.id_to_tag]
        ]
        self.id_to_tag = model.id_to_tag
        _, self.f_eval = model.build(training=False, **self.parameters)
        model.reload()

    def predicts(self,line):   
        if line:
            # Save original bigrams 
            bigram_sent = self.to_bigram(line,0).strip().split()
            
            # Replave all digits with zeros
            line = zero_digits(line)
            input_seq = self.to_bigram(line,0).strip().split()
            
            # Prepare input
            sentence = prepare_sentence(input_seq, self.word_to_id, self.char_to_id,
                                        lower=self.parameters['lower'])
            input = create_input(sentence, self.parameters, False) 
            if self.parameters['crf']:
                y_preds = np.array(self.f_eval(*input))[1:-1]
            else:
                y_preds = self.f_eval(*input).argmax(axis=1)
            tags = [self.id_to_tag[y_pred] for y_pred in y_preds]

            # Output tags in the IOB2 format
            if self.parameters['tag_scheme'] == 'iobes':
                tags = iobes_iob(tags)
            print(tags) 
            # Make output form
            out_form = ""
            unigram_sent = self.bigrams_to_unigrams(bigram_sent)
            
            for i in range(len(tags)): 
                if tags[i].startswith('B'):
                    out_form += '<'+unigram_sent[i]
                elif tags[i].startswith('I'):
                    if i == len(tags)-1:
                        out_form += unigram_sent[i]+':'+tags[i][2:]+'>'
                    elif tags[i+1] == 'O':
                        out_form += unigram_sent[i]+':'+tags[i][2:]+'>'
                    else:
                        out_form += unigram_sent[i]
                else:
                    out_form += unigram_sent[i]
            return out_form
