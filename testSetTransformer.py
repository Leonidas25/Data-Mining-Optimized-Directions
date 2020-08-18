appendText='_'
original=open("test_set_a2.csv",'r')
new=open("test_set_a2_t.csv",'a')
for line in original:
    new.write('\"' + line.rstrip() + '\"' + '\n')
new.close()