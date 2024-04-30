
f = open("main_5_index_list.txt", 'r')
lines = f.readlines()
list = []
for line in lines:
    line = line.rstrip('\n')
    if line.find('#', 0, 1)!=0 and line!='':
        list.append(line)
    

print(list)
f.close()

    
