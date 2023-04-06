# random password generator using python

import random
import array
max_len=10
digit=['0','1','2','3','4','5','6','7','8','9']
low_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upp_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sym=['@','#','$','%','&','*',':',';','?','€','!','+','-','/','~']
password = digit + low_case +upp_case + sym
rand_digit = random.choice(digit)
rand_lowcase = random.choice(low_case)
rand_uppcase = random.choice(upp_case)
rand_sym = random.choice(sym)

temp_pass= rand_digit + rand_lowcase + rand_uppcase + rand_sym 

for x in range(max_len):
    temp_pass=temp_pass + random.choice(password)
    temp_pass_list=array.array('u',temp_pass)
    random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
	password = password + x

print(password)
