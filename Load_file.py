#PySpark automatically creates the SparkContext object named sc in the PySpark shell.

# Create a Python list of numbers from 1 to 100 
numb = range(1, 100)

# Load the list into PySpark  
spark_data = sc.parallelize(numb)

# Load a local file into PySpark shell
lines = sc.textFile(file_path)

