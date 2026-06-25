# Databricks notebook source
# ADLS access permission
storage_account = "strgazuredata04"
access_key = "<ACCESS_KEY_REMOVED>"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    access_key
)

# COMMAND ----------

# container access verifying
dbutils.fs.ls(
    "abfss://ingested@strgazuredata04.dfs.core.windows.net/"
)

# COMMAND ----------

df = spark.read.format("delta").load("abfss://ingested@strgazuredata04.dfs.core.windows.net/drivers")

display(df)

# COMMAND ----------

# Remove Duplicates
df = df.dropDuplicates()

# COMMAND ----------

# Create Derived Column
from pyspark.sql.functions import upper
df = df.withColumn(
    "team_name_upper",
    upper("team_name")
)
df.display()

# COMMAND ----------

# Save to Presentation Layer
df.write \
.format("delta") \
.mode("overwrite") \
.save(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/drivers"
)

# COMMAND ----------

presentation_df = spark.read.format("delta").load(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/drivers"
)

display(presentation_df)