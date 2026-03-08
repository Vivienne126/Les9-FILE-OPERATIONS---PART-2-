import os

with open("new.txt" , "w") as f:
    f.write("In write mode how are you")



file=open("newfile.txt" ,"w")
file.write("Hello")
#Does a file exist

if os.path.exists("output.txt"):
    print("Yes it exists")
else:
    print("No it doesent exist")
    file=open("newfile2.txt" , "w")


#Delete a file
if os.path.exists("1.txt"):
    os.remove("1.txt")
