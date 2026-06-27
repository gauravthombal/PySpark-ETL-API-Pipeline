# 🚀 PySpark ETL API Pipeline

## 📌 Project Overview

This project demonstrates an **End-to-End ETL (Extract, Transform, Load) Pipeline** built using **PySpark**. The pipeline extracts product data from the **DummyJSON API**, performs data cleaning and transformation using PySpark, and stores the processed data in both **CSV** and **Parquet** formats.

The project follows a real-world Data Engineering workflow and showcases how API data can be transformed into analytics-ready datasets.

---

## 🏗️ Architecture

> Place your architecture diagram inside the `images` folder.

```text
images/
└── architecture.png
```

Then display it using:

```markdown
![Architecture](images/architecture.png)
```

---

## 🔄 ETL Workflow

```
DummyJSON API
        │
        ▼
Extract API Data
        │
        ▼
Raw JSON (products.json)
        │
        ▼
PySpark Transformations
        │
        ├── Remove Duplicates
        ├── Handle Null Values
        ├── Rename Columns
        ├── Select Required Columns
        └── Data Cleaning
        │
        ▼
Processed Data (CSV)
        │
        ▼
Parquet Files
```

---

## 📂 Project Structure

```
PySpark-ETL-API-Pipeline/
│
├── data/
│   ├── raw/
│   │   └── products.json
│   
│   └── parquet/
│
├── notebooks/
│   └── PySpark_ETL_API_Pipeline.ipynb
│
├── src/
│   ├── extract.py
│
├── images/
│   └── architecture.png
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Technologies Used

* Python
* PySpark
* Apache Spark
* DummyJSON API
* JSON
* CSV
* Parquet
* Google Colab
* Git
* GitHub

---

## 📥 Extract Phase

* Connected to the DummyJSON API
* Retrieved product data
* Stored the raw response as `products.json`

---

## 🔄 Transform Phase

The following transformations were performed using **PySpark**:

* Read JSON data
* Flatten nested JSON structure
* Selected required columns
* Removed duplicate records
* Handled missing values
* Renamed columns
* Cleaned the dataset

---

## 📤 Load Phase

The transformed data was stored as:

* CSV
* Parquet

This enables efficient analytics and downstream processing.

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/gauravthombal/PySpark-ETL-API-Pipeline.git
```

### Navigate to the project

```bash
cd PySpark-ETL-API-Pipeline
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Extract

```bash
python src/extract.py
```

### Run Transform

```bash
python src/transform.py
```

### Run Complete Pipeline

```bash
python src/main.py
```

---

## 📊 Output

The pipeline generates:

```
data/raw/products.json

data/processed/

data/parquet/
```

---

## 🎯 Skills Demonstrated

* ETL Pipeline Development
* API Data Extraction
* PySpark Data Processing
* Data Cleaning
* Data Transformation
* JSON Processing
* Parquet Storage
* Git & GitHub
* Data Engineering Fundamentals

---

## 🚀 Future Improvements

* Incremental Data Loading
* Logging
* Exception Handling
* Configuration File
* Scheduling with Apache Airflow
* Docker Containerization
* Cloud Storage Integration (AWS S3 / Azure Data Lake)
* CI/CD Pipeline

---

## 👨‍💻 Author

**Gaurav Thombal**

* GitHub: https://github.com/gauravthombal

---

⭐ If you found this project useful, consider giving it a star!
