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

    def join_trip(self, id):
        query = "INSERT INTO trip_friends (trips_id, friends_id, created_at, updated_at) VALUES (:trip_id, :friends_id, NOW(), NOW())"
        data = {'trip_id' : id, 'friends_id' : session['id']}
        join_trip = self.db.query_db(query, data)
        return {"status": True}

    def my_trips(self):
        query = "SELECT * FROM trips WHERE tripOrganizer_id = :id"
        data = { 'id' : session['id']}
        my_trips= self.db.query_db(query,data)
        return (my_trips)

    def joined_trips(self):
        query = "SELECT * FROM trip_friends WHERE friends_id = :id"
        data = { 'id' : session['id']}
        joined_trips = self.db.query_db(query,data)
        return 

    def others_trips(self):
        # query = "SELECT * FROM trips WHERE tripOrganizer_id != :id" #not showing the user name, but correct partial info
        query = "SELECT users.first_name, users.last_name, trips.id, trips.tripOrganizer_id, trips.destination, trips.plan, trips.start_date, trips.end_date FROM users JOIN trips ON users.id = trips.tripOrganizer_id WHERE trips.tripOrganizer_id != :id"
        data = { 'id' : session['id']}
        others_trips = self.db.query_db(query,data)
        return (others_trips)

    def trip_detail(self, id):
        query = "SELECT users.first_name, users.last_name, trips.destination, trips.plan, trips.start_date, trips.end_date FROM users JOIN trips ON users.id = trips.tripOrganizer_id WHERE trips.id = :id"
        data = {'id' : id}
        trip_detail = self.db.query_db(query, data)
        return (trip_detail)

