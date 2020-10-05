/*
Find the ID(s) of auction(s) with the highest current price.
*/

SELECT itemID
FROM item
WHERE currently=(SELECT currently from item ORDER BY currently DESC LIMIT 1);