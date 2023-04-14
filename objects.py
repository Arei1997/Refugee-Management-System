import sys
import EP.epfunctions as empl
import CAMP.campfunctions as camp
import REFUGEE.refugeefunctions as refu
import USER.userfunctions as usfu
import EXCEPTIONS.customExceptions as exceptions
# import MAIN.main as main1


class Volunteer:

    def __init__(self, username, isActive, camp):
        self.username = username
        self.isActive = isActive
        self.userType = type(self)
        self.camp = camp*isActive  # maybe a bit hacky -- idk

    def register_refugee(self):
        # get a bunch of inputs and pass the form into the function
        # Maybe interact with a GUIesque object which functions as a form

        print('''
====== REGISTER A REFUGEE ======

Inputs required:

[1] CampID
[2] Primary Refugee Name
[3] Dependents
                            
        ''')

        while True:

            # run a verify camp function
            campID = int(input("Enter camp id: "))
            primaryName = input("Enter primary refugee name: ")
            dependents = []
            print('Type "done" if no more dependents')
            while True:
                dependentName = input(
                    "Enter dependent name (type 'done' if no more dependents): ")
                if dependentName.lower() == "done":
                    break
                else:
                    # append it to the dependents list
                    dependents.append(dependentName)

            # ask user to confirm results
            while True:
                print(
                    f"Confirm the inputs - CampID:{campID} Primary Refugee:{primaryName} Dependents:{dependents} ")
                choice = input("Confirm choice with Y/N: ")
                if choice.lower() not in 'YyNn':
                    print('invalid entry')
                    raise exceptions.InputError()
                else:
                    break

            if choice.lower() == 'y':
                refu.add_refugee(campID, primaryName, dependents)
                print('refugee added')

                # print success
                break

            elif choice.lower() == 'n':
                print('Re-enter inputs: ')
                continue

    def my_details(self):
        # get a bunch of inputs and pass the form into the function
        # Maybe interact with a GUIesque object which functions as a form
        # user.whatever()
        details = usfu.view(self)
        return details

    def modify_details(self, tochange, oldvalue, newvalue):
        check = usfu.modify(self, tochange, oldvalue, newvalue)
        return check

    # do we even need this in this file considering the menu has an exit function?
    def exit_programme(self):
        pass
        # write all changes to self and exit

# Method not needed, handled by menu and modify_details
##
# def deactivate_self(self):
# while True:
# deactivate = input("""
# Confirm whether you want to deactive your account.
# You will need to contact the admin to reactivate your account.
# Confirm (Y/N): """)
# if deactivate.lower()=="y":
# swaps active status - if you get to this point you should have isActive = True
# usfu.toggle_volunteer_status(self.username)
##                 print("Your account is deactivated, thank you.")
# break
# elif deactivate.lower()=="n":
##                 print("Your account is NOT deactivated")
# break
# else:
##                 print("Invalid input")
# continue
# deactivate account and exit

    def view_refugees(self):
        while True:
            if self.userType == Admin:
                print("""
                ====== VIEW REFUGEES ======
                          
                          Search by:
                          
                          [1] Refugee ID (individual/family)
                          [2] Camp ID
                          [3] View all
                          [/q] quit to menu
    
                """)
                view = input("Enter Choice: ")
                if view == '/q':
                    backmenu = menu(['admin'])
                elif view == '1':
                    id = int(input("Enter refugee id: "))
                    refu.view_refugee(refugeeID=id)

                elif view == '2':
                    id = int(input("Enter camp id: "))
                    refu.view_refugee_camp(campID=id)

                elif view == '3':
                    refu.view_all_refugees()

                else:
                    print("Invalid input. ")

            else:

                pass
                print("""
                ====== VIEW REFUGEES ======
                          
                          Search by:
                          
                          [1] Refugee ID (individual/family)
                          [2] View all from camp ID
    
                """)
                view = int(input("Enter Choice:"))

                if view == 1:
                    id = int(input("Enter refugee id: "))
                    refu.view_refugee(refugeeID=id)

                elif view == 2:
                    refu.view_refugee_camp(campID=self.camp)
        else:

            pass  # is someone working on this right now?

####################################################################################################################################
####################################################################################################################################


