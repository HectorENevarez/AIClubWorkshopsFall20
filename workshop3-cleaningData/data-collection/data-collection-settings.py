import data_collection as dc
import pandas as pd 

path = "C:/Users/Hneva/OneDrive/Desktop/Chrome-Driver/chromedriver.exe"

df = dc.get_jobs('Software Engineer',1000, False, path, 15)

df.to_csv('glassdoor_job.csv', index = False)