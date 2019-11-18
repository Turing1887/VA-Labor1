import csv
import os

user_data = []
# user_data['user'] = []
pauses = []
filename = 'data.csv'

class CSVWriter:

  def __init__(self, name):
    self.name = name

  def readUserData(self):
    with open(filename, newline='') as csvfile:
      csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in csvreader:
        print(', '.join(row))
      
  def addUserData(self,pause):
    pauses.append(str(pause) + ";");

  def writeUserData(self):
    print(pauses)
    with open(filename, 'a', newline='') as csvfile:
      csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      csvwriter.writerow(pauses)