class Admin(Volunteer):

    def __init__(self, username):
        self.username = username
        self.isActive = True
        self.userType = type(self)

    def create_EP(self):
        # get a bunch of inputs and pass the form into the function
        # Maybe interact with a GUIesque object which functions as a form
        # can be the same as the one for regisering volunteers

        empl.add_plan()

    def deactivate_vol(self):

        u = input("Give the username of the volunteer to deactivate:\n")
        usfu.toggle_volunteer_status(u)

    def manage_volunteer(self):

        while True:
            print('''

====== WELCOME TO Volunteer Management ======

[1] Add Volunteer
[2] Delete Volunteer
[3] View Volunteer
[4] View all Volunteer
[5] Change Volunteer state
[6] View Volunteer requests
[/q] Quit to Admin Menu
[/e] Exit (Log Out)

            ''')
            choice = input("Enter Choice: ")

            if choice == '1':
                n = input("Please enter the volunteer's name: ")
                e = input("Please enter the volunteer's email address: ")
                ph = input("Please enter the volunteer's phone number: ")
                while True:
                    c = input(
                        "Please enter the volunteer's camp id (skip if inactive): ")
                    if c == '':
                        break
                    try:
                        c = int(c)
                        break
                    except:
                        print('Please enter a valid camp id')
                r = input("Please enter the volunteer's role: ")

                # are these variable names correct?
                usfu.add_volunteer(
                    name=n, email=e, phonenum=ph, campID=c, role=r)
                continue

            elif choice == '2':
                delusername = input(
                    "Please Enter Volunteer username to Delete: ")
                if delusername == "":
                    print("ERROR: Please enter name to delete")
                    continue
                else:
                    usfu.delete_volunteer(delusername)
                continue

            elif choice == '3':
                viewusername = input("Please Enter Volunteer Name: ")
                if viewusername == "":
                    print("ERROR: Please enter name")
                    continue
                else:
                    usfu.view(viewusername)
                continue

            elif choice == '4':
                usfu.view_all()
                continue

            elif choice == '5':
                stateusername = input(
                    "Please Enter Volunteer Name To Change State: ")
                if stateusername == "":
                    print("ERROR: Please enter name")
                    continue
                else:
                    usfu.toggle_volunteer_status(stateusername)
                continue

            elif choice == '6':
                # call some method or other object
                continue

            elif choice == '/e':
                break

            elif choice == '/q':
                back_to_menu = menu(['admin'])

            else:
                print('\n\nInvalid input...\n\nPlease try again.\n\n')
                continue

    def manage_ep(self):
        """
        description: will bring up a menu for functions we can perform on the emergency plans.
        """
        while True:
            print('''
            ====== WELCOME TO Emergency Plan Management ======

    [1] Add Emergency Plan
    [2] Delete Emergency Plan
    [3] View Emergency Plan
    [4] View all Emergency Plan
    [5] Modify Emergency Plan
    [/q] Quit to Admin Menu
    [/e] Exit (Log Out)
        ''')
            choice = input("Enter Choice: ")

            if choice == '1':
                empl.add_plan()
                continue

            elif choice == '2':
                print('Here are all the plans: ')
                empl.view_all_eps()
                delepid = input("Please Enter Emergency Plan ID to Delete: ")
                if delepid == "":
                    print("ERROR: Please enter Plan to delete")
                    continue
                else:
                    empl.delete_ep(delepid)
                continue

            elif choice == '3':
                viewname = input(
                    "Please Enter emergency plan name (it'll search by keyword): ")
                if viewname == "":
                    print("ERROR: Please enter valid input")
                    continue
                else:
                    empl.view_ep(viewname)
                continue

            elif choice == '4':
                empl.view_all_eps()
                continue

            elif choice == '5':
                while True:
                    epID = input(
                        "Please Enter Emergency Plan ID To Change Details or press /q to return: ")
                    if epID == '/q':
                        self.manage_ep()
                    if epID == "":
                        print("ERROR: Please enter valid ID")
                        pass
                    output = empl.view_ep_byID(int(epID))
                    if output:
                        print(output)
                        name = ''
                        description = ''
                        end_date = None
                        category = ''
                        answer = input('change name (y/n)?')
                        if answer == 'y':
                            name = input('Input new name: ')
                        answer = input('change description (y/n)?')
                        if answer == 'y':
                            description = input('Input new description: ')
                        answer = input('change end date (y/n)?')
                        if answer == 'y':
                            end_date = input('Input new end date: ')
                        answer = input('change category (y/n)?')
                        if answer == 'y':
                            category = input('Input new category: ')
                        empl.modify_ep(int(
                            epID), name=name, description=description, end_date=end_date, category=category)
                        break
                    else:
                        print(f'Emergency Plan {epID} not valid.')
                continue
            elif choice == '6':
                # call some method or other object
                continue

            elif choice == '/e':
                sys.exit()
            # to quit back to the admin menu we just instantiate a new menu object with the admin
            elif choice == '/q':
                back_to_menu = menu(['admin'])

            else:
                print('\n\nInvalid input...\n\nPlease try again.\n\n')
                continue

    def manage_camp(self):
        """
        description: will bring up a menu for functions we can perform on the camps
        """
        while True:
            print('''
====== WELCOME TO Emergency Plan Management ======

[1] Add Camp to Emergency Plan
[2] Delete Camp
[3] View Camp
[4] View all Camps
[5] Modify Camp
[/q] Quit to Admin Menu
[E] Exit (Log Out)
        ''')
            choice = input("Enter Choice: ")

            if choice == '1':
                empl.view_all_eps()

                e = input('Please enter EP ID: ')
                t = input('Please enter number of tents: ')
                f = input('Please enter the amount of food in the camp: ')
                m = input('Please enter the amount of medicine in the camp: ')
                camp.add_camp(epID=e, tents=t, food=f, med=m)
                # empl.add_plan()
                continue

            elif choice == '2':
                camp.view_all_camps()
                d = input("Please Enter Camp ID to Delete: ")
                if d == "":
                    print("ERROR: Please enter Camp ID to delete")
                    continue
                else:
                    camp.delete_camp(d)
                continue

            elif choice == '3':
                viewname = input("Please Enter Camp ID: ")
                if viewname == "":
                    print("ERROR: Please enter name")
                    continue
                else:
                    camp.view_camp(viewname)
                continue

            elif choice == '4':
                camp.view_all_camps()
                continue

            elif choice == '5':
                camp.view_all_camps()
                c = input(
                    "Please Enter Camp ID To Change Details: ")
                if c == "":
                    print("ERROR: Please enter ID")
                    continue
                else:
                    camp.view_camp(c)
                    print(
                        'Type new value for each attribute - leave blank to maintain current.')
                    t = input("New number of tents: ")
                    f = input("New amount of food: ")
                    m = input("New amount of medicine")
                    camp.modify_camp(campID=c, med=m, food=f, tents=t)
                continue

            elif choice in 'Ee':
                sys.exit()
            # to quit back to the admin menu we just instantiate a new menu object with the admin
            elif choice == '/q':
                back_to_menu = menu(['admin'])

            else:
                print('\n\nInvalid input...\n\nPlease try again.\n\n')
                continue


