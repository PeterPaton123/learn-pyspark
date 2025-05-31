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

4. **Install Docker **
   ```bash
   sudo snap install docker
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
