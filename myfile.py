file = open("myfile.py","r")
count=0
for line in file:
    words = line.split(" ")
    count =+ len(words)
file.close()
print("I love my Parents : ", count)