/*
Find the number of sellers whose rating is higher than 1000.
*/

SELECT COUNT(*)
FROM Seller 
WHERE rating > 1000;