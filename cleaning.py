import re

# filename = 'adult.data'
# fileopen = open("adultdata.csv","w+")
filename = 'adult.test'
fileopen = open("adulttest.csv","w+")

files = open(filename).read()
files = files.split("\n")
print(type(files))
# index = []
for i in range (0,len(files)):
    m = re.search(r"[\?]",files[i])
#     if m is not None:
#         index.append(i)
      if m is None:
          fileopen.writelines(files[i])
          fileopen.writelines("\n")

# for i in range (0,len(files)):
#     if i not in index:
#         fileopen.writelines(files[i])
#         fileopen.writelines("\n")

fileopen.close()
