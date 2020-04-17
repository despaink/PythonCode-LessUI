# Using readlines() 
file1 = open('errorLog67.txt', 'rb') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines: 
    print(line)