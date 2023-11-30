print('welcome to the tip calculator')
bill= float(input("TOTAL BILL: RS "))
tip=int(input('how much tip would like to donate for charity?'))
people=int(input('how many people to split the bill?'))
new_bill= tip+bill
bill_person= new_bill/people
print('each person should pay',round(bill_person,2),'RS each.') 