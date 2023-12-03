import random
alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num=['0','1','2','3','4','5','6','7','8','9']
symb=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
password=""
print("Welcome to monk password generator")

nr_alp=int(input("how many alphabets you want buddy??: "))
for char in range(1,nr_alp+1):
    password+=random.choice(alp)
nr_num=int(input("how many number you want buddy??: ")) 
for char in range(1,nr_num+1):
    password+=random.choice(num)
nr_sym=int(input("how many symbols you want buddy??: "))    
for char in range(1,nr_sym+1):
    password+=random.choice(symb)


pass_list=list(password)
random.shuffle(pass_list)
npas = "".join(pass_list)

print(f"THE PASSWORD IS : {npas}")