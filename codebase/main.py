import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

REQUIRED_COLUMNS = [
    "Emp_ID", "Name", "Department", "Salary", "Experience"
]
def load_data(file_path):

    if not os.path.exists(file_path):
        print("\nError: CSV file not found!")
        return None
    try:
        df = pd.read_csv(file_path)
        missing_columns = [
            col for col in REQUIRED_COLUMNS
            if col not in df.columns
        ]
        if missing_columns:
            print("Error: Missing columns:", missing_columns)
            return None

        return df[REQUIRED_COLUMNS].copy()

    except Exception as e:
        print("Error loading CSV:", e)
        return None


def clean_data(df):

    print("\n========== DATA CLEANING ==========")

    original_rows = len(df)

    for col in ["Emp_ID", "Name", "Department"]:
        df[col] = df[col].astype("string").str.strip()

    df = df.dropna(subset=["Emp_ID", "Name", "Department"])

    for col in ["Emp_ID", "Name", "Department"]:
        df = df[df[col] != ""]

    df["Salary"] = pd.to_numeric(
        df["Salary"], errors="coerce"
    )

    df["Experience"] = pd.to_numeric(
        df["Experience"], errors="coerce"
    )

    before_duplicates = len(df)
    df = df.drop_duplicates(
        subset=["Emp_ID"], keep="first"
    )

    duplicates_removed = before_duplicates - len(df)
    print("Duplicates removed:", duplicates_removed)
    missing_salary = df["Salary"].isna().sum()

    if missing_salary > 0:
        valid_salaries = df["Salary"].dropna()

        if valid_salaries.empty:
            raise ValueError(
                "Cannot calculate mean: all salaries are missing."
            )

        salary_mean = valid_salaries.mean()
        df.loc[:, "Salary"] = df["Salary"].fillna(
            salary_mean
        )

        print(
            f"Missing Salary filled with mean: {salary_mean:.2f}"
        )

    
    df = df.reset_index(drop=True)

    print("Original rows:", original_rows)
    print("Cleaned rows:", len(df))
    print("===================================")

    return df


def employee_summary(df):

    print("\n========== EMPLOYEE SUMMARY ==========")
    total_employees = len(df)
    average_salary = df["Salary"].mean()

    highest_employee = df.loc[
        df["Salary"].idxmax()
    ]

    total_payroll = df["Salary"].sum()
    print("Employees:", total_employees)
    print(f"Average salary: {average_salary:.2f}")
    print(
        f"Highest paid: {highest_employee['Name']} "
        f"({highest_employee['Salary']:.0f})"
    )

    print(f"Total payroll: {total_payroll:.2f}")

    print("=======================================")


def department_analysis(df):

    print("\n========== DEPARTMENT ANALYSIS ==========")
    department_data = df.groupby("Department").agg(
        Employee_Count=("Emp_ID", "count"),
        Average_Salary=("Salary", "mean")
    )

    for department, row in department_data.iterrows():
        count = int(row["Employee_Count"])
        print(
            f"{department}: {count} employees | "
            f"Avg salary: {row['Average_Salary']:.2f}"
        )

    print("=========================================")

    return department_data

def filter_employees(df):

    print("\n========== SALARY FILTER ==========")

    try:
        limit = float(
            input("Enter salary limit: ")
        )

        filtered_data = df[df["Salary"] > limit]
        print(f"\nEmployees earning above {limit:.2f}:")
        if filtered_data.empty:
            print("No employees found.")

        else:
            for _, employee in filtered_data.iterrows():

                print(
                    f"{employee['Name']} "
                    f"({employee['Salary']:.0f})"
                )

    except ValueError:
        print("Invalid salary limit! Please enter a number.")


def plot_chart(department_data):
    print("\nGenerating department salary chart...")
    plt.figure(figsize=(9, 5))

    department_data["Average_Salary"].plot(
        kind="bar",
        edgecolor="black"
    )

    plt.title("Department-wise Average Salary")
    plt.xlabel("Department")
    plt.ylabel("Average Salary")
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def main():

    print("\n========================================")
    print("       EMPLOYEE DATA ANALYZER")
    print("========================================")

    file_path = (
        sys.argv[1] if len(sys.argv) > 1
        else input("Enter CSV file name (default: employees.csv): ").strip()
    )

    if not file_path:
        file_path = "employees.csv"
    df = load_data(file_path)

    if df is None:
        return

    try:
        df = clean_data(df)
    except ValueError as e:
        print("Data cleaning error:", e)
        return

    # Interactive menu
    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Employee Summary")
        print("2. Department Analysis + Salary Filter + Chart")
        print("3. Filter Employees by Salary")
        print("4. Display All Employees")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":

            employee_summary(df)

        elif choice == "2":
            department_data = department_analysis(df)
            filter_employees(df)
            plot_chart(department_data)

        elif choice == "3":

            filter_employees(df)
        elif choice == "4":
            print("\n========== EMPLOYEE RECORDS ==========")
            print(df.to_string(index=False))

        elif choice == "5":

            print("\nThank you for using Employee Data Analyzer!")

            break

        else:

            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()
