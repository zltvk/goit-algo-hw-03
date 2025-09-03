from datetime import datetime

def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        diff = today - date_object
        print(f'The difference is {diff.days} days')
        return diff.days
    except ValueError:
        return f"Date format {date} is not correct! The correct format is: 'YYYY-MM-DD'"
        
get_days_from_today("2025-10-09")


#-------------------------------------------------------------





