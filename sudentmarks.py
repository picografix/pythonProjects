from operator import itemgetter
name = input().split(",")
marks = input().split(",")
marks = [ float(mark) for mark in marks]
tuples_list = []
for i in range(len(name)):
    tuples_list.append((name[i],marks[i]))
tuples_list = sorted(tuples_list,key=itemgetter(0),)
tuples_list = sorted(tuples_list,key = itemgetter(1),reverse =True)
print(tuples_list)