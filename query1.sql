/*
Find the number of users in the database.
*/
SELECT 
(SELECT COUNT(*) FROM Seller) +
(SELECT COUNT(*) FROM Bidder);