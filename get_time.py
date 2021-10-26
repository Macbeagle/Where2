import datetime
from pytz import timezone  

brisbane_tz = timezone('Australia/Brisbane')
time = datetime.now(brisbane_tz)
time = time.strftime('%H')

pretend_time = 6