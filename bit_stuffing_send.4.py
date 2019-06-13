f=open("bitstuffing.txt","w")


b=[1,0,0,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0]
print "before stuffing"
print b

d=[]
count=0
for i in range(len(b)):
    if b[i]==1:
        count=count+1
        d.append(b[i])
    elif b[i]!=1:
        count=0
        d.append(b[i])
    if count==5:
        d.insert(i+1,0)

print "after stuffing"
print (d)

f=open("bitstuffing.txt","w")
f.writelines(str(d))
f.close()