###############################################################################################################
################################################################################################################
###############################################################################################################
###############################################################################################################

# Start of menu


class menu:

    def __init__(self, user):
        print(user)
        self.done = False
        self.Home = True

        # we are going to make an object depending on the value of user
        if user[0] == 'admin':
            user = Admin('admin')
        elif user[0] == 'volunteer':
            username = user[1]
            user = Volunteer(username, user[2], user[3])
        while not self.done:

            self.Home = True

            print('''              
====== WELCOME TO BLABLABLUI ====== ''')

            if type(user) == Volunteer and user.isActive:

                print('''
What do you wish to do today?

[1] My details
[2] Register a refugee
[3] My camp
[4] View refugees
[E] Exit
     
                    ''')

                choice = input("Enter Choice:")

                if choice == '1':
                    sub = display_details(user, self)
                    continue

                elif choice == '2':
                    user.register_refugee()

                elif choice == '3':
                    self.display_camps(user)

                elif choice == '4':
                    user.view_refugees()

                elif choice in 'Ee':
                    self.done = True

                else:
                    print('\n\nInvalid input...\n\nPlease try again.\n\n')
                    continue

            elif type(user) == Volunteer and not user.isActive:

                print('''
                      
Unfortunately, your account is deactivated.
Please contact admin for more information.
                           
                    ''')

                self.done = True

            elif type(user) == Admin:

                print('''
                
What do you wish to do today?

[1] My details
[2] View and Manage Volunteers
[3] View and Manage Emergency Plans
[4] View and Manage Camps
[5] View Refugees
[E] Exit (Log Out)
       
                    ''')
                choice = input("Enter Choice: ")

                if choice == '1':

                    submenu = display_details(user, self)
                    continue

                elif choice == '2':
                    user.manage_volunteer()

                elif choice == '3':
                    user.manage_ep()

                elif choice == "4":
                    user.manage_camp()

                elif choice == '5':
                    user.view_refugees()

                elif choice in 'Ee':
                    # main1.main()
                    # continue
                    # break
                    self.done = True

                else:
                    print('\n\nInvalid input...\n\nPlease try again.\n\n')
                    continue

        else:
            self.destroy
            # return some error
            # maybe use click to get help for menu

    def destroy(user):

        user.exit_programme()
        del self
        sys.exit()

