use tfprac1;

SELECT * FROM users;

SELECT * FROM trips;

SELECT * FROM trip_friends;

SELECT users.first_name, trips.tripOrganizer_id, trips.destination FROM trips
RIGHT JOIN users
on users.id = trips.tripOrganizer_id;
-- WHERE trips.tripOrganizer_id = 2;


SELECT users.first_name, trip_friends.trips_id, trips.destination FROM trip_friends
RIGHT JOIN users
ON users.id = trip_friends.friends_id
JOIN trips
ON trips.id = trip_friends.trips_id
WHERE trip_friends.friends_id = 2;
-- WHERE trips.tripOrganizer_id = 2
-- or trips.tripOrganizer_id = 2

-- show every trips and joined trips
SELECT * FROM trips
LEFT JOIN trip_friends ON trips.id = trip_friends.trips_id;


SELECT * FROM trips
LEFT JOIN trip_friends ON trips.id = trip_friends.trips_id
WHERE trips.tripOrganizer_id = 2 OR trip_friends.friends_id =2;

SELECT * FROM trips
LEFT JOIN trip_friends ON trips.id = trip_friends.trips_id
WHERE trips.tripOrganizer_id != 2 AND trip_friends.friends_id !=2;

SELECT * FROM trips
WHERE trips.id NOT IN (SELECT trips.id FROM trips
LEFT JOIN trip_friends ON trips.id = trip_friends.trips_id
WHERE trips.tripOrganizer_id = 2 OR trip_friends.friends_id =2);

SELECT * FROM users
JOIN trips ON users.id = trips.tripOrganizer_id
WHERE trips.id NOT IN (SELECT trips.id FROM trips
LEFT JOIN trip_friends ON trips.id = trip_friends.trips_id
WHERE trips.tripOrganizer_id = 2 OR trip_friends.friends_id =2);

SELECT * FROM users
JOIN trips ON users.id = trips.tripOrganizer_id;

SELECT users.first_name, users.last_name, trips.id, trips.tripOrganizer_id, trips.destination, trips.plan, trips.start_date, trips.end_date FROM users JOIN trips ON users.id = trips.tripOrganizer_id 
