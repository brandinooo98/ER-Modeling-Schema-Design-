/*
Find the number of auctions belonging to exactly four categories.
*/

SELECT COUNT(itemID)
FROM
(
    SELECT itemID, COUNT(categoryID) AS COUNT
    FROM LineItem GROUP BY itemID
)
WHERE COUNT = 4;