/*
Find the number of users from New York (i.e., users whose location is the string "New York").
*/
SELECT COUNT(*)
FROM Seller, Location
WHERE Seller.locationID = Location.locationID
AND Location.location = "New York";