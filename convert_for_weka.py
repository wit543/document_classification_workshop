dict_file = open("dic","r")
dict_key = dict_file.read().splitlines()

check_dup = dict()

ltc_file = open("LTC","r")
ltc_file.readline()

weka_file = open("doc_classify.arff","w")

weka_file.write("@relation doc_classify\n")

for word in dict_key :
    word_quote_list = word.split('\'')
    if len(word_quote_list) >1 :
        word = '\\\''.join(word_quote_list)
    word_space_list = word.split(' ')
    if (len(word_space_list) > 1) :
        word = ''.join(word_space_list)
    if word in check_dup :
        print ('hit')
    check_dup[word] = 1
    weka_file.write("@attribute \'"+word+"\' numeric\n")
weka_file.write("@attribute \'Class\' {\'sci.space\',\'sci.electronics\',\'other\'}\n")
weka_file.write("@data\n")

for line in ltc_file.readlines() :
    line_list = line.split(',')
    if line_list[0].split()[0].split(':')[0] == 'space' :
        line_list[len(line_list)-1] = '\'sci.space\''
    elif line_list[0].split()[0].split(':')[0] == 'electronics' :
        line_list[len(line_list)-1] = '\'sci.electronics\''
    else :
        line_list[len(line_list)-1] = '\'other\''
    line_list[0] = line_list[0].split()[1]

    line_str = ','.join(line_list)
    weka_file.write(line_str+"\n")

weka_file.close()
ltc_file.close()
dict_file.close()
