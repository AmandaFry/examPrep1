from system.core.controller import *
from flask import Flask, session, flash

class User(Controller):
    def __init__(self, action):
        super(User, self).__init__(action)
        self.load_model('User_Model')

    def index(self):
        #index is still needed for inital page load
        return self.load_view('index.html')

    def login(self):
        user_info = {
            'email' : request.form['email'],
            'passw' : request.form['passw']
        }
        user_login = self.models['User_Model'].login_user[user_info]
        
        if user_login['status']  == False:
            #return to logon page and show errors
            if message in user_login['errors']:
                flash(message)
            return self.load_view('index.html')
        else:
            #login and store name and I in session
            session['id'] = user_login['user']['id']
            session['name'] = user_login['user']['f_name'] + ' ' + user_login['user']['l_name']
            return redirect('/dashboard')
            #return self.load_view('dashboard.html')

    def register(self):
        user_info = {
            'f_name' : request.form['f_name'],
            'l_name' : request.form['l_name'],
            'email' : request.form['email'],
            'password' : request.form['passw'],
            'conf_passw' : request.form['conf_passw']
        }

        user_register = self.models['User_Model'].register_user[user_info]

        return self.load_view('index.html')

    def logout(self):
        session.clear()
        return redirect('/')