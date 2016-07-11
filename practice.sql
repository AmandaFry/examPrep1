USE tfprac1;

SELECT * FROM users;

SELECT * FROM trips;

SELECT * FROM trip_friends;

SELECT * FROM trips WHERE tripOrganizer_id = 3;

SELECT * FROM trips WHERE id = 8;

SELECT users.first_name, users.last_name, trips.destination, trips.plan, trips.start_date, trips.end_date FROM users
JOIN trips
ON users.id = trips.tripOrganizer_id
WHERE trips.id = 8;

SELECT * FROM trips WHERE tripOrganizer_id != 2;

SELECT users.first_name, users.last_name, trips.destination, trips.plan, trips.start_date, trips.end_date FROM users
JOIN trips
ON users.id = trips.tripOrganizer_id
WHERE trips.tripOrganizer_id != 2;

INSERT INTO trip_friends (trips_id, friends_id, created_at, updated_at) VALUES (1, 2, NOW(), NOW());



SELECT trips.id, trips.destination, trips.start_date, trips.end_date, trips.plan FROM trips
JOIN trip_friends 
ON trips.id = trip_friends.trips_id
WHERE trip_friends.friends_id = 2
OR trips.tripOrganizer_id = 2;


SELECT * FROM trips WHERE tripOrganizer_id = 2;
SELECT * FROM trip_friends WHERE friends_id = 2;

USE tfprac1;

SELECT trips.id, trips.tripOrganizer_id, trips.destination, trips.start_date, trips.end_date, trips.plan, trip_friends.trips_id, trip_friends.friends_id FROM trips
JOIN trip_friends 
ON trips.id = trip_friends.trips_id
WHERE trips.tripOrganizer_id = 2
OR trip_friends.friends_id = 2;


SELECT trips.id, trips.tripOrganizer_id, trips.destination, trip_friends.trips_id, trip_friends.friends_id FROM trips
JOIN trip_friends 
ON trips.id = trip_friends.trips_id
WHERE trips.tripOrganizer_id = 2;
-- trips.tripOrganizer_id = 2;
-- OR trip_friends.friends_id = 2

SELECT * FROM users;

SELECT * FROM trips;

SELECT * FROM trip_friends;

SELECT * FROM trips WHERE tripOrganizer_id = 2;
SELECT * FROM trip_friends WHERE friends_id = 2;