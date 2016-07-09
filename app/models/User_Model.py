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

            if len(loged_in_user) == 0:
                errors.append("User was not found, please register")
            elif not self.bcrypt.check_password_hash(loged_in_user[0]['password'], user_info['passw'])
                errors.append("Password is not valid")
                return {'status' : False, 'errors' : errors}
            else:
                return {'status' : True, 'user' : loged_in_user}


    def register_user(self, user_info):
        errors=[]
        success=[]

        # elif not NOSPACE_REGEX.match(user_info['passw']):
        #     errors.append("Please enter valid password")
        pass