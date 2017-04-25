import json
import os
import numpy
import operator
stop_word =  ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours	ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]
symbols = ["!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/","\\",">","<",">>","<<","... ",":",";","{","}","[","]","\"\"","''","==","--","?","`","-","``",".",":","|","..."]
dic = {}
dic_n = []
for filename in os.listdir("sci.space.json"):
    with open("sci.space.json/"+filename) as data_file:
        data = json.load(data_file)
        token = data["sentences"][0]["tokens"]
        words_stop_word_removed = [x for x in token if x["word"] not in stop_word]
        words_stop_word_and_sysmbol_removed = [x for x in words_stop_word_removed if x["word"] not in symbols]
        # print k
        # for i in xrange(len(token)):
        #     if token[i]["word"] in s:
        #         token.pop(i)
        dic_temp =dic.fromkeys(dic, 0)
        for word in words_stop_word_and_sysmbol_removed:
            if word["word"].lower() not in dic:
                dic[word["word"].lower()]=1;
                dic_temp[word["word"].lower()]=1;
            else:
                dic[word["word"].lower()]+=1;
                dic[word["word"].lower()]+=1;
        dic_n.append(dic_temp)

# print(dic);
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
# print(sorted_dic)

# A list of the keys of dictionary
list_keys = [ k[0] for k in sorted_dic ]
list_values = [ k[1] for k in sorted_dic ]
print(list_keys)
list_n = []
for doc in dic_n:
    n = []
    for key in list_keys:
        if key in doc:
            n.append(doc[key])
        else:
            n.append(0)
    list_n.append(n);

print(list_n)
# or a list of the values
# list_values = [ v for v in sorted_dic.values() ]

# # A list of the keys of dictionary
# list_keys = [ k for k in dict ]
#
# # or a list of the values
# list_values = [ v for v in dict.values() ]
#
# # or just a list of the list of key value pairs
# list_key_value = [ [k,v] for k, v in dict.items() ]
