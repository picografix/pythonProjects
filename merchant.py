from operator import itemgetter
numberMerchant= int(input())

d= []
g= []
s =[]
name=[]
for i in range(numberMerchant):
        data = input().split(",")
        name.append(data[0])
        d.append(data[1])
        g.append(data[2])
        s.append(data[3])
name_sorted = []
for i in range(numberMerchant):
    name_sorted.append([int(d[i]),int(g[i]),int(s[i]),name[i]])
name_sorted = sorted(name_sorted,key= itemgetter(3))
name_sorted = sorted(name_sorted,key= itemgetter(0,1,2),reverse=True)
print("+","-"*25,"+","-"*4 ,"+","-"*4 ,"+","-"*4,"+",sep="") 
print("| {name:<23} | {d:>2} | {g:>2} | {s:>2} |".format(name="Merchant",d="D",g="G",s="S"))
print("+","-"*25,"+","-"*4 ,"+","-"*4 ,"+","-"*4,"+",sep="")
for i in range(numberMerchant):
    print("| {name:<23} | {d:>2} | {g:>2} | {s:>2} |".format(name = name_sorted[i][3],d=name_sorted[i][0],g=name_sorted[i][1],s=name_sorted[i][2]))
print("+","-"*25,"+","-"*4 ,"+","-"*4 ,"+","-"*4,"+",sep="")