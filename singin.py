# Take data from your users
print ('Create your new account ')
user_name = input('Enter your user name: ')
password = input('Enter your password: ')
mobile = input('Enter your mobile number: ')
print('You are successfully create your account, Please login here: ')

# Store data which user input us and create account
User_data_name = user_name
User_data_password = password
User_data_mobile = mobile

# Login account
login_user= input('User name or Mobile number:  ')
login_password = input('Password: ')

# Main function which controlling all data.
if login_user == User_data_name and login_password == User_data_password:
    print('You are successfully login.' )
else:
    print('Something went wrong, please try again')
