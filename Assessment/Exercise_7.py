#EX 7

# Pandas DataFrame Filtering

import pandas as pd

data =  {
    "name": ["Isha", "Punith", "Aasha", "Vinith", "Priya", "Anusuya"],
    "Department": ["Sales", "Testing", "HR", "Marketinng", "HR", "Finance"],
    "Salary": [25000, 37000, 30000, 27000, 30000, 49000]

}

df = pd.DataFrame(data)
print(df)

print("\n")

percentile = df["Salary"].quantile(0.75)
print("percentile: ",percentile)

print("\n")

emp_with_sal_More_than_75_percentile = df[df["Salary"]>percentile]

print("high earning employees: \n",emp_with_sal_More_than_75_percentile)


"""

This program creates a DataFrame of employees with their salaries.

It calculates the 75th percentile salary and then filters out
all employees whose salary is greater than that value.

"""