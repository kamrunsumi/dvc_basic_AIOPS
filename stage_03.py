with open("artifacts01.txt", "r") as f:
   text= f.read()

print(text)

with open("artifacts02.txt", "w") as f:
   text= f.write(text + "added lines")

print('End of stage_03')