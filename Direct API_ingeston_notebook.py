# Databricks notebook source(This notebook is intended to run in Azure Databricks)
# ADLS access permission
storage_account = "strgazuredata04"
access_key = "<ACCESS_KEY_REMOVED>"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    access_key
)

# COMMAND ----------

# Read Data from OpenF1 API
import requests
url = "https://api.openf1.org/v1/drivers?session_key=latest"
data = requests.get(url).json()
print(f"Records fetched: {len(data)}")

# COMMAND ----------


# import pandas as pd
# pdf = pd.DataFrame(data)
# pdf["country_code"] = pdf["country_code"].fillna("Unknown")
# df = spark.createDataFrame(pdf)
# display(df)

# Convert JSON to Spark Dataframe
import pandas as pd
pdf = pd.DataFrame(data)
pdf = pdf.fillna("")
df = spark.createDataFrame(pdf)
display(df)

df.printSchema()
# print(type(data))
# print(len(data))
# print(data[0])

# COMMAND ----------

# save to raw layer
df.write \
.mode("overwrite") \
.json(
    "abfss://raw@strgazuredata04.dfs.core.windows.net/drivers_api"
)

# COMMAND ----------

# container access verifying
dbutils.fs.ls(
    "abfss://raw@strgazuredata04.dfs.core.windows.net/"
)

# COMMAND ----------

# save to delta(to ingested layer)
df.write \
.format("delta") \
.mode("overwrite") \
.save("abfss://ingested@strgazuredata04.dfs.core.windows.net/drivers")

# COMMAND ----------

# read from delta
ingested_df = spark.read.format("delta") \
.load("abfss://ingested@strgazuredata04.dfs.core.windows.net/drivers")

display(ingested_df)


# container check
dbutils.fs.ls(
    "abfss://ingested@strgazuredata04.dfs.core.windows.net/"
)