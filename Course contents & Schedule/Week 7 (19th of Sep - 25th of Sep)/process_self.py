"""
A short demonstration of reading and processing files in Python.
"""


# Open this file read only  
myfile = open("process_self.py", "r")

  
# Print lines and number only those with code   
line_num = 1
for line in myfile: 
    if line.strip() == "":
        print(line)
    elif line.strip()[0] == "#":
        print(line)
    else:
        print(line_num, ":", line)
        line_num += 1 

  
myfile.close()