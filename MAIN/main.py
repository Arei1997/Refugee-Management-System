from os.path import exists,dirname,abspath
import json
from importlib.machinery import SourceFileLoader
import sys

DIR = dirname(abspath(__file__))[:-5] #current directory
# needs to be uncommented when refugee file fixed
# refugee_module = SourceFileLoader('refugeefunctions',DIR+R'/REFUGEE/refugeefunctions.py').load_module()


#need a loop, some form of interaction, ability to call in functions from other files, some way to break out of the loop
#print out some key

#inactive volunteer should flag warning message
#should invalid volunteer be allowed to view any information on any camps? Should these functions be locked behind a camp check? Probably yes

#keywords, ie "Add" -> directs to lit of possible things to add
#output a brief key at every stage
#decided on this - no time to implement now, therefore leave till monday
generalkeywords = ("add", "modify", "delete", "view", "view all")

#keysword to submit to console -> associated function names as string
#use getattr for accessing object methods
adminkeywords = ('volunteer','ep','camp')

volunteerkeywords = ('volunteer','refugee')

def login_func(u,p, user):

    with open(DIR + '/users.json','r') as j: data = json.load(j)

    if u == data["admin"]["username"] and p == data['admin']['password']:
        #instantiate user variable as admin
        user.append("admin")
        print("Now logged in as admin!\n")
    else:
        for volunteer in data['volunteers']:
            if u == volunteer['username'] and p == volunteer['password']:
                #instatiate user variable as volunteer
                user.append("volunteer")
                print("Now logged in as volunteer!\n")
                break
        else : 
            #u/p not recognised
            print('username/password combination not recognised!\n')
            return False
    return True
    

def help_func(u): print("admin info"*(u[0] == "admin") or "volunteer info")


def main():
    user = []

    while True:
        username = input("Please enter your username:\n")
        password = input("Please enter your password:\n")
        if login_func(username,password,user): break
        
    print('If at any time you get stuck, simply type "?" to view options')

    while True:

        # first we ask user what component they want to edit
        
        if user[0]=="admin":
            print(', '.join(adminkeywords))
        else:
            print(', '.join(volunteerkeywords))

        generalchoice = input('Enter a listed action: ')

        if generalchoice == "?":
            help_func(user)
            continue

        if user[0]=="admin":

            if generalchoice.lower() not in adminkeywords:
                print("Invalid command!")
                continue

        else:
            if generalchoice.lower() not in volunteerkeywords:
                print("Invalid command!")
                continue

        print(', '.join(generalkeywords))
        userchoice = input('Please enter your next command:\n')

        if userchoice == "?":
            help_func(user)
            continue

        if userchoice.lower() not in generalkeywords:
            print("Invalid command!")
            continue



            #module = SourceFileLoader(f'{generalchoice.lower()}functions',
            #DIR+f'/{generalchoice.upper()}/{generalchoice.lower()}functions.py').load_module()
            
            # work in progress 
            # getattr(module,f'{userchoice}_{generalchoice}') (*)
    
      
            #module = SourceFileLoader(f'{generalchoice.lower()}functions',
            #DIR+f'/{generalchoice.upper()}/{generalchoice.lower()}functions.py').load_module()

            


        #functionality for navigating pages
        #functionality for viewing pages
        #break

        input("Session Ended")
        break


main()