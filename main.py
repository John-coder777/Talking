import json
iwrote = 2
filename = "Messages.txt"
myfile=open("Messages.txt",mode="w",encoding="Latin-1")
Messages = ["Hi!"]
for talk in Messages:
  if not iwrote == 2:
    print(talk)
a = 1
Messages.append(input())
iwrote = 1
for name in Messages:
  json.dump(name,myfile)
 
  
myfile.close()  
myfile = open(filename, mode="r", encoding="Latin-1")
for file in Messages:
  print(file)


  