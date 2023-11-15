-- Databricks notebook source
-- DBTITLE 1,show discription of the data

select * from employee;

-- COMMAND ----------

-- DBTITLE 1,Total number of employees in company
select sum( employeecount) as employee_count from employee;

-- COMMAND ----------

-- DBTITLE 1,To check the number of people who are leaving the company
select Attrition,sum(employeecount) employee_count from employee
group by 1;

-- COMMAND ----------

-- DBTITLE 1,Age analysis for which age group we have high attrition number 
select 
    case 
    when Age between 20 and 30 then '20-30'
    when Age between 31 and 40 then '31-40'
    else '41+' end as age_grp,
    sum(employeecount) employeecount
from employee
where Attrition = 'Yes'
group by 1
order by 2 desc;

-- COMMAND ----------

-- DBTITLE 1,Find out attrition by Department
select department,sum(employeecount) employeecount
from employee where Attrition = 'Yes'
group by 1
order by 2 desc;

-- COMMAND ----------

-- DBTITLE 1,attrition by education (1-below college,2-college,3-bachelor,4-master,5-doctor)
select
case when Education = 1 then 'Below College'
     when Education = 2 then 'College'
     when Education = 3 then 'Bachelor'
     when Education = 4 then 'Master'
     when Education = 5 then 'Doctor'
     end Eduction
,sum(employeecount) employeecount
from employee where Attrition = 'Yes'
group by 1
order by 2 desc;

-- COMMAND ----------

-- DBTITLE 1,Attrition by Environement satisfaction (1 - low, 2 - medium, 3 - high, 4 - highly satisfied)
select
case when EnvironmentSatisfaction = 1 then 'Low'
     when EnvironmentSatisfaction = 2 then 'Medium'
     when EnvironmentSatisfaction = 3 then 'High'
     when EnvironmentSatisfaction = 4 then 'Highly Satisfied'
     end EnvironmentSatisfaction
,sum(employeecount) employeecount
from employee where Attrition = 'Yes'
group by 1
order by 2 desc;

-- COMMAND ----------

-- DBTITLE 1,Attrition by job satisfaction
select
case when JobSatisfaction = 1 then 'Low'
     when JobSatisfaction = 2 then 'Medium'
     when JobSatisfaction = 3 then 'High'
     when JobSatisfaction = 4 then 'Highly Satisfied'
     end JobSatisfaction
,sum(employeecount) employeecount
from employee where Attrition = 'Yes'
group by 1
order by 2 desc;

-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------



-- COMMAND ----------


