
import pandas as panda

#load the csv files
order_products_csv = panda.read_csv("order_products__train.csv")
products_csv = panda.read_csv("products.csv")

order_product_merged = order_products_csv.merge(products_csv, on= "product_id")

product_order_rank = order_product_merged['product_name'].value_counts()
product_order_rank.columns = ['product name', 'counts']
#recommend the top 20 most purchased products
recommendations = product_order_rank.head(20)

print(recommendations)
