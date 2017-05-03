dict_file = open("dic","r")
dict = dict_file.read().splitlines()

ltc_file = open("LTC","r")
ltc_file.readline()

weka_file = open("doc_classify.arff","w")

weka_file.write("@relation doc_classify\n")

for word in dict :
    word_quote_list = word.split('\'')
    if len(word_quote_list) >1 :
        word = '\\\''.join(word_quote_list)
        print(word)
    weka_file.write("@attribute \'"+word+"\' numeric\n")
weka_file.write("@attribute \'Class\' {\'sci.space\',\'sci.electronics\'}\n")
weka_file.write("@data")

for line in ltc_file.readlines() :
    line_list = line.split(',')
    line_list[len(line_list)-1] = line_list[0].split()[0]
    line_list[0] = line_list[0].split()[1]

    line_str = ','.join(line_list)
    weka_file.write(line_str+"\n")

weka_file.close()
ltc_file.close()
dict_file.close()
