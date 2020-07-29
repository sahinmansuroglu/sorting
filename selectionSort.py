print("selectiion Sort Algorithm")
arrayList=[23,66,45,34,89,76,34,65,76,45,76,45,34,76,67]
print(len(arrayList))
for i in range(0,len(arrayList)-1):
    for j in range(i+1,len(arrayList)):
   
        if arrayList[i] < arrayList[j]:
            temp=arrayList[i]
            arrayList[i]=arrayList[j]
            arrayList[j]=temp
            
            #arrayList[i],arrayList[i+1]=arrayList[i+1],arrayList[i]

print(arrayList)




