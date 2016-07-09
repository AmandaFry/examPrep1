"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Travel(Controller):
    def __init__(self, action):
        super(Travel, self).__init__(action)
        self.load_model('Travel_Model')

   
    def dashboard(self):
        return self.load_view('dashboard.html')

