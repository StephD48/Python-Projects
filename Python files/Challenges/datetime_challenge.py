
from datetime import datetime
from pytz import timezone


format = "%Y-%m-%d %H:%M:%S %Z%z"

hours = '08:00 - 15:00'

now_utc = datetime.now(timezone('US/Pacific'))
if hours >'8:00' and  hours < '15:00':
    print('This branch is closed.')
else:
    print('This branch is open.')

print('The current time in Portland Oregon is:', now_utc.strftime(format))

now_utc = datetime.now(timezone('US/Eastern'))
if hours > '08:00' and  hours < '15:00':
    print('This branch is closed.')
else:
    print('This branch is open.')    
print('The current time in New York is:', now_utc.strftime(format))


now_utc = datetime.now(timezone('Europe/London'))
if hours > '08:00' and hours < '15:00':
    print('This branch is closed.')
else:
    print('This branch is open.')
print('The current time in London England is:', now_utc.strftime(format))



