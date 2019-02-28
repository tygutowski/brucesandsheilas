#Bruces and Sheilas
#Tyler Gutowski and Jimmy Hubbard
import random
reset=True
while(reset):
    turn=0
    numlist=random.sample(range(10),4)
    num1=str(numlist[0])
    num2=str(numlist[1])
    num3=str(numlist[2])
    num4=str(numlist[3])
    print ("Welcome to Bruces and Sheilas")

    bigboyloop=True
    while(bigboyloop):
        turn+=1

        #Making number
        digitloop=True
        while(digitloop==True):
            print("Please choose a 4 digit integer:")
            ans=input("")
            ans1=ans[0]
            ans2=ans[1]
            ans3=ans[2]
            ans4=ans[3]
            if (ans1==ans2) or (ans1==ans3) or (ans1==ans4) or (ans2==ans3) or (ans2==ans4) or (ans3==ans4):
                print ("Please don't use repeating digits.")
                digitloop=True
            else:
                digitloop=False
                
        bruce=0
        sheila=0

        
        #Count number of Bruces
        if(ans1==num1):
            bruce+=1
        if(ans2==num2):
            bruce+=1
        if(ans3==num3):
            bruce+=1
        if(ans4==num4):
            bruce+=1

        #Count number of sheilas
        if(ans1==num2) or (ans1==num3) or (ans1==num4):
            sheila+=1
        if(ans2==num3) or (ans2==num4) or (ans2==num1):
            sheila+=1
        if(ans3==num2) or (ans3==num4) or (ans3==num1):
            sheila+=1
        if(ans4==num1) or (ans4==num2) or (ans4==num3):
            sheila+=1

        #Ending
        if(bruce<4):
            print("Bruces:",bruce,"     Sheilas:",sheila)
            print("You are on turn",turn)
            print("")
        if(bruce==4):
            print("You win!")
            print("It took you",turn,"turns!")
            print("")
            bigboyloop=False
            ask2=True
            while (ask2):
                repeat=input("Would you like to play again?\n")
                if (repeat=="yes"):
                    reset=True
                    ask2=False
                elif (repeat=="no"):
                    reset=False
                    ask2=False
                else:
                    print("Please either enter yes or no.\n")
                    ask2=True

