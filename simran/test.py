#f=open("data.txt","r")
#print(f.read())
#f.close()

f=open("data.txt","w")
f.write("ujjwal")
f.close()

f=open("data.txt","r+")
print(f.read())
f.write("regex")
f.close()

