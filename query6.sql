/*
Find the number of users who are both sellers and bidders.
*/

SELECT COUNT(*)
FROM
(
    SELECT userID FROM Seller
    INTERSECT
    SELECT userID FROM Bidder
);