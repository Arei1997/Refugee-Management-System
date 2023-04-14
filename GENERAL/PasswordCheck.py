import re

#def valid_password(password):
#    while True:
#        # length
#        if len(password) < 8:
#            break
#        # lower case
#        if re.search(r'[a-z]', password) is None:
#            break
#        # upper case
#        if re.search(r'[A-Z]', password) is None:
#            break
#        #numbers
#        if re.search(r'[0-9]', password) is None:
#            break
#        # special chars
#        if re.search(r'[~`! @#$%^&*()-+={\[}\]|:;\"\'<,>.?/]', password) is None:
#            break
#        return True
#    # loop has failed to complete, password invalid
#    return False

#loop above redundant; try:

def valid_password(password):
    return all([len(password) > 8, re.search(r'[a-z]', password),
    re.search(r'[A-Z]', password), re.search(r'[0-9]', password),
    re.search(r'[_~`! @#$%^&*()-+={\[}\]|:;\"\'<,>.?/]', password)])

if __name__ == '__main__':
    print(valid_password('Farguscassidy8'))