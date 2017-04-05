###############################################################################
# This is a small script created to check if there are old
# links directing the visitor to the old AnyBody wiki page.

### Author: Ioan-Matei Sarivan @ Anybody Technology A/S
### ms@anybodytech.com

############################www.anybodytech.com################################



import os
print('#########################')
for file in os.listdir():
    if '.md' in file:
        #print(file)
        with open(file, encoding="UTF-8") as f:
            lines = f.readlines()
        #file.close()
        for line in lines:
            try:
                if 'anyscript.org' in line:
                    print(file)
                    print(line)
            except:
                print('fail')
                print(file)
