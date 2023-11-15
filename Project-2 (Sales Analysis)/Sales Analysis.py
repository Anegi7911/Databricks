# Databricks notebook source
# DBTITLE 1,Files location in dbfs
# /FileStore/tables/sales_csv-1.txt
# /FileStore/tables/menu_csv.txt

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

# COMMAND ----------

schema = StructType(
    [
        StructField("product_id", IntegerType(), True),
        StructField("customer_id", StringType(), True),
        StructField("order_date", DateType(), True),
        StructField("location", StringType(), True),
        StructField("source_order", StringType(), True),
    ]
)

sales_df = (
    spark.read.format("csv")
    .option("inferschema", "true")
    .schema(schema)
    .load("/FileStore/tables/sales_csv-1.txt")
)

sales_df.show()

# COMMAND ----------

# DBTITLE 1,Adding year/month/quater
sales_df = sales_df.withColumn("Order_Year",year(sales_df.order_date)).withColumn("Order_month",month(sales_df.order_date)).withColumn("Order_quarter",quarter(sales_df.order_date))

sales_df.show()

# COMMAND ----------

# DBTITLE 1,Menu Data
menu_schema = StructType([
    StructField("product_id",IntegerType(),True),StructField("product_name",StringType()
    ,True),StructField("price",StringType(),True),
])

menu_df = spark.read.format("csv").option("inferschema","true").schema(menu_schema).load("/FileStore/tables/menu_csv.txt")

menu_df.show()

# COMMAND ----------

# DBTITLE 1,Total amount spend by each customer
total_amount_spend = sales_df.join(menu_df,'product_id').groupBy('customer_id').agg({'price':'sum'}).orderBy('customer_id')
total_amount_spend.show()

# COMMAND ----------

total_amount_spend.show()

# COMMAND ----------

# DBTITLE 1,Total amount spend by each category
total_amount_spend_category = sales_df.join(menu_df,'product_id').groupBy('product_name').agg({'price':'sum'}).orderBy('product_name')
total_amount_spend_category.show()

# COMMAND ----------

# DBTITLE 1,Total amount of sales in each month 
total_amt_sales_mtd = sales_df.join(menu_df,'product_id').groupBy('order_year','order_month').agg({'price':'sum'}).alias('price').orderBy('order_year','order_month')

total_amt_sales_mtd.show()

# COMMAND ----------

# DBTITLE 1,sales by quarter
total_ytd_sales = sales_df.join(menu_df,'product_id').groupBy('order_quarter').agg({'price':'sum'}).orderBy('order_quarter')
total_ytd_sales.show()

# COMMAND ----------

# DBTITLE 1,how many times each product is purchased
times_product_purchased = sales_df.join(menu_df,'product_id').groupBy('product_id','product_name').agg(count('product_id').alias('product_count')).orderBy('product_count',ascending=0)
times_product_purchased.show()

# COMMAND ----------

# DBTITLE 1,frequency of customer visited
sales_df.select(sales_df.source_order).distinct().show()

frequency_of_customer_visited = sales_df.filter(sales_df.source_order=='Restaurant').groupBy('customer_id').agg({'order_date':'count'})



frequency_of_customer_visited.show()

# COMMAND ----------

# DBTITLE 1,total sales by each country
total_sales_country = sales_df.join(menu_df,'product_id').groupBy('location').agg({'price':'sum'})
total_sales_country.show()

# COMMAND ----------

# DBTITLE 1,total sales by order_source
total_sales_order_source = sales_df.join(menu_df,'product_id').groupBy('source_order').agg(sum('price').alias('sales'))
total_sales_order_source.show()

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


