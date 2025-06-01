# Installation Instructions

1. **Install Poetry (Python Dependency Manager)**  
   ```bash
   pip install poetry
   ```

2. **Install Invoke**  
   ```bash
   pip install invoke
   ```

3. **Install Java (OpenJDK 11) & Set JAVA_HOME**  
   ```bash
   sudo apt-get update
   sudo apt-get install openjdk-17-jdk
   echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
   echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
   source ~/.bashrc
   ```
*Adjust `JAVA_HOME` if your Java path differs.

# Parallel GPU Processing using Nvidia RAPIDs Accelerator for PySpark

4. **CUDA Toolkit**
   ```bash
   sudo apt install nvidia-cuda-toolkit
   ```

5. **Download the cuDF Jar**

   This is a GPU-accelerated DataFrame library (written in C++/CUDA, with a Java wrapper). It provides low-level, columnar data processing on the GPU for Spark.
   Find CUDA version:
   ```
   nvcc --version
   ```
   Find the right version from the Maven central repository: https://repo1.maven.org/maven2/ai/rapids/cudf/25.04.0/
   For example
   ```
   wget https://repo1.maven.org/maven2/ai/rapids/cudf/25.04.0/cudf-25.04.0-cuda12.jar
   ```
   
6. **Download the JARs for RAPIDS accelerator for PySpark**

   This is a Spark plugin that integrates with Spark SQL/Catalyst. It rewrites Spark’s execution plans to use GPU (cuDF) operations where supported, delegating suitable Spark SQL/DataFrame operations to the GPU via cuDF.

   From https://nvidia.github.io/spark-rapids/docs/download.html, find installed Scala version with
   ```
   inv startdev
   ls .venv/lib/python3.12/site-packages/pyspark/jars/ | grep scala
   ```
   Expected Scala version for PySpark <4.0.0 is 2.12
   ```
   wget https://repo1.maven.org/maven2/com/nvidia/rapids-4-spark_2.12/25.04.0/rapids-4-spark_2.12-25.04.0.jar
   ```
   You may want to move these jars to a separate directory:
   ```
   cd 
   mkdir rapids_jars/
   mv *.jar rapids_jars/
   ```

# Start Developer Environment

```inv startdev```

# Notebook to .py

Generate .py files from notebooks with

```
   cd src/
   poetry run jupytext --to py:percent notebook.ipynb
```

# Execute
To run Python files:

```inv run filename.py```

To run notebooks, select .venv as the Kernel.

Investigate the execution plan by clicking on the localhost link output after a SparkSession is initialised and go to the SQL/DataFrame tab.