####################################################################################################################################
####################################################################################################################################


class display_details:

    def __init__(self, user, menu):
        # print(user)
        self.done = False
        self.Home = True

        # print(user.my_details())

        while not self.done:

            detailskey = user.my_details()
            print('\n\n====== VIEWING MY DETAILS ====== \n')

            print('Username: ' + detailskey.get('username', 'N/A'))
            print('Email: ' + detailskey.get('email', 'N/A'))
            print('Name: ' + detailskey.get('name', 'N/A'))
            print('Password: ' + ('x' * len(str(detailskey.get('password', 'N/A')))))
            # why can't you view your own password? And doesn't it just make more sense not to display this?
            print('Phone Number: ' + detailskey.get('phonenum', 'N/A') + '\n')

            if type(user) == Volunteer:
                print('Account type: Volunteer')
                print(' Camp: ' + detailskey.get('camp', 'N/A'))
                print(' Role: ' + detailskey.get('role', 'N/A'))

            else:
                print('Account type: Admin')

            print('\n=============================== ')

            print('''
What do you wish to do with your details
[1] Change details''')
            if type(user) == Volunteer:
                print('[2] Deactivate account')
            print('[H] Home')

            choice = input("Enter Choice: ")

            if choice == '1':
                attrlist = ('username', 'email', 'name',
                            'password', 'phonenum', 'camp', 'role')
                detailslist = [detailskey.get(x, 'N/A') for x in attrlist]
                self.change_details(user, detailslist)
                if not self.Home:
                    self.done = True

            elif choice == '2' and isinstance(user, Volunteer):
                self.deactivate_account(user, menu, detailskey)
                if not self.Home:
                    self.done = True

            elif choice in 'Hh':
                return

            else:
                print('\n\nInvalid input...\nPlease try again.\n')
                continue

        else:
            del self

    def change_details(self, user, oldlist):

        while not self.done:

            # NEW
            printmenu = False

            print('''
What details do you wish to change
[1] Change Email
[2] Change Name
[3] Change Password
[4] Change Phone Number''')

            if type(user) == Volunteer:
                print('''
[5] Change Camp
[6] Change Role''')

            print('''
[B] Back
[H] Exit Home''')

            choice = input("Enter Choice: ")
            attrlist = ['x', 'email', 'name', 'password', 'phonenum'] + \
                ['camp', 'role']*isinstance(user, Volunteer)

            try:
                choice = int(choice)
                tochange = attrlist[choice].capitalize()
                printmenu = True
                oldvalue = oldlist[choice]

            except ValueError:  # B, H, Other stuff
                if choice in 'Bb':
                    return
                elif choice in 'Hh':
                    self.Home = False
                    return
                else:
                    print('\n\nInvalid input...\nPlease try again.\n')
                    continue

            except IndexError:  # input numeric value out of scope
                print('\n\nInvalid input...\nPlease try again.\n')
                continue

            if printmenu:
                print('\n\n====== CHANGE ' + tochange + ' ====== \n')
                if tochange != 'password':
                    print('Your old ' + tochange + ': ' + str(oldvalue))

                else:
                    print('Your old ' + tochange + ': ' +
                          ('x' * len(str(oldvalue))))
                    # but how is this useful?

                newvalue = input('Enter new ' + tochange + ': ')

                if (newvalue == input('Confirm new ' + tochange + ': ')):
                    check = user.modify_details(tochange, oldvalue, newvalue)

                    if (check):
                        print("\n" + tochange + " changed successfully!\n")
                        while True:
                            changes = "Do you wish to change any other of your details? [y/n]\n"
                            cont = input(changes)

                            if cont == 'y':
                                print('================================\n\n')
                                break

                            elif cont == 'n':
                                return

                            else:
                                print('Invalid Input! please try again...')

                    else:
                        print('Something went wrong, please try again...')

                else:

                    print('Invalid Input! please try again...')

            # if not printmenu:
            #    continue #I think this was the intention
            #
            #print('\n\n====== CHANGE ' + tochange + ' ====== \n')
            #placeholder = 'x'
            #print(f'Your old {tochange}: {oldvalue}'*(tochange != 'password') or f'Your old {tochange}: {placeholder * len(oldvalue)}')
            # don't worry about it ^
            #
            #newvalue = input('Enter new ' + tochange + ': ')
            #confirmvalue = input('Confirm new ' + tochange + ': ')
            # if newvalue != confirmvalue:
            #    print('Invalid Input! please try again...')
            #    continue
            #
            #check = user.modify_details(tochange, oldvalue, newvalue)

    def deactivate_account(self, user, menu, detailskey):

        print('\n\n========== DEACTIVATE ACCOUNT ==========\n')
        print('THE ADMINISTRATOR WILL BE NOTIFIED OF YOUR DEACTIVATION REQUEST.\n')
        print('IF ACCEPTED, YOU WILL BE LOCKED OUT OF YOUR ACCOUNT.\n')

        while True:
            changes = "DO YOU WISH TO PROCEED? [y/n]\n"
            cont = input(changes)

            if cont == 'y':
                print('================================\n\n')
                password = input('Enter your password to continue: ')

                if password != detailskey['password']:
                    print('\nWrong password entered. Please try again.')
                    continue

                else:
                    check = user.modify_details('isActiveReq', True, False)
                    if check:
                        print(
                            'Request accepted and admin notified. This session will now be terminated.')
                        self.Home = False
                        menu.done = True
                        return

                    else:
                        print('Something went wrong, please try again...')
                        return

            elif cont == 'n':
                return

            else:
                print('Invalid Input! please try again...')

