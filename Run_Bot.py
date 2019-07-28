# Ahriman

from bot_insta import *


doc = ''' 
      Add User and Login= Enter----( 1 )
      #Login User = Enter----------( - )
      Likes Automatic = Enter------( 3 )
      Exit Browser = Enter---------( 4 )
      Exit the App = Enter---------( 5 )
'''

def Add():
    usname = input('Enter user name :')
    pas = input('Enter password :')
    with open('UserName.txt' , 'w') as f:
        f.write(usname)
        f.write('\n') 
        f.write(pas)           
    # USER = {1 : usname , 2 : pas}
    # with open('UserName.txt' , 'r') as f:
    #     g = f.readline()
    #     h = f.readline()
    # bot.Instagram_Bot(g,h)
    Login()

    
def Login():
    with open('UserName.txt' , 'r') as f:
        g = f.readline()
        h = f.readline()
    item = Instagram_Bot(g,h)
    item.Login_bot()
    Doc()

def Like_Ato():
    Likes_Automatic_Following_bot()
    Doc()
       
        



def Doc():
    print(doc)
    x = int(input('Select one item from above :'))
    if x == 1:
        Add()
    elif x == 3:
        pass
    else:
        Doc()
    # elif x == 3:
    #     Doc()
    # elif x == 4:
    #     pass
    # elif x == 5:
    #     pass

Doc()