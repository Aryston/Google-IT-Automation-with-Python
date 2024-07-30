from datetime import datetime, timedelta

# Početni datum
start_date = datetime(2024, 7, 28)

# Broj dana za dodati
days_to_add = 1010

# Novi datum
new_date = start_date + timedelta(days=days_to_add)
new_date.strftime('%A, %d. %B %Y.')

#gemini

from datetime import datetime, timedelta

def add_days_to_date(start_date_str, days_to_add):
    start_date = datetime.strptime(start_date_str, "%d. %B %Y.")
    new_date = start_date + timedelta(days=days_to_add)
    return new_date.strftime("%A, %d. %B %Y.")

start_date_str = "28. srpnja 2024."
days_to_add = 1010

new_date_str = add_days_to_date(start_date_str, days_to_add)
print(f"1010 dana nakon {start_date_str} je {new_date_str}")
