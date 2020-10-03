SELECT COUNT(*) 
FROM User, Location
WHERE User.locationID = Country.locationID
AND Location.location = 'New York';  