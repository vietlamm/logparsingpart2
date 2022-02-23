from urllib.request import urlretrieve
import re
#fetching a file and downloading a local copy
URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'


local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)


local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)

j=0

#creating a list for the log file and running it through a loop
#need to create another loop so that it reads the file and see whats month it is so it can split the file based on what month it is
with open("local_copy.log", "r") as file:
  for l in file:
    d=l.split()
      if re.search ('(/Jan/)', l):
      j+=1
      
      print(d)
