from system.core.model import Model
from flask import Flask, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')

class User_Model(Model):
    def __init__(self):
        super(User_Model, self).__init__()

    def login_user(self, user_info):
        # to collect error messages
        errors=[]
        if len(user_info['email']) < 2 or len (user_info['passw']) < 2:
            errors.append("Email and/or password is too short")
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append("Please enter valid email format")
        if errors:
            return {'status' : False, 'errors' : errors}
        else:
            query = "SELECT * FROM users WHERE email = :email"
            data = {'email' : user_info['email']}
            loged_in_user = self.db.query_db(query,data) #run query and assign to varuable 
            print ('$' * 25)
            print loged_in_user
            print ('$' * 25)
            
            if len(loged_in_user) == 0:
                errors.append("User was not found, please register")
            elif not self.bcrypt.check_password_hash(loged_in_user[0]['password'], user_info['passw']):
                errors.append("Password is not valid")
                return {'status' : False, 'errors' : errors}
            else:
                return {'status' : True, 'user' : loged_in_user}


    def register_user(self, user_info):
        errors=[]
        success=[]

        if len(user_info['f_name']) < 2:
            errors.append("First name cannot be empty")
        elif not NOSPACE_REGEX.match(user_info['f_name']):
            errors.append("Please enter a valid first name")
        elif len(user_info['l_name']) < 2 :
            errors.append("Last name cannot be empty")
        elif not NOSPACE_REGEX.match(user_info['f_name']):
            errors.append("Please enter a valid last name")
        elif len(user_info['email']) < 2 :
            errors.append("Email cannot be empty")
        elif not EMAIL_REGEX.match(user_info['email']):
            errors.append("Please enter a valid email format")
        elif not PW_REGEX.match(user_info['passw']):
            errors.append("Please enter a valid password. It must be 8 charater long, at must include least one upper case and number")
        elif len(user_info['conf_passw']) < 2 :
            errors.append("Confirm password cannot be empty")
        elif not (user_info['passw'] == user_info['conf_passw']):
            errors.append("Password and confirm password must match")   
      
        if errors:
            return {"status": False, "errors": errors}
        else:
            #check to see if email already in use
            query = "SELECT * FROM users WHERE email = :email"
            data = {'email': user_info['email']}
            email_inuse = self.db.query_db(query, data)

            if email_inuse:
                errors.append("Email account already in use")
                return {"status": False, "errors": errors}
            else:
                query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:f_name, :l_name, :email, :passw, NOW(), NOW())"

                password = user_info['passw']
                hashed_pw = self.bcrypt.generate_password_hash(password)
                data = {
                    'f_name':user_info['f_name'],
                    'l_name':user_info['l_name'],
                    'email':user_info['email'],
                    'passw':hashed_pw,
                }
                registered_user = self.db.query_db(query, data)
                print ('%' * 25)
                print registered_user
                print ('%' * 25)
                return {"status": True }
                

    