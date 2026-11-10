x=56789087654323456789876543222234567897654354
y=34
z=0
swap=True

lists=[6,2,9,7,0,5,3,1,4,8,10]
n=len(lists)
i=0


while swap==True and i<n-1:
    swap=False
    print("itration")
    for j in range (0,n-1-i):
        
        if lists[j]<lists[j+1]:
            z=lists[j]
            lists[j]=lists[j+1]
            lists[j+1]=z
            swap=True
            
        print(lists)
        
    if swap==False:
        break

    i=i+1
print(lists)

print(x,y)
x,y=y,x

print(x,y)