#URL VALIDATION
import re
file = open("reday7.txt","r")
data= file.read()
pattern=re.compile(r"(https|http|ftp)[://]+[a-z.]+")
res=re.finditer(pattern,data)
for row in res:
    print(row)

#phone number validation
import re 
file=open("reday7.txt","r")
data=file.read()
pattern=re.compile(r"(6|7|8|9){1}[\d]{4}[ *.-][\d]{5}")
res=re.finditer(pattern,data)
for i in res:
    print(i)

#gmail validation

import re
file=open("reday7.txt","r")
data=file.read()
pattern=re.compile(r"[\w\d]+[@][a-z.]+")
pattern1=re.compile(r"[\w\d]{10}[@][a-z.]+")
res=re.finditer(pattern,data)
res1=re.finditer(pattern1,data)
for i in res:
    print(i)
for i in res1:
    print(i)

#password validation

import re 
file=open("reday7.txt","r")
data=file.read()
pattern=re.compile(r"([A-Z]+)([a-z]+)([\d]+)([#@$!]+)")
res=re.finditer(pattern,data)
for i in res:
    print(i)

# name validation
import re
file =open("reday7.txt","r")
data=file.read()
pattern=re.compile(r"(Mrs|Mr|Ms)[.\s]*[A-Z]{1}[\w]+")
res=re.finditer(pattern,data)
for i in res:
    print(i)