import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import matplotlib.pyplot as plt
import numpy as np

load_dotenv()

connection_url = URL.create(
    drivername="mysql+mysqlconnector",
    username=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    database=os.getenv("MYSQL_DATABASE")
)

engine = create_engine(connection_url)

# Q1 Analyze the number of employees working in each department and present the findings visually.

query="SELECT departments.department_name,employees.employee_id FROM departments INNER JOIN employees ON departments.department_id=employees.department_id;"

df=pd.read_sql(query,engine)

no_of_emp=df.groupby("department_name")["employee_id"].count()
print("number of employees working in each department",no_of_emp)
plt.figure()
no_of_emp.plot(kind='bar')
plt.title("Number of Employees in Each Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()

# Q2 Analyze the average salary of employees in each department and present the findings visually.

query_1="SELECT departments.department_name,salaries.salary FROM departments INNER JOIN employees ON departments.department_id=employees.department_id INNER JOIN salaries ON employees.employee_id=salaries.employee_id;"
df=pd.read_sql(query_1,engine)

ave_salary=df.groupby("department_name")["salary"].mean()
print("average salary of employees in each department",ave_salary)
plt.figure()
ave_salary.plot(kind="bar",color="skyblue")
plt.title("Average salary of employees in each department")
plt.xlabel("department name")
plt.ylabel("average salary")
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.show()

# Q3 Identify the department with the highest total salary and present the comparison visually.

total_salary=df.groupby("department_name")["salary"].sum()
high_salary=total_salary.idxmax()
print("department with the highest total salary:",high_salary)
plt.figure()
total_salary.plot(kind="bar",color="lightgreen")
plt.title("Total salary by department")
plt.xlabel("Highest Salary")
plt.ylabel("Department Name")
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.show()

# Q4 Analyze employee distribution across different cities and present the findings visually.

query_2="SELECT employee_name,city FROM employees"
df=pd.read_sql(query_2,engine)
city_emp=df.groupby("city")["employee_name"].count()
print("employee distribution across different cities ",city_emp)

plt.figure()
city_emp.plot.bar()
plt.title("total employees across different city")
plt.xlabel("city")
plt.ylabel("no of employee")
plt.tight_layout()
plt.show()

# Q5 Analyze employee performance across departments and present the findings visually.

query_3="SELECT employees.employee_id,departments.department_name FROM employees INNER JOIN departments ON employees.department_id=departments.department_id;"

df=pd.read_sql(query_3,engine)
dep_name=df.groupby("department_name")["employee_id"].count()
print("employee performance across departments",dep_name)
plt.figure()
dep_name.plot.bar()
plt.title("total employees across different city")
plt.xlabel("city")
plt.ylabel("no of employee")
plt.tight_layout()
plt.show()

# Q6 Identify the highest-paid employees and present the salary comparison visually.

query_4="SELECT employees.employee_name,salaries.salary,employees.employee_id FROM employees INNER JOIN salaries ON employees.employee_id=salaries.employee_id;"

df=pd.read_sql(query_4,engine)

sal_emp=df.groupby(["employee_id",'employee_name'])["salary"].sum()
high_sal_emp=sal_emp.idxmax()
print("highest-paid employees",high_sal_emp)
plt.figure()
name=sal_emp.index.get_level_values("employee_name")
value=sal_emp.values
plt.bar(name,value)
plt.title("Salary comparison of employees")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.ticklabel_format(style="plain", axis="y")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()

# Q7 Analyze the overall distribution of employee salaries and present the findings visually.

dis=df["salary"].describe()
print("overall distribution of employee salaries",dis)

plt.figure()
plt.hist(df["salary"],bins=5,color="green",edgecolor="black")
plt.title("Distribution of employees Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.ticklabel_format(style="plain",axis="x")
plt.show()

# Q8 Analyze how salaries vary between different departments and present the findings visually.

query_5="SELECT departments.department_name,salaries.salary FROM departments INNER JOIN employees ON departments.department_id=employees.department_id INNER JOIN salaries ON employees.employee_id=salaries.employee_id;"
df=pd.read_sql(query_5,engine)

aver_salary=df.groupby("department_name")["salary"].mean()
print("salaries vary between department",aver_salary)
plt.figure()
aver_salary.plot(kind="bar",color="olive")
plt.title("Salaries vary differnt department")
plt.xlabel("department name")
plt.ylabel("salary")
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.show()

# Q9 Identify employees earning above the company average and present the findings visually.

query_6="SELECT departments.department_name,salaries.salary ,employees.employee_name FROM departments INNER JOIN employees ON departments.department_id=employees.department_id INNER JOIN salaries ON employees.employee_id=salaries.employee_id;"
df=pd.read_sql(query_6,engine)

company_average = df["salary"].mean()
above_ave_emp=df[df["salary"]>company_average]
print("above the company average:",above_ave_emp)

plt.figure()
above_ave_emp.plot.bar(x='employee_name',y='salary',color="slateblue")
plt.title("employees earning above the company average")
plt.xlabel("department name")
plt.ylabel("Above average salary")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.xticks(rotation=45,ha="right")
plt.show()

# Q10 Analyze the budgets of all projects and present the comparison visually.

query_7="SELECT project_name,budget FROM projects;"
df=pd.read_sql(query_7,engine)

print("the budgets of all projects",df)

plt.figure()
df.plot.bar(x="project_name",y="budget",color="coral")
plt.xlabel("Project Name")
plt.ylabel("Budget")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.xticks(rotation=45,ha="right")
plt.show()

# Q11 Identify which departments handle the highest project budgets and present the findings visually.

query_8="SELECT departments.department_name,projects.project_name,projects.budget FROM departments INNER JOIN  projects ON departments.department_id=projects.department_id;"
df=pd.read_sql(query_8,engine)

bud_pro=df.groupby("department_name")["budget"].sum()
high_bud_pro=bud_pro.idxmax()
print("departments handle the highest project budgets:",high_bud_pro)

plt.figure()
bud_pro.plot.bar()
plt.title("deparment name with budget")
plt.xlabel("Department Name")
plt.ylabel("Budget")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.xticks(rotation=45,ha="right")
plt.show()

# Q12 Analyze the project budgets associated with different clients and present the findings visually.

query_9="SELECT clients.client_name,projects.budget FROM clients INNER JOIN projects ON clients.client_id=projects.client_id;"
df=pd.read_sql(query_9,engine)

client_bud=df.groupby("client_name")["budget"].sum()
print("project budgets associated with different clients",client_bud)

plt.figure()
client_bud.plot.bar(color="orange")
plt.xlabel("cilent name")
plt.ylabel("Project budget")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.xticks(rotation=45,ha="right")
plt.show()

# Q13 Analyze the distribution of projects according to their current status and present the findings visually.

query_10="SELECT project_status,project_name FROM projects;"
df=pd.read_sql(query_10,engine)

pro_status=df["project_status"].value_counts()
print("distribution of projects according to their current status ",pro_status)
plt.figure()
pro_status.plot.bar(color="coral")

plt.title("Distribution of Projects by Current Status")
plt.xlabel("Project Status")
plt.ylabel("Number of Projects")

plt.tight_layout()
plt.show()

# Q14 Analyze project budgets according to their start dates and present the trend visually.

query_11="SELECT start_date,budget,project_name FROM projects ORDER BY start_date ASC;"

df=pd.read_sql(query_11,engine)
print("project budgets according to their start dates ",df)

plt.figure()
df.plot.bar(x="start_date",y="budget",color="black")
plt.grid()
plt.xlabel("Start Date")
plt.ylabel("Budget")
plt.title("project budgets according to their start dates ")
plt.ticklabel_format(style="plain",axis="y")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()

# Q15 Identify employees with the highest performance scores and present the comparison visually.

query_12="SELECT employees.employee_name,employee_projects.performance_score,employees.employee_id FROM employees INNER JOIN employee_projects ON employees.employee_id=employee_projects.employee_id;"

df=pd.read_sql(query_12,engine)

performance=df.groupby(["employee_id",'employee_name'])["performance_score"].sum()
high_performance=performance.idxmax()
print("employees with the highest performance scores",high_performance)

plt.figure()
name=performance.index.get_level_values("employee_name")
performance.plot.bar(x="name",y="score")
plt.xlabel('Employee Name')
plt.ylabel('Perfromance Score')
plt.title("Emploee and they Score")
plt.ticklabel_format(style="plain",axis="y")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()

# Q16 Analyze the distribution of employee performance scores and present the findings visually.

QUERY_13="SELECT employees.employee_id,employees.employee_name,employee_projects.performance_score FROM employees INNER JOIN employee_projects ON employees.employee_id=employee_projects.employee_id;"
df=pd.read_sql(QUERY_13,engine)

per_dis=df.groupby(["employee_name",'employee_id'])["performance_score"].describe()
print("distribution of employee performance scores",per_dis)

plt.figure()
name=per_dis.index.get_level_values("employee_name")
per_dis["mean"].plot.bar()
plt.xlabel('Employee Name')
plt.ylabel('Perfromance Score')
plt.title("performance_score")
plt.ticklabel_format(style="plain",axis="y")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()

# Q17Analyze the relationship between working hours and performance scores and present the findings visually.

query_14="SELECT performance_score,hours_worked FROM employee_projects;"
df=pd.read_sql(query_14,engine)

print("relationship between working hours and performance scores",df)

plt.figure()
df.plot.scatter(x="performance_score",y="hours_worked",marker="s")
plt.xlabel("perfromace work")
plt.ylabel("working hours")
plt.title("Relationship Between Working Hours and Performance Scores ")
plt.tight_layout()
plt.show()

# Q18 Analyze the relationship between employee salary and project working hours and present the findings visually.

query_15="SELECT salaries.salary,employee_projects.hours_worked,employees.employee_id FROM employees INNER JOIN salaries ON employees.employee_id = salaries.employee_id INNER JOIN employee_projects ON employees.employee_id = employee_projects.employee_id; "
df=pd.read_sql(query_15,engine)

emp_hour=df.groupby('employee_id')["hours_worked"].sum()
emp_sal=df.groupby("employee_id")["salary"].first()
emp_rel_pro=pd.DataFrame({
    "hours_worked":emp_hour,
    "salary":emp_sal
})
print("relationship between employee salary and project working hours ",emp_rel_pro)

plt.figure()
emp_rel_pro.plot.scatter(x="hours_worked",y="salary",marker="o",cmap="viridis")
plt.xlabel("total workong hours")
plt.ylabel("salary")
plt.title("relationship between employee salary and project working hours")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.show()

# Q19 Analyze project performance in relation to project budget and present the findings visually.

query_16="SELECT projects.budget,employee_projects.performance_score FROM projects INNER JOIN employee_projects ON projects.project_id=employee_projects.project_id; "
df=pd.read_sql(query_16,engine)

print("project performance in relation to project budget",df)
plt.figure()
df.plot.scatter(x="performance_score",y="budget",marker="o")
plt.grid()
plt.xlabel("perfromance score")
plt.ylabel("budget")
plt.title("project project in relation to project budget")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.show()

# Q20 Analyze completed and incomplete tasks across the company and present the findings visually.

query_17="SELECT tasks.task_status, departments.department_name FROM employees INNER JOIN departments ON employees.department_id=departments.department_id INNER JOIN tasks ON tasks.employee_id=employees.employee_id;"
df=pd.read_sql(query_17,engine)

task=df.groupby("department_name")["task_status"].value_counts()
print("completed and incomplete tasks across the company ",task)

plt.figure()
table=task.unstack(fill_value=0)
department_name=table.index
complete=table["Completed"]
incomplete=table["In Progress"]

x=np.arange(len(department_name))
width=0.35

plt.bar(x-width/2,complete,width,label="complete task")
plt.bar(x+width/2,incomplete,width,label="Incomplete task")
plt.xticks(x,department_name ,rotation=45,ha="right")
plt.xlabel("Department")
plt.ylabel("Number of Tasks")
plt.title("Completed and Incomplete Tasks Across Departments")
plt.legend()
plt.tight_layout()
plt.show()

# Q21 Identify employees with the highest number of completed tasks and present the comparison visually.

query_18="SELECT employees.employee_name,employees.employee_id,tasks.task_status FROM employees INNER JOIN  tasks ON employees.employee_id=tasks.employee_id;"
df=pd.read_sql(query_18,engine)

high_num=df[df["task_status"]=='Completed'].groupby(["employee_id","employee_name"])["task_status"].count()
max_count = high_num.max()
highest_employees = high_num[high_num == max_count]
print("employees with the highest number of completed tasks",highest_employees)

plt.figure()
high_num.plot.bar()
plt.xlabel("Employee_name")
plt.ylabel("num of completed ")
plt.title("Employee with the completed task")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()

# Q22 Identify projects with the highest number of incomplete tasks and present the comparison visually.

high_num=df[df["task_status"]=='In Progress'].groupby(["employee_id","employee_name"])["task_status"].count()
max_count = high_num.max()
highest_employees = high_num[high_num == max_count]
print("employees with the highest number of incompleted tasks",highest_employees)

plt.figure()
high_num.plot.bar()
plt.xlabel("Employee name")
plt.ylabel("num of incompleted ")
plt.title("Employee with the incompleted task")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show() 

# Q23 Analyze the time required to complete tasks and present the findings visually.

query_19="SELECT task_id,task_name,assigned_date,completed_date FROM tasks WHERE completed_date IS NOT NULL;"
df=pd.read_sql(query_19,engine)

df["completed_date"]=pd.to_datetime(df["completed_date"])
df["assigned_date"]=pd.to_datetime(df["assigned_date"])
df["total_time"]=(df["completed_date"]-df["assigned_date"]).dt.days
print("time required to complete tasks",df[['task_id','task_name','total_time']])

plt.figure()
df.plot.bar(x="task_name",y="total_time")
plt.xlabel("task name")
plt.ylabel("completed day")
plt.title("time required to completed task")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.show()

# Q24 Compare departments based on employee count, salary, project activity and performance, and present the findings visually.

query_20="SELECT departments.department_id,departments.department_name,employees.employee_id,salaries.salary,projects.project_id,employee_projects.performance_score FROM departments  INNER JOIN employees ON departments.department_id=employees.department_id INNER JOIN salaries ON employees.employee_id=salaries.employee_id INNER JOIN employee_projects ON employees.employee_id=employee_projects.employee_id INNER JOIN projects ON employee_projects.project_id=projects.project_id; "
df=pd.read_sql(query_20,engine)

employee_count = df.groupby("department_name")["employee_id"].nunique()
avg_salary = df.groupby("department_name")["salary"].mean()
project_activity = df.groupby("department_name")["project_id"].nunique()
avg_performance = df.groupby("department_name")["performance_score"].mean()

department_analysis = pd.DataFrame({
    "employee_count": employee_count,
    "average_salary": avg_salary,
    "project_activity": project_activity,
    "average_performance": avg_performance
})

print("Compare departments based on employee count, salary, project activity and performance",department_analysis)

plt.figure()
fig,ax=plt.subplots(2,2,figsize=(14,9))

department_analysis["employee_count"].plot.bar(ax=ax[0,0])
ax[0,0].set_xlabel("department name")
ax[0,0].set_ylabel(" No of employees")
ax[0,0].set_title("No of Employee in each department")
ax[0,0].tick_params(axis="x",rotation=45)


department_analysis["average_salary"].plot.bar(ax=ax[0, 1],color="orange")
ax[0,1].set_xlabel("department name")
ax[0,1].set_ylabel(" average salary")
ax[0,1].set_title("Average Salary in each department")
ax[0,1].tick_params(axis="x",rotation=45)
ax[0,1].ticklabel_format(style="plain",axis="y")

department_analysis["project_activity"].plot.bar(ax=ax[1, 0],color="green")
ax[1,0].set_xlabel("department name")
ax[1,0].set_ylabel(" No of projects id ")
ax[1,0].set_title("No of project id  in each department")
ax[1,0].tick_params(axis="x",rotation=45)


department_analysis["average_performance"].plot.bar(ax=ax[1, 1],color="purple")
ax[1,1].set_xlabel("department name")
ax[1,1].set_ylabel(" average perfromance score")
ax[1,1].set_title("perfromance score  in each department")
ax[1,1].tick_params(axis="x",rotation=45)
ax[1,1].ticklabel_format(style="plain",axis="y")

fig.suptitle("Compare departments based on employee count, salary, project activity and performance")

plt.tight_layout()
plt.show()

# Q25 Analyze the relationship between project budget, working hours and performance, and present the findings visually.

query_21="SELECT projects.project_id, projects.budget,employee_projects.hours_worked,employee_projects.performance_score FROM projects INNER JOIN employee_projects ON projects.project_id=employee_projects.project_id; "
df=pd.read_sql(query_21,engine)

rel_pro_bud_per=df.groupby("project_id").agg({
    "budget":"first",
    "hours_worked":"sum",
    "performance_score":"mean"
})
print("relationship between project budget, working hours and performance",rel_pro_bud_per)

plt.figure()
rel_pro_bud_per.plot.scatter(
    x="hours_worked",
    y="budget",
    c="performance_score",
    colormap="viridis",
    colorbar=True)

plt.xlabel("Total Working Hours")
plt.ylabel("Project Budget")
plt.title("Relationship Between Project Budget, Working Hours and Performance")
plt.ticklabel_format(style="plain", axis="y")
plt.tight_layout()
plt.show()

# Q26 Analyze client-wise project activity and performance and present the findings visually.

query_22="SELECT clients.client_id,clients.client_name,projects.project_id,projects.project_name,employee_projects.performance_score FROM clients INNER JOIN projects ON clients.client_id=projects.client_id INNER JOIN employee_projects ON projects.project_id=employee_projects.project_id;"
df=pd.read_sql(query_22,engine)

pro_act=df.groupby("client_id")["performance_score"].mean()
project_act=df.groupby("client_id")["project_id"].nunique()

cilent_wise=pd.DataFrame({
    "project_activity":project_act.values,
    "average_performance":pro_act.values,
    "client_id":project_act.index
})
print("client-wise project activity and performance ",cilent_wise)

plt.figure()
cilent_wise.plot.scatter(x="project_activity",y="average_performance",c="client_id",cmap="viridis",colorbar=True)
plt.xlabel("project actitvity")
plt.ylabel("Average perfromance score")
plt.title("client-wise project activity and performance")
plt.ticklabel_format(style="plain",axis="y")
plt.tight_layout()
plt.show()

