import random
import getpass

words = getpass.getpass('The jumble is:')

random.shuffle(words)
if True:
    print(words)
else:
    print('try again')
