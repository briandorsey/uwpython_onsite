import subprocess
import os


special_case = False

def fetch(url):
    if special_case:
        print 'this is special'

    stdout, stderr = subprocess.Popen(['curl', url], stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE).communicate()
    data = stdout
    fish = 'yummy'
    return data
