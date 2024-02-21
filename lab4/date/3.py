from datetime import datetime,timedelta
today = datetime.now()
tomorrow = today + timedelta(days = 1)
yesterday = today - timedelta(days = 1)
print(today.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))
print(yesterday.strftime("%Y-%m-%d"))