# Import all the code from CurrencyValues1 as my.
import CurrencyValues1 as my

# Need dates in this code
from datetime import datetime as dt

# Some simple test data
string_date="12/31/2018"
# Convert string date to datetime.date
print(my.to_date(string_date ))

today = dt.today()
# Show today's date in mm/dd/yyyy format
print(my.mdy(today))

dollar_amt=12345.678
# Show this big number in currency format
print(my.to_curr(dollar_amt))
