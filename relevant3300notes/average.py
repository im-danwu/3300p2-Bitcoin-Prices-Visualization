from datetime import datetime


def avg(stack):
    if len(stack) == 0:
        return None
    else:
        return sum(stack) / float(len(stack))

lines = []
with open('bitcoins-minute.csv') as f:
    lines = [line.strip() for line in f.readlines()]

f = open('bitcoins-weekly.csv', 'w')

prev = datetime.now()
stack = []
for line in lines:
    buy, sell, timestr = line.split(',')
    timestamp = datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')

    if timestamp.isocalendar()[1] == prev.isocalendar()[1]:
        stack.append(float(buy))
    else:
        average = avg(stack)
        stack = [float(buy)]
        if average is not None:
            #print timestamp, average
            f.write(str(timestamp) + ', ' + str(average) + '\n')
    prev = timestamp
    
f.close()


