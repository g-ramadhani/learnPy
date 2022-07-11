#I'm Learning Python
#Program Coffee Shop

#Blacklisted Member
blacklist = ["ben", "loki", "lou"]

#Menu
menu = ["Black Coffee","Espresso","Latte","Tea"]
price = [5,10,15,20]

print("=====SG COFFEE=====")
#Asking Name for order
name = input("What Is Your Name ? \n")

#Check if name in blacklist
if name.lower() == blacklist[0] or name.lower() == blacklist[1] or name.lower() == blacklist[2] :
    #check if blacklist is true
    answer=input(name + ", Are you evil ? (Yes/No)\n")
    #check if evil is true, asking good deed
    cekBaik=int(input("How many good deeds have you done today ?\n"))
    if answer.lower() == "yes" and cekBaik < 4 :
            #true condition member blacklisted and member are evil
            print(name + " you're bad evil, you're not welcome here, Get Out!!!")
            exit()
    #False condition member blacklisted and member are not evil
    else :
        print("Oh, so you're one of those good " + name + "s. Come on in")

print("===================")
#Member not in blacklisted
print("\nHello " + name +", welcome to SG Coffee, Here is what we serving:")

#display menu from list
num = 1
for i, j in zip(menu,price) :
    print(str(num)+". "+i+" = "+"$"+str(j))
    num += 1

#Order Menu
order = int(input("\nYour Choice 1-4: "))

if order == 1 :
    pilih = menu[0]
    price = price[0]
elif order == 2  :
     pilih = menu[1]
     price = price[1]
elif order == 3 :
     pilih = menu[2]
     price = price[2]
elif order == 4 :
     pilih = menu[3]
     price = price[3]
else :
    print("Sorry, we don't have that here.")
    price = 0
    quit()

#Total Buying quantity
quantity = input("how many " + pilih +" would you like ?\n")

#Total price must pay
total = price * int(quantity)

print("Sounds Good " + name + " , we'll have your "+ quantity + " " + pilih + " ready for you in a moment, all about " +str(total)+ " dollars\n")

#Bonus Foods and drink
if total < 500 :
   print("Congrats " + name + " you got Bonus one free Snack, thanks for coming today")
   exit()
else :
   print("Congrats " + name + " you got Bonus one free Latte, thanks for coming today")
   exit()
