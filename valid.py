#All functions which will validate user input go into here. 
def mainValid(choice):
  if choice == 1 or choice == 2:
    return True 
  else:
    return False

def mainMenuValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
    return True 
  else: 
    return False