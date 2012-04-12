"""
Schedule students for lightning talks
"""
import random

students = open('students.txt').read()
students = students.split('\n')
students.remove('')
random.shuffle(students)
weeks = range(3,10)
weeks4 = weeks*4
schedule = zip(weeks4, students)
schedule.sort()
f = open('schedule.txt', 'w')
for week, student in schedule:
    f.write('%s %s\n' % (week, student))
f.close()
