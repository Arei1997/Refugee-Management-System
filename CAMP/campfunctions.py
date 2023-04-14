from os.path import exists, dirname,abspath
import json
from importlib.machinery import SourceFileLoader
DIR = dirname(abspath(__file__))[:-5] #current directory
mymodule = SourceFileLoader('userfunctions',DIR+R'/USER/userfunctions.py').load_module()
exceptions =  SourceFileLoader('customExceptions',DIR+R'/EXCEPTIONS/customExceptions.py').load_module()

import logging
#import EXCEPTIONS.customExceptions as ex
logging.basicConfig(filename = DIR + '/methods.log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')

#establish generic file structure - camp container
if not exists(DIR+'/camps.json'):
    campdata = {
        'camps' : [],
        'count' : 0
    }
    with open(DIR+'/camps.json','w') as j: json.dump(campdata, j, indent = 3)
    logging.debug(' camps.json file created.')
#brought outside to put into generic main function at later date


def add_camp(epID, **kwargs): #  opt: emergency plan(can a camp exist without emergency plan), tents,food, med
    #ep necessary to add camp, but not necessary to maintain one - e.g. ep ends but camp remains

    # get kwargs arguments if they exist else set to 0
    tents = kwargs.get('tents', 0)
    food = kwargs.get('food',0)
    med = kwargs.get('med',0)

    with open(DIR+'/camps.json','r') as j: data = json.load(j)
    campID = int(data['camps'][-1]['campID'])+1 if data['count'] else 1

    # find out id value
    camps = {
        'campID': campID,
        'epID': epID,
        'tents': tents,
        'food':food,
        'med':med
    }

    data['camps'].append(camps)
    data['count'] += 1
    count = data['count']
    with open(DIR+'/camps.json','w') as j: json.dump(data, j, indent = 2)
    logging.debug(f' Camp added. campID: {campID} epID: {epID}, Tents: {tents}, foodstuffs: {food}, Med. Supplies {med}, Count: {count}.')


def delete_camp(campID = ''): #epID and id give unique camp

    with open(DIR+'/camps.json','r') as j: data = json.load(j)
    if not campID:
        raise exceptions.InputError()

    for item in data['camps']:
        if item['campID'] == campID:
            data['camps'].remove(item)
            #prevents decrementing count if camp deleted twice
            break
    else: 
        print(campID)
        raise exceptions.NoExistError('Camp with ID ' + str(campID))

    data['count'] -= 1
    with open(DIR+'/camps.json','w') as j: json.dump(data, j, indent = 3)

    # delete volunteers associated with the camp
    with open(DIR+'/users.json','r') as j: data = json.load(j)
    print(data)

    for item in data['volunteers']:
        print(item)
        if item['campID']==campID:
            mymodule.modify_volunteer(username=item['username'],campID=None)
    logging.debug(f' Camp (ID: {campID}) deleted.') #update this

# can be for all camps or a specific one
def view_all_camps(): # can't be for all camps or a specific one
    with open(DIR+'/camps.json','r') as j: data = json.load(j)
    for camp in data['camps']:
        print(camp)
    logging.debug(' All camps viewed.')

    #no need to close file when using above method
    #j.close()

def view_camp(epID = '', campID = ''): #cannot be for all camps
    with open(DIR+'/camps.json','r') as j: data = json.load(j)
    if not epID and not campID:
        raise exceptions.InputError()

    for camp in data['camps']: #good practice to name object iterator something meaningful
        if camp['epID'] == epID and camp['campID'] == campID:
            print(camp)
            break
    else:
        raise exceptions.NoExistError('The camp with ID ' + str(campID) + ' and emergency plan ' + str(epID))

    logging.debug(f' Camp (ID: {campID}) with associated emergency plan(s): {epID}, viewed.')



def modify_camp(epID = '', campID = '', **kwargs): # you can change the amount of tents, food, etc at the camps & the numbers passed represent changes in amount
    with open(DIR+'/camps.json','r') as j: data = json.load(j)
    if not epID and not campID:
        raise exceptions.InputError()

    '''tent = kwargs.get('tent',0)
    food = kwargs.get('food',0)
    med = kwargs.get('med',0)
    '''
    #^why? You do not want to assign if not specified

    for item in data['camps']:
        if item['epID'] == epID and item['campID'] == campID:
            for key in kwargs: 
                item[key] = kwargs.get(key)
            break
    else:
        raise exceptions.NoExistError('The camp with ID ' + str(campID) + ' and emergency plan ' + str(epID))

    with open(DIR+'/camps.json', 'w') as j: json.dump(data, j, indent = 3)
    logging.debug(f' Camp (ID: {campID}, associated EP: {epID}) modified. Keyword arguments added: {kwargs}') #fix because there may be an issue


def modify_camp_2(supply, quant, epID = '', campID = ''):
    '''

    :param supply:  the supplies you want to increment
    :param quant: the amount which you want to increment by
    :param epID:
    :param campID:
    :return:
    '''
    with open(DIR+'/camps.json','r') as j: data = json.load(j)
    if not epID and not campID:
        raise exceptions.InputError()

    for item in data['camps']:
        if all([item['epID']== epID, item['campID'] == campID]):
            item[supply] = max(item[supply] + quant, 0)
            break
    else:
        raise exceptions.NoExistError('The camp with ID ' + str(campID) + ' and emergency plan ' + str(epID))

    with open(DIR+'/camps.json','w') as j: json.dump(data, j, indent = 3)
    logging.debug(f' Camp (ID: {campID}, associated EP: {epID}) modified. Supply - {supply} was changed by {quant}.') #fix because there may be an issue
    
#add_camp(3, tents='20', med='50')
#view_all_camps()
#view_camp(3, 2)
#modify_camp(epID=3, campID=2, med='501', tent='70')
#delete_camp(1)
#modify_camp_2('tents', 50, '3', '2')


#ZAID practice
# def remove_camp(): 
#     new_list = []
#     with open('camps.json','r') as j:
#         open_file = json.load(j)
#         delete_camp = input('Please enter the ID of the camp to be removed: ')
#         i = 0
#         for camp in open_file['camps']:
#             if open_file['camps'][i]['campID'] == int(delete_camp):
#                 pass
#                 i += 1
#             else:
#                 new_list.append(camp)
#                 i += 1
#         open_file['camps'] = new_list
#         open_file['count'] -= 1
#         with open('camps.json','w') as j:
#             json.dump(open_file, j, indent = 2)
            
#    #another iteration
# def remove_camp(campID):
#     #removed_list = [] # an idea to prevent count from going lower with repeated id removal
#     new_list = []
#     with open('camps.json','r') as j:
#         open_file = json.load(j)
#     i = 0
#     for camp in open_file['camps']:
#         if open_file['camps'][i]['campID'] == camp_id:
#             i += 1
#             continue
#         else:
#             new_list.append(camp)
#             i += 1
#     open_file['camps'] = new_list
#     open_file['count'] -= 1
#     #removed_list.append(num) 
#     with open('camps.json','w') as j:
#         json.dump(open_file, j, indent = 2)
#delete_camp()