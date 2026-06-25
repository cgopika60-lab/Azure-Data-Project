# Databricks notebook source
# ADLS access permission
storage_account = "strgazuredata04"
access_key = "<ACCESS_KEY_REMOVED>"

spark.conf.set(
    f"fs.azure.account.key.{storage_account}.dfs.core.windows.net",
    access_key
)

# COMMAND ----------

# read presentation data
presentation_df = spark.read.format("delta").load(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/drivers"
)

display(presentation_df)

# COMMAND ----------

# Team wise Driver count Analysis(1)      *To identify the number of drivers in each team*
from pyspark.sql.functions import count

team_analysis=presentation_df.groupBy("team_name") \
                             .agg(count("*").alias("driver_count")) \
                             .orderBy("driver_count",ascending=False)

display(team_analysis)

# COMMAND ----------

team_analysis.write \
.format("delta") \
.mode("overwrite") \
.save(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/team_analysis"
)

# COMMAND ----------

# save to csv format
team_analysis.write \
    .mode("overwrite") \
    .option("header",True) \
    .format("csv") \
    .save(
        "abfss://presentation@strgazuredata04.dfs.core.windows.net/team_analysis_csv"
    )

# COMMAND ----------

dbutils.fs.ls(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/team_analysis_csv"
)

# COMMAND ----------

# ***********************************************************************************************************************************************

# COMMAND ----------

# Drivers Name and Racing numbers Analysis  (2)    *To identify drivers and their official rracing numbers*

team_driver_list = presentation_df.select(
    "team_name",
    "full_name",
    "driver_number"
).orderBy("team_name", "driver_number")

display(team_driver_list)

# COMMAND ----------

team_driver_list.write \
.format("delta") \
.mode("overwrite") \
.save(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/team_driver_list"
)

# COMMAND ----------

# save to csv format
team_driver_list.write \
    .mode("overwrite") \
    .option("header",True) \
    .format("csv") \
    .save(
        "abfss://presentation@strgazuredata04.dfs.core.windows.net/team_driver_list_csv"
    )

# COMMAND ----------

dbutils.fs.ls(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/team_driver_list_csv"
)

# COMMAND ----------

# **********************************************************************************************************************************************

# COMMAND ----------

# Driver Profile Analysis (3)      *To create drivers profile containing their names, team names and profile image URLs*

driver_profile_analysis = presentation_df.select(
    "full_name",
    "team_name",
    "headshot_url"
).orderBy("team_name")

display(driver_profile_analysis)

# COMMAND ----------

driver_profile_analysis.write \
.format("delta") \
.mode("overwrite") \
.save(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/driver_profile_analysis"
)

# COMMAND ----------

# save to csv format
driver_profile_analysis.write \
    .mode("overwrite") \
    .option("header",True) \
    .format("csv") \
    .save(
        "abfss://presentation@strgazuredata04.dfs.core.windows.net/driver_profile_analysis_csv"
    )

# COMMAND ----------

dbutils.fs.ls(
    "abfss://presentation@strgazuredata04.dfs.core.windows.net/driver_profile_analysis_csv"
)