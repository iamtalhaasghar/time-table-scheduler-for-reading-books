DURATION = 60
DAYS = 60

def daysOfMonth():
    daysList = [('Day#%02d' % (i+1)) for i in range(DAYS)]
    return daysList

        
def toMin(time):
    t = time.split(':')
    return int(t[0])*60 + int(t[1])

def to12Hour(minutes):
    h = minutes//60
    m = minutes%60
    status = "?"
    for i in range(h+1):
        if(i%12==0):
            if(i==12):
                status = "PM"
            elif(i == 0): 
                status = "AM"
    return ('%02d:%02d %s' % (12 if h%12==0 else h%12, m, status))


def makePeriods():
    start = "09:00"
    end = "23:59"
    shortBreak = int("30")

    temp = toMin(start)
    timeList=[]
    e = toMin(end)
    while (temp < e):

        if(temp + DURATION <= e):
            other = temp + DURATION
        else:
            temp -= shortBreak
            other = e            
        timeList.append('%s to %s'%(to12Hour(temp),to12Hour(other)))
        temp = other + shortBreak
    return timeList


        

