/*
Find the number of users in the database.
*/
SELECT COUNT(*)
FROM
(
    SELECT userID FROM Seller
    UNION
    SELECT userID FROM Bidder
);