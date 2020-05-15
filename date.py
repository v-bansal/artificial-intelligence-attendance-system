from datetime import datetime, date

today = date.today()
dt = today.strftime("%d-%m-%Y")
print(dt)

currTime = datetime.now()
tm = currTime.time()
print(tm)

timestamp = datetime.now()
dt_string = timestamp.strftime("%d %m %Y %H:%M:%S")
d = datetime.strptime(dt_string, "%d %m %Y  %H:%M:%S")
tt = (d.hour,d.minute,d.second)
print(tt)