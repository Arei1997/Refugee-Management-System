from os.path import exists, dirname,abspath
import json
import logging
from importlib.machinery import SourceFileLoader

DIR = dirname(abspath(__file__))[:-8] #current directory
logging.basicConfig(filename = DIR + '/methods.log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')
exceptions =  SourceFileLoader('customExceptions',DIR+R'/EXCEPTIONS/customExceptions.py').load_module()
 

if not exists(DIR+'/refugees.json'):
    refugeedata = {
        'refugees' : [],
        'count' : 0,
        'familycount' : 0
    }
    with open(DIR+'/refugees.json','w') as j: json.dump(refugeedata, j, indent = 3)
    logging.debug(' refugees.json file created.')


def add_refugee(camp = '', primaryName = '', dependants = [], **kwargs):
    #TODO: we need a count of refugees per camp
    if not camp or not primaryName:
        raise exceptions.InputError()


    with open(DIR+'/refugees.json','r') as j: data = json.load(j)

    # for item in data['refugees']:
    #     if item['primaryRefugee'] == primaryName and item['familyMembers'] == dependants and item['camp'] == camp:
    #         raise ex.AlreadyExistError('Refugee and family of: ' + primaryName)

    refugeedata = {
        'refugeeID' : int(data['refugees'][-1]['refugeeID']) + 1 if data['count'] else 1,
        'camp': camp,
        'primaryRefugee': primaryName,
        'familyMembers': dependants
    }

    data['refugees'].append(refugeedata)
    data['familycount'] += 1
    data['count'] += (1 + len(dependants))
    familycount = data['familycount']
    count = data['count']
    with open(DIR+'/refugees.json','w') as j: json.dump(data, j, indent = 2)

def delete_refugee(camp = '',refugeeID = ''): #ep and id give unique camp
    if not refugeeID and not camp:
        raise exceptions.InputError()
    with open(DIR+'/refugees.json','r') as j: data = json.load(j)
    if not camp and not refugeeID: return None

    for item in data['refugees']:
        if item['refugeeID'] == refugeeID:
            dec = len(item['familyMembers']) + 1
            data['refugees'].remove(item)
            #prevents decrementing count if camp deleted twice
            break
    else:
        raise exceptions.NoExistError('Refugee with ID ' + str(refugeeID) + ' at camp ' + str(camp))

    data['count'] -= dec
    data['familycount'] -= 1
    count = data['count']

    with open(DIR+'/refugees.json','w') as j: json.dump(data, j, indent = 3)
    logging.debug(f'Refugee (ID: {refugeeID}) of camp {camp} removed. Count: {count}.')

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
            break
    else:
        raise exceptions.NoExistError('The camp with ID ' + str(campID) + ' and emergency plan ' + str(epID))

    logging.debug(f'Camp (ID: {campID}) with associated emergency plan(s): {epID}, viewed.')

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


#add_refugee(6,'John Richardson', ['Mrs Richardson', 'Richardson Jnr', 'Richardson Girl'])
#delete_refugee(6,2)
#view_camp('1', '4')
#modify_camp('1', '2', food='10')


#ZAID practice
# def remove_camp(): 
#     new_list = []
#     with open('camps.json','r') as j:
#         open_file = json.load(j)
#         delete_camp = input('Please enter the ID of the camp to be removed: ')
#         i = 0
#         for camp in open_file['camps']:
#             if open_file['camps'][i]['id'] == int(delete_camp):
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
# def remove_camp(camp_id):
#     #removed_list = [] # an idea to prevent count from going lower with repeated id removal
#     new_list = []
#     with open('camps.json','r') as j:
#         open_file = json.load(j)
#     i = 0
#     for camp in open_file['camps']:
#         if open_file['camps'][i]['id'] == camp_id:
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
