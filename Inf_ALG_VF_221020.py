# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:53:21 2022

@author: fisch
"""

    
from pyfiglet import Figlet
import time
import re




while True:
    
    f = Figlet(font='slant')
    print (f.renderText('Subtrahierer 3000'))
    print("-------------------------------------------------------------------")
    print("Author = Vincent Fischer; Nicolas Heine")
    print("")

    print("Hello and welcome to our little project!") 
    print("1 = dec")
    print("2 = bin")
    print("3 = hex")
    ip = input("Please select the type of number system you want to subtract in: ")
    

    
    def dec():
        
          
        def dec_to_bin(r):
            return int(bin(r)[2:])


        while True: 
            i1 = input("Please enter your first number: ")
            i2 = input("And now your second number: ")
            
           
            if i1.isdigit() and i2.isdigit():
                pass
               
            
            else:
                print("")
                print("Sorry, we can't continue because your input contained something that is not a number.")
                time.sleep(2)
                answer = input("Do you wanna try again? /y/n/: ")
                if answer == "y":
                    continue
                elif answer == "n":
                    break
                else:
                        print("You have just made another wrong entry...")
                        print("No more ""Do you wanna try again? ""for you!")
                        break
          
                    
            n1 = int(i1)
            n2 = int(i2)
            
            r = n1-n2
            print("")
            print("The Result in dec is: ", r)
            if i1 < i2:
                pass
            else:
                print("The Result in bin is: ", dec_to_bin(r))
                print("The Result in hex is: " '{0:x}'.format(r))
                
              
            print("-------------------------------------------------------------------")
            break
            
            
        
    
    def bins():
        
        def dec_to_bin(r):
            return int(bin(r)[2:])

        while True: 
            i1 = input("Please enter your first number: ")
            i2 = input("And now your second number: ")
            
            
            
            all_binary = all(c in '01' for c in i1)
            all_binary2 = all(c in '01' for c in i2)
        
            
            if all_binary and all_binary2:
                pass
          
            else:
                print("")
                print("Sorry, we can't continue because your input contained something that is not a number.")
                time.sleep(2)
                answer = input("Do you wanna try again? /y/n/: ")
                if answer == "y":
                    continue
                elif answer == "n":
                    break
                else:
                    print("You have just made another wrong entry...")
                    print("No more ""Do you wanna try again? ""for you!")
                    break
                
            if i1 < i2:
                print("Your second number can't be bigger than your first one!")
                continue
            else:
                pass
                    
            n1 = int(i1, 2)
            n2 = int(i2, 2)
            r = n1-n2
            
            print("")
            print("The Result in bin is: ", dec_to_bin(r))
            print("The Result in dec is: ", r)
            if i1 < i2:
                pass
            else:
                print("The Result in hex is: " '{0:x}'.format(r))
            print("-------------------------------------------------------------------")
            
            break
            
            
        
        
        
    def hexs():
        while True:


            def dec_to_bin(r):
                return int(bin(r)[2:])

            i1 = input("Please enter your first number: ")
            i2 = input("And now your second number: ")
            
            text = i1
            text2 = i2
            
            result = re.sub("[A-F0-9]", '', text)
            result2 = re.sub("[A-F0-9]", '', text2)
            
            if len(result) and len(result2) == 0:
                pass
          
            else:
                print("")
                print("Remember that you can only use digits from A-F and 1-9")
                time.sleep(2)
                answer = input("Do you wanna try again? /y/n/: ")
                if answer == "y":
                    continue
                elif answer == "n":
                    break
                else:
                    print("You have just made another wrong entry...")
                    print("No more ""Do you wanna try again? ""for you!")
                    break
                
            
            
            dec1 = int(i1, 16)
            dec2 = int(i2, 16)
            
            

            
            r = dec1-dec2
            
            
            print("")
            print("The Result in hex is: " '{0:x}'.format(r))
            print("The Result in dec is: ", r)
            print("The Result in bin is: ", dec_to_bin(r))
            print("-------------------------------------------------------------------")
            break


    if  ip == "1":
        dec()
        print("Home = 1")
        print("Quit = 2")
        answer = input("What would you like to do now? : ")
        if answer == "1":
            continue
        else:
            break

    elif ip == "2":
        bins()
        print("Home = 1")
        print("Quit = 2")
        answer = input("What would you like to do now? : ")
        if answer == "1":
            continue
        else:
            break
    
    elif ip == "3":
        hexs()
        print("Home = 1")
        print("Quit = 2")
        answer = input("What would you like to do now? : ")
        if answer == "1":
            continue
        else:
            break

    else:
        print("")
        print("")
        print("Sorry this entry is not valid.")
        print("You will be returned to the menu in 3 sec.")
        print("")
        print("")
        time.sleep(3)
        pass
    
    

    
    




    
    