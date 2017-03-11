import random
import os
import time

class Enemy():
    life = 3
    damage = 5
    name = ['goblin']
class Hero():
    coin = 150
    weaponLvl = 1
    weapon_name = "Bow Staff"
    armorLvl = 0
    armor_name = "none"
    potions = 0
    life = 15
    life_Max = 15
    def __init__ (self):
        self.name=input("what is the name of your hero? ")
#intilize
hero1=Hero()

#random script to build the question database
Q = []
A = []
qQnA = []
print('building database...')
for line in open('data.txt'):
     qQnA =(line.split('~'))
     Q.append(qQnA[0])
     A.append(qQnA[1].strip('\n'))
print('database structuring complete')


#fight sequence
def fight():
    basicEnemy=Enemy()
    print("HP: ",("*" * basicEnemy.life))
    print("Enemy Name",basicEnemy.name)
    print(" \n \n \n \n \n \n ")
     
    while basicEnemy.life >= 1: 
      PIN = random.randrange(0,len(Q))
      Question = Q[PIN]
      Answer = A[PIN]
      print(Question)
      choice = input().lower()
      if choice == Answer: 
          os.system('clear')
          print("good gob!")
          print(" youre strike was successful! ")

  
          time.sleep(2)
          basicEnemy.life -= hero1.weaponLvl
          
          os.system('clear')
      elif choice == "potion":
          if hero1.potions > 0:
           hero1.life += 5
           hero1.potions -= 1
           os.system('clear')
           if hero1.life > hero1.life_Max:
              hero1.life = hero1.life_Max
          else:
           os.system('clear')
           print("you dont have any potions!! \n the enemy attacked you as you stood dumbfounded")
           hero1.life -= (basicEnemy.damage - hero1.armorLvl)
           time.sleep(3)
           os.system('clear')
      else:
          os.system('clear')
          print("missed, he countered!")
          print("he took ",(basicEnemy.damage - hero1.armorLvl),"health from you!!")

          time.sleep(2)
          hero1.life -= (basicEnemy.damage - hero1.armorLvl) 
          os.system('clear')    
      if basicEnemy.life <= 0:
          os.system('clear')
          coinsWon = random.randrange(0,10)
          hero1.coin += coinsWon
          print("you won ",coinsWon," coins!")

          print("(game will continue in 5 seconds)")
          time.sleep(5)
          break
      elif hero1.life <= 0:
          os.system('clear')
          print("you died!")
          time.sleep(5)
          break
      print("Enemy HP")
      print("HP: ",( "*" * basicEnemy.life))
      print("XX LIFE:",hero1.life,"ARMOR:",hero1.armor_name,"(",hero1.armorLvl,")","WEAPON",hero1.weaponLvl)


# Check current Stats
def check_gear():
    os.system('clear')
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("XX LIFE:",hero1.life,"ARMOR:",hero1.armor_name,"(",hero1.armorLvl,")","WEAPON",hero1.weaponLvl)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    print(' Name: ',hero1.name, '\n Life: ',hero1.life,'\n Coins: ',hero1.coin,'\n Armor ',hero1.armor_name,'\n Armor LVL',hero1.armorLvl,'\n Weapon ',hero1.weapon_name, '\n Weapon LVL', hero1.weaponLvl,' \n Potions: ',hero1.potions)
    time.sleep(5)


#runs through marketplace, to sell, buy and recover
def marketPlace():
    os.system('clear')

         
    choice = 0
    while choice is not "3":
        print("hello", hero1.name, " you have ", hero1.coin, " coins")
        print("what would you like to do? \n 1.)buy gear \n 2.)rest at inn \n 3.)Leave the Market")
        choice = input()
        if choice is "1":
            Buy_gear()
        elif choice is "2":
            rest_Inn()
        elif choice is "3":
            print("farewell")
        else:
            print("i dont understand your choice")
        os.system('clear')

# rest at inn

def rest_Inn():
    os.system('clear')
    print("you get a good nights rest and your health is restored")
    hero1.life = hero1.life_Max
    time.sleep(3)
    os.system('clear')


