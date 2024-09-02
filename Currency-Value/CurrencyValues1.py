# Contains custom functions for dates and currency values.
import datetime as dt

def to_date(any_str):
    """ Convert mm/dd/yy or mm/dd/yyyy string to datetime.date, or None if invalid date. """
    try:
       if len(any_str) == 10:
          the_date = dt.datetime.strptime(any_str,'%m/%d/%Y').date()
       else:
          the_date = dt.datetime.strptime(any_str,'%m/%d/%y').date()
    except (ValueError, TypeError):
            the_date = None
    return the_date

def mdy(any_date):
    """ Return a string date in mm/dd/yyyy format. Pass in Python date or string date in mm/dd/yyyy format """
    if type(any_date) == str:
       any_date = to_date(anydate)
    # Make sure its datetime being fowarded 
    if isinstance(any_date,dt.date):
       s_date = f"{any_date:'%m/%d/%Y'}"
    else:
        s_date = "Invalid date"
    return s_date
    
def to_curr(anynum, len=0):
    """ Return a number as a string with $ and commas. Length is optional """
    s = "Invalid amount"
    try:
       x = float(anynum)
    except ValueError:
         x = None
    if isinstance(x,float):
       s = '$' + f"{x:,.2f}"
       if len > 0:
          s=s.rjust(len)
    return s
