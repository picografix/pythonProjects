def li_to_num(a):
    a_rev = a[::-1]
    ans = 0
    for i in range(len(a)):
        ans += a_rev[i]*(10**i)
    return ans
def sumup(i,a,b):
    sumo = 0
    for j in range(a,b):
        sumo += i[j]
    return sumo 
def convert(a):
    n = []
    p=0
    for i in range(len(a)):
        if a[i]==1 and  i !=len(a)-1:
            p+=1
        elif a[i]==1 and i ==len(a)-1:
            p+=1
            n.append(p)
        elif a[i]==0:
            if p!=0:
                n.append(p)
            n.append(0)
            p = 0
        
    return n        
dicty = {}
for i in range (97,123):
    dicty[chr(i)] = i-96
word = input()
"""op = 0
for i in wor:
    if i==" ":
        op = wor.index(i)
        break
word= wor[:op]"""
li = []
for i in word:
    if i!= " ":
        li.append(dicty[i])
#print(li)
remli=[]
quoli=[]
remnum=0
quonum=0

for i in range(len(li)):
    remli.append((li[i] % 9))
    quoli.append((li[i]//9))
remli_rev  = remli[::-1]
quoli_rev = quoli[::-1]
for i in range(len(remli)):
    remnum += remli_rev[i]*(10**i)
    quonum += quoli_rev[i]*(10**i)
bin_rem = bin(remnum)
bin_quo = bin(quonum)
bin_quo = bin_quo[2:]
bin_rem = bin_rem[2:]
bin_rem = [int(i) for i in bin_rem]
bin_quo = [int(i) for i in bin_quo]
conv_rem =  convert(bin_rem)
conv_quo = convert(bin_quo)
print((li_to_num(conv_rem),li_to_num(conv_quo)))