/*
Find the number of categories that include at least one item with a bid of more than $100.
*/
SELECT COUNT(DISTINCT Category.categoryID)
FROM Category, LineItem
WHERE Category.categoryID = LineItem.categoryID
AND LineItem.itemID IN
(SELECT Bid.itemID
FROM Bid
WHERE CAST(Bid.amount AS DOUBLE) > 100.);