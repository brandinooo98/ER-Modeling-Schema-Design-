/*
Find the number of categories that include at least one item with a bid of more than $100.
*/

SELECT COUNT(*)
FROM
(
SELECT lineItem, item
WHERE lineItem.itemID = item.itemID AND currently > 100
);