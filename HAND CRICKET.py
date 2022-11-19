import random as rd
print("...HELLO & WELCOME TO HAND CRICKET GAME .......")
rnd = rd.randrange(1,3)
user_choice = int (input("enter your choice Between  1 & 2  for a TOSS ..... 1 is for ODD & 2 is for EVEN\n: " ))
if user_choice == 1 :
    print("YOUR, choice is ODD,  and COMPUTER'S choice is even\n")
elif user_choice == 2 :
    print("YOUR choice is EVEN,  and COMPUTER'S choice is ODD\n")
else:
    print("invalid input\n")
    quit()
while (True):
    computer = rd.randrange(1,7)
    user_num = int (input("enter your choice from 1 - 6 \n:  "))
    if user_num <=6:    
        results = user_num + computer
        a = results%2
        if user_choice== 2  and a==0 or user_choice== 1 and a!=0 :
            print("........YOU WON THE TOSS...... THE RESULT OF TOSS IS",results)
            y = str(input("DO YOU WANT TO BAT OR YOU WANT TO FIELD?......IF YOU WANT TO BAT PRESS 'B'  AND IF YOU WANT TO FIELD PRESS 'F'...........\n"))
            if y == 'b':
                print("INSTRUCTION  : YOU CHOSE TO BAT FIRST\n")
                i = 0
                computer = rd.randrange(1,7)

                while(True):
                    comp = rd.randrange(1,7)
                    user_no = int(input("number you want for batting :  \n"))
                    
                    score_user = i 
                    if user_no > 6 :
                        print("\nINVALID ENTERIES .....  YOUR NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                    elif comp == user_no:
                        print(".......OUT........\n")
                        e = i
                        h = i +1
                        print("your score is  \n",e)
                        print("\nINTRUCTIONS : YOU GAVE A TARGET OF\n" ,h)
                        i = 0
                        while (i!=h):
                
                            computer = rd.randrange(1,7)
                            user = int(input("number you want for bowling :  \n"))
                    

                            score = i
                    
                            if user > 6 :
                                print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                            elif computer == user:
                                print(".......OUT........\n")
                                print("computer score  is  \n",score)
                                print("!!!...>>>YOU WON<<<...!!!")
                                quit()
                
                
                            elif i >=h:
                                print("!!!...>>>YOU LOSE<<<...!!!")
                                break
                                quit()
                            
                                
                            else:
                                i = i + computer 
                                print("\nRUNS =\n ", i   )
                        break      
    
                    else:
                        i = i + user_no
                        print ("RUNS = ", i)
        
            elif y =='f':
                print("....YOU CHOSE TO FIELD FIRST....")
                i = 0
                computer = rd.randrange(1,7)

                while(True):
                    comp = rd.randrange(1,7)
                    user = int(input("number you want :  \n"))
                    
                    score = i 
                    if user > 6 :
                        print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                    elif comp == user:
                        print(".......OUT........\n")
                        print("computer's score is  \n",score)
                        s = score +1
                        print("..YOU GOT A TARGET OF ...",s)
                        i = 0
                        computer = rd.randrange(1,7)

                        while(True):
                            comp = rd.randrange(1,7)
                            user = int(input("number you want for batting :  \n"))

                            score = i 
                            if user > 6 :
                                print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
         
                            elif comp == user:
                                print(".......OUT........\n")
                                print("your score is  \n",score)
                                print("!!!...>>>YOU LOSE<<<...!!!")
                                quit()
                                
                            elif i>=s:
                                print("!!!...>>>YOU WIN<<<...!!!")
                                quit()
    
                            else:
                                i = i + user
                                print("\nRUNS = ", i ,       "\nCOMPUTER'S NUMBER IS   \n",comp            )
                        
    
                    else:
                        i = i + comp
                        print ("RUNS = ", i)
            else:
                print(".......INVALID ENTRY.....")
                break
        
        
        elif user_choice==1 and a%2==0 or user_choice ==2 and a!=0:
            print(".........COMPUTER WINS THE TOSS......THE RESULT OF THE TOSS IS ",results)
            cp = rd.randrange(1,3)
            if cp == 1 :
                print("INSTRUCTION  : COMPUTER CHOSE TO BAT FIRST\n")
                i = 0
                computer = rd.randrange(1,7)

                while(True):
                    comp = rd.randrange(1,7)
                    user_no = int(input("number you want for bowling :  \n"))
                    
                    score_comp = i 
                    if user_no > 6 :
                        print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                    elif comp == user_no:
                        print(".......OUT........\n")
                        e = i 
                        h = i +1
                        print("computer's score is  \n",e)
                        print("\nINTRUCTIONS : YOU GOT A TARGET OF\n" ,h)
                        i = 0
                        while (i!=h):
                
                            computer  = rd.randrange(1,7)
                            user = int(input("number you want for batting :  \n"))
                    

                            score = i
                    
                            if user > 6 :
                                print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                            elif comp == user:
                                print(".......OUT........\n")
                                print("your score is  \n",score)
                                print("!!!...>>>YOU LOSE<<<...!!!")
                                if score_comp == score:
                                    print(".......IT'S A TIE........")
                                quit()
                            
                
                    
                            elif score >=h:
                                print("!!!...>>>YOU WON<<<...!!!")
                            else:
                                i = i + user  
                                print("\nRUNS = ", i ,       "\nCOMPUTER'S NUMBER IS   \n",comp            )
                        break      
                    
                    else:
                        i = i + comp
                        print ("RUNS = ", i)





            else:
                print("INSTRUCTION : COMPUTER CHOSE TO FIELD FIRST\n")
                i = 0
                comp_fielding = rd.randrange(1,7)

                while(True):
        
                    user_batting = int(input("number you want for batting :  \n"))

                    score = i 
                    if user_batting > 6 :

                        print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                    elif comp_fielding == user_batting:
                        print(".......OUT........\n")
                        print("your score is  \n",score)
                        print("INSTRUCTIONS : YOU HAVE GIVEN A TARGET OF\n",score+1)
                        f = score +1
                        q= 0
                        while(q!=f):
                            comp_batting = rd.randrange(1,7)
                            user_fielding = int(input("number you want for fielding :  \n"))


                            score_comp = q 
                            if user_fielding > 6 :
                                print("\nINVALID ENTERIES .....  YOU NUMBER SHOULD BE BETWEEN  1-6........\n")
        
                            elif comp_batting == user_fielding:

                                print(".......OUT........\n")
                                print("computer's score is  is  \n",score_comp)
                                print("!!!...>>>YOU WON<<<...!!!")
                                quit()
                            elif (q>= f):
                                print("!!!..>>>YOU LOSE<<<...!!!")
                
    
                            else:
                                q = q + comp_batting
                                print("\nRUNS = ", q,       "\nCOMPUTER'S NUMER IS ",comp_batting)

                        break
    
                    else:
                        i = i + user_batting
                        print("\nRUNS = ", i ,       "\nCOMPUTER'S NUMBER IS   \n",comp_fielding)





                        