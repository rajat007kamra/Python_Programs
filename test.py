#Given a String ,iteratively consecutive duplicate chracters of even countfrom the string,strating from the front .
#The output should not have any consecutive duplicate chracters  of even count.

val= input()
mylist={}
list=[]
for i in val:
    if((val.count(i))%2!=0):
        mylist[i]=val.count(i)

for i in mylist.keys():
    list.append(i*mylist[i])
#converting list into string
print(''.join(list))
