from os.path import exists, dirname,abspath
import json
from importlib.machinery import SourceFileLoader
DIR = dirname(abspath(__file__))[:-5] #current directory
exceptions =  SourceFileLoader('customExceptions',DIR+R'/EXCEPTIONS/customExceptions.py').load_module()

import logging
logging.basicConfig(filename = DIR + '/methods.log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')


#init block
if not exists(DIR+'/users.json'):
    userdata = {
        'admin' : {'username': 'admin', 'password': '111'},
        'volunteers': [ #yes? no?
            {'username': 'volunteer1', 'password': '111', 'isActive': False, 'campID': None},
            {'username': 'volunteer2', 'password': '111', 'isActive': False, 'campID': None},
            {'username': 'volunteer3', 'password': '111', 'isActive': False, 'campID': None}
        ],
        'count': 3 #or 0?
    }
    with open(DIR+'/users.json','w') as j: json.dump(userdata, j, indent = 3)
    logging.debug(' users.json file created.')


def add_volunteer(**kwargs): #kwargs mapped from registration page; do not include if no value

    with open('users.json','r') as j: data = json.load(j)
    num = int(data['volunteers'][-1]['username'][9:])+1 if data['count'] else 1

    volunteer = {
        'username': f'volunteer{num}',
        'password': '111',
        'isActive': ("campID" in kwargs.keys())
    }
    for item in kwargs: volunteer[item] = kwargs.get(item)

    data['volunteers'].append(volunteer)
    data['count'] += 1
    with open('users.json','w') as j: json.dump(data, j, indent = 3)
    
    count = data['count']
    username = volunteer['username']
    # word = volunteer['word']
    isActive = volunteer['isActive']
    campID = kwargs.get('campID', None)
    logging.debug(f' Volunteer added to camp (ID: {campID}). Username: {username}. Count: {count}. Volunteer: {isActive}')


def modify_volunteer(username = '', **kwargs): #set arg = None if attr empty/removed
    with open('users.json','r') as j: data = json.load(j)
    if not username:
        raise exceptions.InputError()
        

    for item in data['volunteers']:
        if item['username'] == username:
            for key in kwargs: item[key] = kwargs.get(key)
            item['isActive'] = not item['campID'] == None
            break
    else:
        raise exceptions.NoExistError('User with username: ' + username)

    with open('users.json', 'w') as j:
        json.dump(data, j, indent = 3)
    
    logging.debug(f' Volunteer modified. Username: {username}. Keyword arguments added: {kwargs}')


def delete_volunteer(username = ''):
    with open('users.json','r') as j: data = json.load(j)
    if not username:
        raise exceptions.InputError()

    for item in data['volunteers']:
        if item['username'] == username:
            data['volunteers'].remove(item)
            break
    else: 
        raise exceptions.NoExistError('User with username: ' + username)
        

    data['count'] -= 1
    with open('users.json','w') as j: json.dump(data, j, indent = 3)
    logging.debug(f' Volunteer deleted. Username: {username}')
    

#is this needed now? inactive user defined as without camp/EP/role
def toggle_volunteer_status(username = ''):
    with open('users.json','r') as j: data = json.load(j)
    if not username:
        raise exceptions.InputError()
        

    for item in data['volunteers']:
        if item['username'] == username:
            item['isActive'] = not item['isActive']
            break
    else: 
        raise exceptions.NoExistError('User with username: ' + username)
        

    with open('users.json','w') as j: json.dump(data, j, indent = 3)
    logging.debug(f' Volunteer toggled off. Username: {username}')
