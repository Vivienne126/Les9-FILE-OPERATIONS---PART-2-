with open("new.txt") as f:
    data1=f.read()

with open("newfile.txt") as f2:
    data2=f2.read()

data1=data1+"\n"
data1=data1+data2

with open("merged_file.txt" , "w") as fp:
    fp.write(data1)