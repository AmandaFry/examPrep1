from system.core.controller import *

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
        
        return self.load_view('index.html')

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

