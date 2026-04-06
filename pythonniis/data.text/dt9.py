#write a list in a file using text file concept
f=open("sita.text","r+")
print(f.read())
f.write("ok")
f.close()