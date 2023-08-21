# print("**********************KAUN BANEGA COREPATI**************************")
# print("Your Question is: \nWhat is color of APPLE ")
# print("The option is: \n1.Red\n2.Blue\n3.Green\n4.Yellow")
# user= int(input("chose the option in between four: "))
# correct_anser=[1]
# if user==correct_anser:
#     print("your answer is right")
# else:
#     print("your is wrong ")   
questions =[["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4],["what is a color of apple?","red","black","yellow","blue",4]]
level =[1,20,2000,200000,20000000,20000000000,20000000000,20000000000000]
money=0
for i in range(0,len(level)):
    question=questions[i]
    print(f"question for{level[i]}")
    print(f"{question[i]}")
    print(f"1.{question[1]}        2.{question[2]}")
    print(f"2.{question[3]}        4.{question[4]}")
    user=int(input("enter the correct option: "))
    if user==question[-1]:
        print("correct answer you win",level[i])
        if i==2:
            money+=2000
        elif i ==3:
            money+=200000
    else:
        print("wrong answer") 
        break           
print("you have",money)
