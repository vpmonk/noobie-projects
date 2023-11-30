hero = input("ENTER NAME OF THE HERO: ")
heroine = input("ENTER NAME OF THE HEROINE: ")
new = hero+heroine
new_i= new.lower()

t = new_i.count("t")
r = new_i.count("r")
u = new_i.count("u")
e = new_i.count("e")
first = t+r+u+e

l = new_i.count("l")
o = new_i.count("o")
v = new_i.count("v")
e = new_i.count("e")
second = l+o+v+e

score = int(str(first)+str(second))
if score >=90:
    print ("YOU ARE AN EXCEPTIONAL PATNER"+ f"SCORE IS {score}")
           
elif 90 > score >35:
        print("YOUR PAIR IS LIKE COKE-MENTOS AND GET READY FOR ROLLER COSTER"+f" SCORE IS {score}")
else:
    print("better BREAKUP THIS WONT LAST AND"+f" SCORE IS {score}")         
