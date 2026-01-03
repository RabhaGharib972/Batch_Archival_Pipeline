# 📦 Batch Archival Data Pipeline
## PostgreSQL → Spark Batch → Parquet → HDFS

This project implements a **production-style batch archival data pipeline** that extracts operational data from PostgreSQL, processes it using Apache Spark batch jobs, and stores it as partitioned Parquet files in HDFS for long-term storage and analytics.

This pipeline represents **Phase 2** of a larger data engineering system, following a real-time streaming ingestion layer.

---

## 🧠 Architecture Overview

PostgreSQL (Operational Data)  
↓  
Apache Spark Batch Job  
↓  
Parquet Files (Partitioned by Date)  
↓  
HDFS (Archive / Data Lake Layer)

---

## 🎯 Project Objectives

- Archive operational data for historical analysis
- Convert relational data into optimized columnar format
- Improve query performance using partitioning
- Simulate enterprise-grade batch processing workflows
- Prepare data for analytics and reporting


### Architecture Diagram


![Pipeline Architecture](screenshots/pipeline-architecture.png)



---

## 🔧 Technologies Used

- PostgreSQL – Source operational database
- Apache Spark – Batch processing engine
- Parquet – Columnar storage format
- HDFS – Distributed file system
- Linux VM – Execution environment

---

## 📂 Repository Structure

```text
.
├── spark_batch_postgres_to_hdfs.py
├── README.md
├── screenshots/
│   ├── pipeline-architecture.png
│   ├── ShowData.png
│   ├── CountRecords.png
│   ├── Partitioning.png
└── .gitignore
```

## ⚙️ Execution Steps

### 1️⃣ Ensure HDFS Is Running

```javascript
jps

```
##### Expected output:

```javascript
NameNode
DataNode
```

##### If HDFS is not running:

```javascript
start-dfs.sh
```
### 2️⃣ Create Archive Directory in HDFS

```javascript
hdfs dfs -mkdir -p /archive/randomuser
```
### 3️⃣ Run Spark Batch Job

```javascript
spark-submit \
--jars postgresql-42.2.18.jar \
spark_batch_postgres_to_hdfs.py
```
This job performs the following actions:

Reads data from PostgreSQL using JDBC

Adds a load_date column

Writes partitioned Parquet files into HDFS

### 4️⃣ Verify Data in HDFS

```javascript
hdfs dfs -ls /archive/randomuser/parquet
```
##### Expected output:

```javascript
_SUCCESS
load_date=YYYY-MM-DD/
```
### ✅ Data Validation

```javascript
spark-shell
```

```javascript
val df = spark.read.parquet("hdfs://localhost:9000/archive/randomuser/parquet")
df.show(10, false)
df.count()
df.select("load_date").distinct().show()
```
This confirms:

    1. Data integrity

    2. Correct schema inference

    3. Proper partitioning by load date


## 🛡️ Design Considerationsy

Parquet format improves storage efficiency and query performance.


Date-based partitioning enables faster filtering and pruning.


Explicit HDFS URI avoids filesystem ambiguity.


Batch jobs are designed to be scheduler-ready for orchestration. tools












## Author

- [@Rabha Gharib](https://github.com/RabhaGharib972)

