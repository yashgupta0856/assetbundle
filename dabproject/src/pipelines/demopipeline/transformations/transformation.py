from pyspark import pipelines as dp
from pyspark.sql.functions import *
from pyspark.sql.types import *

@dp.table()
def data():
    return spark.range(10)