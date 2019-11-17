import csv
import os

usercount = 0
user_data = {}
# user_data['user'] = []
pauses = []
filename = 'data.csv'

class CSVWriter:

  def __init__(self, name):
    self.name = name

  def readUserData(self):
    with open(filename, newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
        print(', '.join(row))
      
      
  def addUserData(self,pause):
    pauses.append(pause)

  def writeUserData(self):

    print(pauses)
    with open('eggs.csv', 'w', newline='') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow(pauses)