#runs through letting user buy his armor, if statement with tiered options avaiable based on coins
def buy_gear_ARMOR():
    os.system('clear')
   
    choice = 0
    while choice is not "4":
        print(' 1.)Leather Armor(100 Coins) \n 2.)Iron Armor(500 coins)  \n 3.)DragonSkin Armor(5000 coins)')
        choice = input()
        if choice is "1":
            if hero1.coin >= 100:
                hero1.coin -= 100
                hero1.armor_name = "Leather Armor"
                hero1.armorLvl = 1
                print('you have aquired leather armor! ArmorLVL = 1')
            else:
                print('you possess insufficent funds')
        elif choice is "2":
            if hero1.coin >= 500:
                hero1.coin -= 500
                hero1.armor_name = "Iron Armor"
                hero1.armorLvl = 2
                print('you have aquired Iron armor! ArmorLVL = 2')
            else:
                print('you possess insufficent funds')        
        elif choice is "3":
            if hero1.coin >= 5000:
                hero1.coin -= 5000
                hero1. armor_name = "DragonSkin Armor"
                hero1.armorLvl = 3
                print('you have aquired DragonSKin Armor! ArmorLVL = 3')
            else:
                print('you possess insufficent funds')
        elif choice is "4":
            print("good bye")
        else:
            print("error")

        time.sleep(2)
        os.system('clear')

def buy_gear_WEAPONS():
    os.system('clear')
   
    choice = 0
    while choice is not "4":
        print('1.) Basic Iron Sword (100 Coins) \n 2.) Curved Katana (1000 coins)  \n 3.)Buster Blade(5000 coins)')
        choice = input()
        if choice is "1":
            if hero1.coin >= 100:
                hero1.coin -= 100
                hero1.weapon_name = "Basic Iron Sword"
                hero1.weaponLvl = 2
                print('you have aquired a Basic Iron Sword! Weapon Level 2!' )
            else:
                print('you possess insufficent funds')
        elif choice is "2":
            if hero1.coin >= 1000:
                hero1.coin -= 1000
                hero1.armor_name = "Curved Katana"
                hero1.weaponLvl = 3
                print('you have aquired a Curved Katana! Weapon Level 3!')
            else:
                print('you possess insufficent funds')        
        elif choice is "3":
            if hero1.coin >= 5000:
                hero1.coin -= 5000
                hero1. armor_name = "Buster Blade"
                hero1.weaponLvl = 4
                print('you have aquired a Buster Blade! Weapon Level 4!')
            else:
                print('you possess insufficent funds')
        elif choice is "4":
            print("good bye")
        else:
            print("error")

        time.sleep(2)
        os.system('clear')

def Buy_Potions():
    os.system('clear')

    print(" (1) Potion = 25, how many do you want?")

    while True:
        choice = input()
        actualChoice = int(choice)*25
        if actualChoice <= hero1.coin:
            print("you are going to purchase ",choice ," potions for ",actualChoice ,"are you sure? \n yes or no? ('cancel' to leave)")
            yon = input()
            if yon ==  "yes":
                hero1.potions += int(choice)
                break
            elif yon == "cancel":
                break
            else:
                pass
        else:
            print("insufficent funds")

#Runs user through buying armor, weapons, or selling items. 
def Buy_gear():
    os.system('clear')
   
    choice = 0
    while choice is not "4":
        print(' 1.)Look at Armor \n 2.)Look at Weapon  \n 3.)buy potions \n4.) go back to market')
        choice = input()
        if choice is "1":
             buy_gear_ARMOR()
        elif choice is "2":
             buy_gear_WEAPONS()
        elif choice is "3":
             Buy_Potions() 
        elif choice is "4":
            print("good bye")
        else:
            print("error")
          
        os.system('clear')

 

#runs through main game
def mainScenerio():
    os.system('clear')
    choice = 0
    while choice is not "4":
        print(' 1.)fight \n 2.)Market Place \n 3.)Check Gear \n 4.)logoff(no saves)')
        choice = input()
        if choice is "1":
            os.system('clear')
            fight()
        elif choice is "2":
            marketPlace()
        elif choice is "3":
            check_gear()
        elif choice is "4":
            print("good bye")
        else:
            print("error")

        os.system('clear')


mainScenerio()



