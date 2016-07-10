from system.core.controller import *
from flask import Flask, flash, session

class Travel(Controller):
    def __init__(self, action):
        super(Travel, self).__init__(action)
        self.load_model('Travel_Model')
   
    def dashboard(self):
        my_trips = self.models['Travel_Model'].my_trips()
        joined_trips = self.models['Travel_Model'].joined_trips()
        others_trips = self.models['Travel_Model'].others_trips()
        return self.load_view('dashboard.html' my_trips=my_trips, joined_trips=joined_trips, others_trips=others_trips)

    def newplan(self):
        return self.load_view('newplan.html')

    def add_trip(self):
        trip_info = {
            'destination' : request.form['destination'],
            'plan' : request.form['plan'],
            'start_date' : request.form['start_date'],
            'end_date' : request.form['end_date']
        }

        new_trip = self.models['Travel_Model'].add_trip(trip_info)

        if new_trip['status'] == False:
            flash(message)
            return self.load_view('newplan.html')
        else:
            return redirect ('/dashboard')

