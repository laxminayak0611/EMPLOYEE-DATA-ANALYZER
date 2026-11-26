# Employee Data Analyzer

**PS No. 28 | Python 3 | Pandas | Matplotlib**

An interactive Python-based application that analyzes employee data from CSV files. It cleans employee records, calculates salary statistics, performs department-wise analysis, filters employees based on salary limits, and generates visualizations.

## Project Overview

The Employee Data Analyzer simplifies employee data analysis using Python and Pandas.

It processes CSV files containing employee information and generates meaningful insights such as:

- Total number of employees.
- Average employee salary.
- Highest-paid employee.
- Total salary expenditure (payroll).
- Department-wise employee count.
- Department-wise average salary.
- Employees earning above a specified salary.

It also generates a bar chart using Matplotlib for department-wise salary comparison.

## Features

- **CSV Data Loading:** Import employee records using Pandas.
- **Data Cleaning:** Remove duplicate employee IDs.
- **Missing Value Handling:** Fill missing salaries using the mean of valid salaries.
- **Employee Summary:** Calculate total employees, average salary, highest salary, and total payroll.
- **Department Analysis:** Calculate employee count and average salary department-wise.
- **Salary Filtering:** Find employees earning above a user-defined salary.
- **Data Visualization:** Generate department-wise average salary bar charts.
- **Interactive Menu:** Access all features through a console-based interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| Pandas | Data processing and analysis |
| Matplotlib | Data visualization |
| CSV | Dataset storage |

## Project Structure

```text
Employee-Data-Analyzer/
│
├── Source Code/
│   └── main.py
│   └── employees.csv
│
├── Documentation/
│   ├── Project_Report.docx
│   └── Project_Presentation.pptx
│
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Employee-Data-Analyzer
```

### 3. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 4. Run the Application

Navigate to the Source Code directory and run:

```bash
python main.py
```

The application will ask for the CSV file name. Enter the path to `employees.csv`.

## Dataset Format

The application expects a CSV file with the following columns:

| Column | Description |
|---|---|
| Emp_ID | Employee ID |
| Name | Employee name |
| Department | Department name |
| Salary | Employee salary |
| Experience | Work experience in years |

### Sample Dataset

```csv
Emp_ID,Name,Department,Salary,Experience
E1,Aman,IT,50000,3
E2,Riya,HR,40000,2
E3,Karan,IT,70000,5
```

**Note:** This project uses dummy employee data only.

## Application Menu

```text
========================================
       EMPLOYEE DATA ANALYZER
========================================

1. Employee Summary
2. Department Analysis + Salary Filter + Chart
3. Filter Employees by Salary
4. Display All Employees
5. Exit

Enter your choice (1-5):
```

## Sample Analysis

For the following employee records:

| Employee | Department | Salary |
|---|---|---:|
| Aman | IT | 50,000 |
| Riya | HR | 40,000 |
| Karan | IT | 70,000 |

### Employee Summary

```text
Employees: 3
Average salary: 53333.33
Highest paid: Karan (70000)
Total payroll: 160000.00
```

### Department-wise Analysis

| Department | Employees | Average Salary |
|---|---:|---:|
| IT | 2 | 60,000 |
| HR | 1 | 40,000 |

### Salary Filtering

For a salary limit of 45,000:

```text
Aman (50000)
Karan (70000)
```

## Data Cleaning Logic

The application follows these data-cleaning steps:

1. Remove rows with missing essential employee information.
2. Convert salary and experience values into numeric format.
3. Remove duplicate employee IDs.
4. Identify missing salary values.
5. Calculate the mean of valid salaries.
6. Replace missing salaries with the calculated mean.

## Testing

The application is designed around the following four test scenarios:

| Test Case | Description |
|---|---|
| Test Case 1 | Normal employee data |
| Test Case 2 | Single employee record |
| Test Case 3 | Duplicate records and missing salary |
| Test Case 4 | Department analysis and salary filtering |

## Learning Outcomes

Through this project, the following concepts are demonstrated:

- Python functions and conditional statements.
- File handling and CSV processing.
- Pandas DataFrames.
- Data cleaning and missing value handling.
- `drop_duplicates()` and `fillna()`.
- `groupby()` and aggregation.
- Boolean filtering.
- Matplotlib data visualization.

## Future Improvements

- Interactive dashboard using Streamlit.
- MySQL database integration.
- Employee search and advanced filtering.
- Excel and PDF report generation.
- Additional data visualization and analytics.

## Author

**Project:** Employee Data Analyzer  
**Problem Statement Number:** 28  
**Language:** Python 3

## License

This project is developed for educational and academic purposes.# EMPLOYEE-DATA-ANALYZER
