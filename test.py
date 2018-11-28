val= input()
mylist={}
list=[]
for i in val:
    if((val.count(i))%2!=0):
        mylist[i]=val.count(i)

for i in mylist.keys():
    list.append(i*mylist[i])
print(''.join(list))
