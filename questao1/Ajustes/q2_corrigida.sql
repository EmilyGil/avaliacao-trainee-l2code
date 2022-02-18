SELECT categories.id, categories.name AS "categories", SUM(orders_products.units_sold) AS "sum" 
FROM ((categories 
	  INNER JOIN products ON categories.id = products.id_categories) 
	  INNER JOIN orders_products ON products.id = orders_products.product_id) 
	  GROUP BY categories.id
	  ORDER BY "sum" DESC LIMIT 4;