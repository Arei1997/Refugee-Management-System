from os.path import exists, dirname,abspath
import json
import logging
from importlib.machinery import SourceFileLoader
DIR = dirname(abspath(__file__))[:-3] #current directory
exceptions =  SourceFileLoader('customExceptions',DIR+R'/EXCEPTIONS/customExceptions.py').load_module()


#logging.basicConfig(filename = DIR + '/methods.log', level = logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

#establish generic file structure - camp container
if not exists(DIR+'/ep.json'):
    epdata = {
        'ePlan' : [],
        'count' : 0
    }
    with open(DIR+'/ep.json','w') as j: json.dump(epdata, j, indent = 3)
    logging.debug(' ep.json created')
#brought outside to put into generic main function at later date


def add_plan(**kwargs): #  opt: emergency plan(can a camp exist without emergency plan), tent,food, med 
    #ep necessary to add camp, but not necessary to maintain one - e.g. ep ends but camp remains
    # get kwargs arguments if they exist else set to 0
    name = kwargs.get('name','')
    description = kwargs.get('description','')
    start_date = kwargs.get('start_date','')
    end_date = kwargs.get('end_date','')
    category = kwargs.get('category','')
    geo = kwargs.get('geo','')
    
    with open(DIR+'/ep.json','r') as j: data = json.load(j)

    epID = int(data['ePlan'][-1]['epID'])+1 if data['count'] else 1

    # find out id value
    EP = {
        #'epID': int(data['ePlan'][-1]['epID'])+1 if data['count'] else 1,
        'epID' : epID,
        'name': name,
        'description': description,
        'start_date': start_date,
        'end_date':end_date,
        'category': category,
        'geo': geo
    }

    data['ePlan'].append(EP)
    data['count'] += 1
    count = data['count'] # added
    with open(DIR+'/ep.json','w') as j: json.dump(data, j, indent = 2)
    logging.debug(f' EP created. Name: {name}, ID: {epID}, Category: {category}, Location: {geo}, Starts {start_date} & Ends {end_date}, Description: {description}, Count: {count}.')

def delete_ep(epID = ''): #delete camps and set volunteers to inactive - refugees?
    
    # start big to small
    # delete EP
    with open(DIR+'/ep.json','r') as j: data = json.load(j)
    if not epID:
        raise exceptions.InputError()

    for item in data['ePlan']:
        if item['epID'] == epID:
            data['ePlan'].remove(item)
            #prevents decrementing count if camp deleted twice
            break
    else: raise exceptions.NoExistError('The emergency plan with ID ' + str(epID))

    data['count'] -= 1
    with open(DIR+'/ep.json','w') as j: json.dump(data, j, indent = 3)
    
    # delete camps for that EP and get all camp IDS to an array
    with open(DIR+'/camps.json','r') as j: data = json.load(j)

    campArray = []
    for item in data['camps']:
        if item['epID'] == epID:
            ## get campID to an array
            campArray.append(item['campID'])
            data['camps'].remove(item)
            data['count'] -= 1            

    with open(DIR+'/camps.json','w') as j: json.dump(data, j, indent = 3)
    
    # make volunteers inactive from campID
    with open(DIR+'/users.json','r') as j: data = json.load(j)

    for item in data['volunteers']:
        campID = item.get('campID')
        if campID in campArray:
            item['isActive'] = False
            data['count'] -= 1            

    with open(DIR+'/users.json','w') as j: json.dump(data, j, indent = 3)
    
    # delete refugees
    with open(DIR+'/refugees.json','r') as j: data = json.load(j)

    for item in data['refugees']:
        if item['campID'] in campArray:
            data['refugees'].remove(item)
            data['familycount'] -= 1
            data['count'] -= 1 + len(item['dependants'])
            # logging.debug(f'{campArray} removed')       
    familyCount = data['familycount'] #added
    with open(DIR+'/refugees.json','w') as j: json.dump(data, j, indent = 3)
    logging.debug(f' Emergency plan (ID: {epID}) deleted. Camps deleted: {campArray}. Families remaining: {familyCount}.')


# can be for all EPS or a specific one
def view_all_eps(): # can be for all camps or a specific one
    with open(DIR+'/ep.json','r') as j: data = json.load(j)
    for ePlan in data['ePlan']:
        print(ePlan)
    logging.debug(' All emergency plans viewed')
    #no need to close file when using above method
    #j.close()

def view_ep(epID = ''): #cannot be for all camps
    with open(DIR+'/ep.json','r') as j: data = json.load(j)
    if not epID:
        raise exceptions.InputError()

    for ePlan in data['ePlan']: #good practice to name object iterator something meaningful
        if ePlan['epID'] == epID:
            print(ePlan)
            break
    else:
        raise exceptions.NoExistError('The emergency plan with ID ' + str(epID))

    logging.debug(f' Emergency plan (ID: {epID}) viewed.')



def modify_ep(epID = '', **kwargs): # you can change the amount of tents, food, etc at the camps & the numbers passed represent changes in amount
    with open(DIR+'/ep.json','r') as j: data = json.load(j)
    if not epID:
        raise exceptions.InputError()

    for item in data['ePlan']:
        if item['epID'] == epID:
            for key in kwargs: 
                item[key] = kwargs.get(key)
            break
    else:
        raise exceptions.NoExistError('The emergency plan with ID ' + str(epID))

    with open(DIR+'/ep.json', 'w') as j: json.dump(data, j, indent = 3)
    logging.debug(f' Emergency plan (ID: {epID}) modified. Keyword arguments added: {kwargs}') #fix because there may be an issue


# delete_ep(1)
# add_plan(name='test',description='test123',start_date = '05-12-2022', end_date = '20-12-2022', category = 'earthquake', geo = 'Wakanda')
# view_ep(epID = 3)
# modify_ep(epID = 3,name='test',description='test',start_date = '05-12-2022', end_date = '20-12-2022', category = 'earthquake', geo = 'Wakanda')