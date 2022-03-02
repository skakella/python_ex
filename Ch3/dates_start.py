#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  dt = date.today()
  today = datetime.today()
  print(dt)
  print(today)


  # print out the date's individual components
  print(dt.year, dt.month, dt.day)

  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun")

  print(days[dt.weekday()])

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class

  
  # Get the current time
  dtime = datetime.now()
  curTime = datetime.time(dtime)
  print(curTime)

 

  
if __name__ == "__main__":
  main();
  