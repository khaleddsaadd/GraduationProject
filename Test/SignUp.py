import pyrebase

#Configure and Connext to Firebase

firebaseConfig = {'apiKey': "AIzaSyD3SaqfyUcu1Xnjkeaqw3ILpn_w4v5s4Fo",
  'authDomain': "pruney-4e073.firebaseapp.com",
  'databaseURL':"https://pruney-4e073.firebaseapp.com",
  'projectId': "pruney-4e073",
  'storageBucket': "pruney-4e073.appspot.com",
  'messagingSenderId': "969307424804",
  'appId': "1:969307424804:web:f6706080c47108567430b1",
  'measurementId': "G-FQRT3VDG5B"}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#Login function

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']
       # print(email)
    except:
        print("Invalid email or password")
    return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

#Main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()