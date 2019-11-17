import json
import os

usercount = 0
user_data = {}
# user_data['user'] = []
pauses = []
filename = 'data.txt'

class JSONWriter:

  def __init__(self, name):
    self.name = name

  def readUserData(self):
    with open(filename) as json_file:
      if os.stat(filename).st_size != 0:
        user_data = json.load(json_file)
        for p in user_data['user']:
          print('Name: ' + p['name'])
          print('Pauses: ' + str(p['pauses']))
          print('')
        print(user_data)
      else:
        print('No User Data Yet')
      
      
  def addUserData(self,pause):
    pauses.append(pause)

  def writeUserData(self):
    user_data.update({
      'user':[
        {
          'name': self.name,
          'pauses': pauses 
        }
      ] 
    })
    print(user_data)
    with open(filename, 'w+') as outfile:
      json.dump(user_data, outfile)