TIME_TABLE_FILE_NAME = "Format.csv"

def readBooksFile():
    books = list()
    f = open("books.txt")
    for i in f:
        row = i.split(",")
        row = [j.strip() for j in row]
        books.append([row[0], int(row[1]), row[2]])
    return books

def createTimeTable():
    
    import Timing
    periods = len(Timing.makePeriods())
    days = Timing.daysOfMonth()
    import pandas as pd
    dataF = pd.DataFrame(index = days ,columns = ['P%s'%(i+1) for i in range(periods)])
    dataF = dataF.rename_axis('Days', axis = 'index')
    dataF = dataF.fillna(theDefaultEmptyChar())
    dataF.to_csv(TIME_TABLE_FILE_NAME)

def readTimeTable():
    import pandas as pd
    data = pd.read_csv(TIME_TABLE_FILE_NAME)
    data = data.set_index('Days')
    return data


def theDefaultEmptyChar():
    return '#'
def theDefaultLabChars():
    return 'LAB'
                
def generateTimeTable():
    'class whose timetable is to be generated'

    import math
    import Timing
    timeList = Timing.makePeriods()
    daysOfMonth = Timing.daysOfMonth()

    import pandas as pd
    timeTable = readTimeTable()
    subjects = readBooksFile()
    
    import random
    random.shuffle(subjects)

    for dayIndex in range(len(daysOfMonth)):
        d = daysOfMonth[dayIndex]
        tempSubjects = list(subjects)
        for p in timeTable.columns:
            if(len(tempSubjects)!=0):
                random.shuffle(tempSubjects)
                temp = tempSubjects.pop()
                if((timeTable.loc[d,p] == theDefaultEmptyChar())):
                    factor = math.ceil(temp[1]/len(daysOfMonth))
                    markup = "<a target='_blank' href='%s'> %s<br>%d to %d </a>" % (temp[2], temp[0], dayIndex * factor, (dayIndex+1) * factor)
                    timeTable.loc[d,p] = markup 
        else:
            if(len(tempSubjects) != 0):
                print("Not enough slots")
            
    newColumns = dict()
    for i in range(len(timeList)):
        key = 'P%d' % (i+1)
        newColumns[key] = timeList[i]
    timeTable = timeTable.rename(columns= newColumns)
    dataFrameToHtmlString(timeTable)
    


def dataFrameToHtmlString(dFrame, shallTranspose = True):
    if(shallTranspose):
        dFrame = dFrame.T
    import pandas as pd
    pd.set_option('display.max_colwidth', 0)
    dFrame.to_html("table.html", escape = False, border=1)


createTimeTable()
generateTimeTable()