###################################################################################################################################
###################################################################################################################################


class handle_volunteers:
    def __init__(self, user):

        self.options = True

        while True:

            if self.options:
                print('\n\n====== SELECT WHICH ACTION TO TAKE ====== \n')
                print('''   
What do you wish to do:
[1] View Volunteer Details
[2] View All Volunteer Details
[3] Manage Volunteers
[H] Home
                        ''')

            detailskey = user.my_details()

            print('\n\n====== VIEWING VOLUNTEER DETAILS ====== \n')

            print('Username: ' + detailskey.get('username', 'N/A'))
            print('Email: ' + detailskey.get('email', 'N/A'))
            print('Name: ' + detailskey.get('name', 'N/A'))
            print('Password: ' + ('x' * detailskey.get('password', 'N/A')))
            # why can't you view your own password? And doesn't it just make more sense not to display this?
            print('Phone Number: ' + detailskey.get('phonenum', 'N/A') + '\n')

            if isinstance(user, Volunteer):
                print('Account type: Volunteer')
                print(' Camp: ' + detailskey.get('camp', 'N/A'))
                print(' Role: ' + detailskey.get('role', 'N/A'))

            else:
                print('Account type: Admin')

            print('\n=============================== \n')

            print('''
                  
    What do you wish to do with your details
    [1] Change details
    [2] Deactivate account
    [H] Home
            ''')

            choice = input("Enter Choice: ")

            if choice == '1':
                attrlist = ('username', 'email', 'name',
                            'password', 'phonenum', 'camp', 'role')
                detailslist = [detailskey.get(x, 'N/A') for x in attrlist]
                self.change_details(user, detailslist)
                if not self.Home:
                    del self

            elif choice == '2':
                self.deactivate_account(user)

            elif choice in 'Hh':
                return

            else:
                print('\n\nInvalid input...\n\nPlease try again.\n\n')
                continue
