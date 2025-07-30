# %%
#1. How many employees are there in each department?
import pandas as pd
data=pd.read_csv('employee_data_project.csv')

data.columns


# %%


# %%
no_of_employee=data['Department'].value_counts()
no_of_employee


# %%
#2. What is the average salary in each department?
data.columns


# %%
average_salary = data.groupby('Department')['Salary'].mean()

print(average_salary)


# %%
#3. Which department has the highest number of employees with “Excellent” performance?
## (idxmax) It returns the index label (i.e., the department name) of the maximum value in the Series.

#data[data['Performance_Rating'] == 'Excellent']['Department'].value_counts().idxmax()

data[data['Performance_Rating'] == 'Excellent']['Department'].value_counts()



# %%
#4. What is the distribution of positions across the organization?
data.columns


# %%
data['Position'].value_counts()


# %%
#5. What is the average attendance rate per department?
data.columns


# %%
average_attendence = data.groupby('Department')['Attendance_Rate'].mean()
average_attendence


# %%
#6. Who are the top 10 highest paid employees?
data.columns


# %%
top_10=data.sort_values(by='Salary',ascending=False).head(10)
top_10[['Employee_ID','Name','Department','Salary']]


# %%
#7. What is the average age of employees in each department?
data.columns


# %%
average_age=data.groupby('Department')['Age'].mean()
average_age


# %%
#8. Count employees who joined after 2022.
import datetime as dt
data.columns


# %%
data['Joining_Date'] = pd.to_datetime(data['Joining_Date'])
count_after_2022 = data[data['Joining_Date'] > '2022-12-31'].value_counts().sum()
print("Total Numbe rof employee who joined after 2022: ",count_after_2022)


# %%
#9. What’s the average number of leaves taken by each position?
data.columns


# %%
average_leaves=data.groupby('Position')['Leaves_Taken'].mean()
average_leaves


# %%
#10. How many employees have taken more than 20 leaves?
data.columns


# %%
more_than_20_leaves=(data['Leaves_Taken']>20).sum()
print("Toatal Number of People: ",more_than_20_leaves)


# %%
#11. Find the employee(s) with the lowest attendance rate.
data.columns


# %%
min_attendance = data['Attendance_Rate'].min()
lowest_attendance_employees = data[data['Attendance_Rate'] == min_attendance]
lowest_attendance_employees[['Employee_ID', 'Name', 'Department', 'Attendance_Rate']]


# %%
#12. What’s the salary range in each department?
data.columns


# %%
salary_range=data.groupby('Department')['Salary'].agg(['min', 'max'])
print(salary_range)


# %%
#13. Add a column called "Experience_Years" based on Joining_Date.
data.columns


# %%
data['Experience_Years'] = (pd.Timestamp.today() - pd.to_datetime(data['Joining_Date'])).dt.days // 365
data[['Employee_ID', 'Experience_Years']]


# %%
#14. Filter all employees with "Good" or "Excellent" performance and salary > 100000.
filter=data[((data['Performance_Rating'] == 'Good') | (data['Performance_Rating'] == 'Excellent')) & (data['Salary'] > 100000)]
filter


# %%
#15. Find the median salary for each position.
median_salary=data.groupby('Position')['Salary'].median()
median_salary


# %%
#16. Create a pivot table showing average salary by Department and Position.
pivot_table=data.pivot_table(values='Salary', index='Department', columns='Position', aggfunc='mean')
pivot_table


# %%
#17. What percentage of employees are in each performance rating category?
percentage=data['Performance_Rating'].value_counts(normalize=True) * 100
percentage


# %%
#18. List employees with above average salary and below average attendance.
employes_average=data[(data['Salary'] > data['Salary'].mean()) & (data['Attendance_Rate'] < data['Attendance_Rate'].mean())]
employes_average


# %%


# %%


# %%



