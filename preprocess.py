import json
import os
import numpy as np
import operator

stop_word =  ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours	ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]
symbols = ["!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/","\\",">","<",">>","<<","... ",":",";","{","}","[","]","\"\"","''","==","--","?","`","-","``",".",":","|","..."]

N = len(os.listdir("sci.space.lemma.json")) + len(os.listdir("sci.electronics.json"))
corpus ={}
words = {}
for filename in os.listdir("sci.space.json"):
    with open("sci.space.json/"+filename,encoding="utf8") as data_file:
        word_temp = {}
        corpus_temp = {}
        data = json.load(data_file)
        token = data["sentences"][0]["tokens"]
        words_stop_word_removed = [x for x in token if x["word"] not in stop_word]
        words_stop_word_and_sysmbol_removed = [x for x in words_stop_word_removed if x["word"] not in symbols]
        for word in words_stop_word_and_sysmbol_removed:
            word_temp[word['word']] = 1
            if word['word'] in corpus_temp:
                corpus_temp[word['word']] +=1
            else:
                corpus_temp[word['word']] =1
        for key, value in word_temp.items():
            if key in words:
                words[key]+=1
            else:
                words[key]=1
        corpus['space:'+filename]=corpus_temp
for filename in os.listdir("sci.electronics.json"):
    with open("sci.electronics.json/"+filename) as data_file:
        word_temp = {}
        corpus_temp = {}
        data = json.load(data_file)
        token = data["sentences"][0]["tokens"]
        words_stop_word_removed = [x for x in token if x["word"] not in stop_word]
        words_stop_word_and_sysmbol_removed = [x for x in words_stop_word_removed if x["word"] not in symbols]
        for word in words_stop_word_and_sysmbol_removed:
            word_temp[word['word']] = 1
            if word['word'] in corpus_temp:
                corpus_temp[word['word']] +=1
            else:
                corpus_temp[word['word']] =1
        for key, value in word_temp.items():
            if key in words:
                words[key]+=1
            else:
                words[key]=1
        corpus['electronics:'+filename]=corpus_temp

######################################################
##                   calculate IDF                  ##
######################################################
IDF = {}
for key, value in words.items():
    IDF[key]=np.log(N/value)
print(len(IDF))

LTC = {}
######################################################
#                   calculate LTC                  ##
#####################################################
print(corpus    )
for key, values in corpus.items():
    base = 0
    temp =[]
    for word, count in values.items():
        base += np.power(np.log(count+1)*np.log(N/values[word]),2)
    # for word, count in values.items():
    #     temp.append(np.log(count+1)*IDF[word]/np.sqrt(base))
    for key_in, values_in in words.items():
        if key_in in values.keys():
            temp.append(np.log(values[key_in]+1)*IDF[key_in]/np.sqrt(base))
        else:
            temp.append(0);

    LTC[key] = temp
print(LTC)

######################################################
##                   print to file                  ##
######################################################
f = open('dic-lemma', 'w')
for key, value in words.items():
    f.write(key+"\n")
f.close()

f = open('LTC-lemma', 'w')
f.write("key | value\n")
for key, values in LTC.items():
    f.write(key+" ")
    for value in values:
        f.write(str(value)+",")
    f.write("\n")
f.close()


# for filename in os.listdir("sci.electronics.json"):
#     with open("sci.electronics.json/"+filename) as data_file:
#         data = json.load(data_file)
#         token = data["sentences"][0]["tokens"]
#         words_stop_word_removed = [x for x in token if x["word"] not in stop_word]
#         words_stop_word_and_sysmbol_removed = [x for x in words_stop_word_removed if x["word"] not in symbols]
#         # print k
#         # for i in xrange(len(token)):
#         #     if token[i]["word"] in s:
#         #         token.pop(i)
#         for word in words_stop_word_and_sysmbol_removed:
#             if word["word"].lower() not in dic_N:

# # print(dic);
# sorted_dic = sorted(dic_N.items(), key=operator.itemgetter(1))
# # print(sorted_dic)
#
# # A list of the keys of dictionary
# list_keys = [ k[0] for k in sorted_dic ]
# list_values = [ k[1] for k in sorted_dic ]
# print(list_values)
# list_n = []
# # print(dic_n[0])
# for doc in dic_n:
#     n = []
#     for key in list_keys:
#         if key in doc:
#             n.append(doc[key])
#         else:
#             n.append(0)
#     list_n.append(n);
#
# # print(list_n)
# f = open('data_n', 'w')
# for n in list_n:
#     for c in n:
#         f.write(str(c)+",")
#     f.write("\n")
# f.close()
# IDF = np.log(N/np.array(list_values))
# print(IDF)
# print(dic_n)
# a = [];
# for n in dic_n:
#
#     a_temp =[];
#     base = 0;
#     for key, value in n.items():
#         base +=np.power(np.log(value+1)*IDF,2)
#     for key, value in n.items():
#         a_temp.append(np.log(value+1)*IDF/np.sqrt(base))
#
#     a.append(a_temp)
# print(a)
#

# # or a list of the values
# # list_values = [ v for v in sorted_dic.values() ]
#
# # # A list of the keys of dictionary
# # list_keys = [ k for k in dict ]
# #
# # # or a list of the values
# # list_values = [ v for v in dict.values() ]
# #
# # # or just a list of the list of key value pairs
# # list_key_value = [ [k,v] for k, v in dict.items() ]
