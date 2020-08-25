# Evaluates the strength of an example password based on its upper-case letters, lower-case letters and numbers it contains
# and provides it with a "score" of Horrible, Weak, Medium or Strong

import re

def evaluate_password(pwd):
   password_scores = {0:'Horrible', 1:'Weak', 2:'Medium', 3:'Strong'}
    password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)
    if re.search(r'[A-Z]', pwd):
        password_strength['has_upper'] = True
    if re.search(r'[a-z]', pwd):
        password_strength['has_lower'] = True
    if re.search(r'[0-9]', pwd):
        password_strength['has_num'] = True
    score = len([b for b in password_strength.values() if b])
    return password_scores[score]

if __name__ == '__main__':
    print ('Enter a password\n\nThe password must be at least 8 charecters long.\n')
    while True:
        password = input('Password: ')
        if 8 <= len(password) < 120:
            break
        print ('The password must be at least 8 charecters long.\n')
    print ('Password is %s' % evaluate_password(password))   