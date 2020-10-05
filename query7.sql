/*
Find the number of categories that include at least one item with a bid of more than $100.
*/
SELECT COUNT(Category.categoryID)
FROM Category, LineItem, Bid
WHERE Category.categoryID = LineItem.categoryID
AND LineItem.itemID IN 
    (SELECT Bid.itemID
    FROM Bid
    WHERE Bid.amount > 100);