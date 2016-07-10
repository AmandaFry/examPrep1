from system.core.model import Model
from flask import Flask, session
from datetime import datetime
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')
PW_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?\d)[A-Za-z\d]{8,}$')

class Travel_Model(Model):
    def __init__(self):
        super(Travel_Model, self).__init__()

    def add_trip(self, trip_info):
        erorrs = []

        today = datetime.now().strftime("%Y-%m-%d")

        if len(trip_info['destination']) < 2:
            erorrs.append("Please enter a valid destination")
        elif len(trip_info['plan']) < 2:
            erorrs.append("Please enter a valid description")
        elif today > trip_info['start_date']:
            erorrs.append("Start date must be in the future")
        elif today > trip_info['end_date']:
            erorrs.append("End date must be in the future")
        elif trip_info['start_date'] >= trip_info['end_date']:
            erorrs.append("Start date must be before end date")
        if erorrs:
            return {"status": False, "errors": erorrs}
        else:
            query = "INSERT INTO trips (tripOrganizer_id, destination, plan, start_date, end_date, created_at, updaetd_at) VALUES (:organizer_id, :destination, :plan, :start_date, :end_date, NOW(), NOW())"
            data = {
                'organizer_id': session['id'], 
                'destination': trip_info['destination'],
                'plan' : trip_info['plan'],
                'start_date' : trip_info['start_date'],
                'end_date' : trip_info['end_date'] 
            }
            self.db.query_db(query, data)
            return {"status": True}

    def my_trips(self):
        pass

    def joined_trips(self):
        pass

    def others_trips(self):
        pass

