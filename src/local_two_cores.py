# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
from pyspark.sql import SparkSession
from pyspark.rdd import RDD

import os

print(os.getenv("JAVA_HOME"))

# %%
spark: SparkSession = SparkSession.builder \
    .appName("Parallel Array Processing") \
    .master("local[2]") \
    .getOrCreate()
sc = spark.sparkContext
print(f"Monitor cluster at: {sc.uiWebUrl}")

# %%
data = [1, 2, 3, 4, 5]
rdd: RDD[int] = sc.parallelize(data)
result = rdd.map(lambda x: x * 2).collect()
print(result)  # Output: [2, 4, 6, 8, 10]

# %%
spark.stop()
