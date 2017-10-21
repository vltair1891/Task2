import requests
import json
import os
import msvcrt as m


data = {'customerID': 'fixer',
        'action': 'getScore',
        'uuid': 'QA_Test_36YQ4WRR',
        'customerSessionID': 'AB88KTM0IQUTYZH'}
#url = 'https://api.bcqa.bc2.customers.biocatch.com/api/v6/score?'
url = 'https://api.bcqa.bc2.customers.biocatch.com/api/v6/score?/'
request = requests.get(url, data)
response = request.text
def IsValid(response):
  try:
    print ("Valid response recieved/n {0}".format(response))
  except ValueError:
    print ("Invalid responce recieved")


 # Function for waiting for key press
def wait():
    m.getch()

 # Clear screen before to show menu, cls is MS Windows command
os.system('cls')

ans=True
while ans:
    print("""
    Test menu:
    ------------

    1.Positive Test - > Valid response recieved
    2.Negative Test - > Wrong customerSessionID
    3.Positive Test - > Score bigger than 800
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\nPositive Test - > Valid response recieved initialized")
      IsValid(response)
      print (response)
      print(request.url)
      print(request.status_code)
      print("\nPress Enter...")
      wait()
      os.system('cls')
    elif ans=="2":
      print("\nNegative Test - > Wrong customerSessionID initialized")
      IsValid(response)
      print("\nPress Enter...")
      wait()
      os.system('cls')
    elif ans=="3":
      print("\nPositive Test - > Score bigger than 800 initialized")
      print("\nPress Enter...")
      wait()
      os.system('cls')
    elif ans=="4":
      print("\nGoodbye")
      ans = None
    else:
      print("\nNot Valid Choice Try again")
      print("\nPress Enter...")
      wait()
      os.system('cls')
      ans = True
