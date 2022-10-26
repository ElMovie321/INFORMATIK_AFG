# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 01:27:47 2022

@author: fisch
"""


    

import time




while True:

    
    print("   _____       __    __             __    _")                
    print("  / ___/__  __/ /_  / /__________ _/ /_  (_)__  ________  _____")     
    print("  \__ \/ / / / __ \/ __/ ___/ __ `/ __ \/ / _ \/ ___/ _ \/ ___/")     
    print(" ___/ / /_/ / /_/ / /_/ /  / /_/ / / / / /  __/ /  /  __/ /")    
    print("/____/\__,_/_.___/\__/_/   \__,_/_/ /_/_/\___/_/   \___/_/")   
    print("   _____ ____  ____  ____" ) 
    print("  |__  // __ \/ __ \/ __ \ ")
    print("   /_ </ / / / / / / / / /")
    print(" ___/ / /_/ / /_/ / /_/ / ")
    print("/____/\____/\____/\____/  ")

                          
    print("-------------------------------------------------------------------")
    print("Author = Vincent Fischer; Nicolas Heine")
    print("Edit: Der Code ist eventuell sehr unübersichtlich:) ")
    print("")
    print("Hello and welcome to our little project!")
    print("")
    print("\033[1;36;m 1 = dec \033[0;0m")
    print("\033[1;35;m 2 = bin \033[0;0m")
    print("\033[1;32;m 3 = hex \033[0;0m")
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
            print("\033[1;36;m The Result in dec is: \033[0;0m", r)
            if n1 < n2:
                pass
            else:
                print("\033[1;36;m The Result in bin is: \033[0;0m", dec_to_bin(r))
                print("\033[1;36;m The Result in hex is: \033[0;0m" '{0:x}'.format(r))
                
              
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
                print("Sorry, we can't continue because your input contained something that is not 0 or 1.")
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
            
            print("\033[1;35;m The Result in bin is: \033[0;0m", dec_to_bin(r))
            print("\033[1;35;m The Result in dec is: \033[0;0m", r)
            if i1 < i2:
                pass
            else:
                print("\033[1;35;m The Result in hex is:  \033[0;0m" '{0:x}'.format(r))
            print("-------------------------------------------------------------------")
            
            break
            
            
        
    def hexs():
        while True:


            def dec_to_bin(r):
                return int(bin(r)[2:])

            i1 = input("Please enter your first number: ")
            i2 = input("And now your second number: ")
            
            all_hex = all(c in '0123456789ABCDEF' for c in i1)
            all_hex2 = all(c in '0123456789ABCDEF' for c in i2)
            
            
            if all_hex and all_hex2:
                dec1 = int(i1, 16)
                dec2 = int(i2, 16)
            
                r = dec1-dec2
                
                print("")
                print("\033[1;32;m The Result in hex is: \033[0;0m" '{0:x}'.format(r))
                print("\033[1;32;m The Result in dec is: \033[0;0m", r)
                print("\033[1;32;m The Result in bin is: \033[0;0m", dec_to_bin(r))
                print("-------------------------------------------------------------------")
                break

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
                
            
            if i1 < i2:
                print("")
                print("Your second number can't be higher than your first!")
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
                

    if  ip == "1":
        dec()
        print("Home = 1")
        print("Quit = Any other key")
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
        print("Quit = Any other key")
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
    