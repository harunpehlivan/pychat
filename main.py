import os, time
from replit import db
from colors import colors

def clear():
  os.system('clear')

login_signup = True
while login_signup:
  clear()
  print('[ --- PyChat Homepage --- ]\n\n')
  print('[1] Login\n[2] Sign Up')
  print()
  ls = input('>>> ')
  clear()

  if ls == '1':
    print('[ --- PyChat Login --- ]\n\n')
    username = input("Username: ")
    password = input('Password: ')
    clear()

    try:
      PASSWORD = db[username]

      if PASSWORD == password:
        print('[ --- PyChat Login --- ]\n\nYou are now Logged in.')#colors
        time.sleep(2)
        clear()
        login_signup = False
      else:
        print('\033[1;31;20mUsername or Password is incorrect, or it does not exist. Please try again.\033[0;37;20m')
        time.sleep(2)

    except:
      print('\033[1;31;20mUsername or passwrod is incorrect, or it does not exist. Please try again.\033[0;37;20m')
      time.sleep(2)

  elif ls == '2':
    print('[ --- PyChat Sign Up --- ]\n\n')
    new_username = input("Create a Username: ")
    new_password = input("Create a Password: ")
    clear()

    try:
      db[new_username] = new_password
      print(f'Welcome, {new_username}, to PyChat! You can now login with your new username and password.')
      time.sleep(2)
    except:
      print('\033[1;31;20mThat username has already been taken.\033[0;37;20m')
      time.sleep(2)

  else:
    print('\033[1;31;20mInvalid entry. Please try again.\033[0;37;20m')
    time.sleep(2)

with open('database.txt','a') as file:
  file.write(f'<PyBot> {username} is online.\n')
  file.close()

chatting = True
while chatting:
  print('[ --- PyChat --- ]')
  file = open('database.txt','r')
  print(file.read())
  
  message = input('\nMessage:\n>>> ')
  clear()

  if message == 'quit':
    chatting = False
    with open('database.txt','a') as file:
      file.write(f'<PyBot> {username} has logged out.\n')
      file.close()
  else:
    with open('database.txt','a') as file:
      file.write(f'[{username}] '+message+'\n')
      file.close()