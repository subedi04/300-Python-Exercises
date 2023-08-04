'''
Write a Python Program to Generate 
a random month between start and end date.
'''

from datetime import datetime
from dateutil.relativedelta import relativedelta
import random

def generate_random_month(start_date_str, end_date_str):
    # Convert the start and end dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    delta = relativedelta(end_date, start_date)
    total_months = delta.years * 12 + delta.months
    random_month = random.randint(0, total_months)
    random_date = start_date + relativedelta(months=random_month)
    
    return random_date.strftime("%Y-%m-%d")

if __name__=="__main__":
    generate_random_month("2022-01-01", "2023-12-31")
