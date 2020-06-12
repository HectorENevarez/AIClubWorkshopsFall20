import pandas as pd

df = pd.read_csv('data-collection/glassdoor_job.csv')

#look at those with rating -1
df['Company'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3],axis=1)

df = df[df['Salary Estimate'] != '-1'] #remove any rows with missing salaries
income = df['Salary Estimate'].apply(lambda x: x.split('(')[0]) #remove paranthesis and only keep values
removeExtra = income.apply(lambda x: x.replace('$' , ' ').replace('K' , ' ')) #remove extra variables

# obtain the minimum salary and maximum salary that is split by " - "(hyphen)
df['min_sal'] = removeExtra.apply(lambda x: x.split(' - ')[0]) 
df['max_sal'] = removeExtra.apply(lambda x: x.split(' - ')[1])

print(df.info()) #check to see if min and max are ints

#convert both features to integers
df['min_sal'] = df['min_sal'].astype('int64')
df['max_sal'] = df['max_sal'].astype('int64')

print(df.info()) #notice the change

#average out the salary
df['Salary(Avg)'] = (df.min_sal + df.max_sal) / 2

#seperate State and City variables
df['State'] = df['Location'].str[-3:]
df['City'] = df['Location'].str[:-4]
jobs_in_states = df.State.value_counts()

#For the next lines of code we will correct errors presented by value counts
condition = df.State == 'ote'
column_names =  ['State' , 'City']
df.loc[condition , column_names] = 'Remote'

condition = df.State == 'tes'
column_names =  ['State' , 'City']
df.loc[condition , column_names] = 'United States'

condition = df.State == 'gan'
column_names =  ['State']
df.loc[condition , column_names] = ' MI'

condition = df.State == 'nia'
column_names =  ['State']
df.loc[condition , column_names] = ' VA'

condition = df.State == 'ate'
column_names =  ['State']
df.loc[condition , column_names] = ' NY'

# Double check to make sure no error in value counts
jobs_in_states = df.State.value_counts()

# Find if the job listing is at the headquarters
df['Position at HQ'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0 ,axis=1)

#Determine the age of the company
df['Company Age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

# For a better insight into our data lets see which tools are most used
df['JavaScript'] = df['Job Description'].apply(lambda x: 1 if 'javascript' in x.lower() else 0)
print(df.JavaScript.value_counts())

df['Python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
print(df.Python.value_counts())

df['C_plus'] = df['Job Description'].apply(lambda x: 1 if 'c++' in x.lower() else 0)
print(df.C_plus.value_counts())

df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
print(df.SQL.value_counts())

df['AWS'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
print(df.AWS.value_counts())

# export data to a folder
df.to_csv(r'Salary_Data_Cleaned.csv')