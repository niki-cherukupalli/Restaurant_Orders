USE restaurant_db;

-- 1. view the menu_items table.
SELECT * FROM menu_items;

-- 2. find the number of items in the table.
SELECT COUNT(*) FROM menu_items;

-- 3. what are the least and most expensive items on the menu?
SELECT * FROM menu_items
ORDER BY price ASC;

SELECT * FROM menu_items
ORDER BY price DESC;

-- 4. how many italian dishes are on the menu?
SELECT COUNT(*) FROM menu_items
WHERE category="Italian";

-- 5. what are the least and most expensive italian dishes on the menu?

SELECT * FROM menu_items
WHERE category="Italian"
ORDER BY price;

SELECT * FROM menu_items
WHERE category="Italian"
ORDER BY price DESC;

-- 6. how many dishes are in each category?
SELECT category, COUNT(menu_item_id) AS num_dishes
FROM menu_items
GROUP BY category;

-- 7. what is the average dish price within each category?
SELECT category, AVG(price) AS avg_price
FROM menu_items
GROUP BY category;

