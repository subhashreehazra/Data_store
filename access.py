import  threading
import sys
import json
from json.decoder import JSONDecodeError
import os
import time

class Data_store:

    def __init__(self):
        self.tm = 0
        self.dt={}

    def create(self, key, val, ttl=0):
        if (os.stat('datastore.json').st_size<=1024*1024*1024):   #checks if the file storing data is less than equal to 1GB
            try:
                dict={}
                if(ttl!=0):
                    self.tm=time.time()+ttl  #sets time to live if provided by the client
                else:
                    self.tm= 0    
                with open('datastore.json',) as json_file: 
                    dict = json.load(json_file)  #loads the json data file as a dictionary
            except JSONDecodeError:
                pass
            if key in dict.keys():  #if key already exists at the time of creation
                print("Error Message: Key already exists in the data store")
            else: 
                if(key.isalpha()):  #key should be a string
                    if(len(key)<=32):   #max size of the key string should be 32 chars
                        try:
                            val=json.loads(val)
                            if(sys.getsizeof(val)<=(16*1024)):   #max size of JSON object value should be 16KB
                                dict[key]=val
                                self.dt[key]=self.tm
                                print("Success: Key value has been successfully")
                                with open('datastore.json', 'w') as outfile:
                                    json.dump(dict, outfile)   #stored back to JSON data file
                            else:
                                print("Error Message: size of the value entered exceeds 16K")  
                        except:
                            print("Error Message: Invalid JSON string")          
                    else:
                        print("Error Message: size of the key exceeds 32 characters")  
                else:
                    print("Error Message: Key should be string")              
        else:
            print("Error Message: File size exceeded 1GB")


    def read(self,key):    
        try:
            dict={}
            with open('datastore.json',) as json_file: #opening JSON data file
                dict = json.load(json_file)
        except JSONDecodeError:
            pass
        if key in dict.keys():
            if(time.time()>self.dt[key] and self.dt[key]!=0):     #checking if the time to live exists for the asked key to read
                print("Error Message: Key entered has expired due to time to live")
            elif(self.dt[key]==0 or time.time()<self.dt[key]):   #if not, print the JSON object value
                print(json.dumps(dict[key]))
        else:
            print("Error Message: Key entered doesn't exits")    #when the key doesn't exist


    def delete(self,key):
        try:
            dict={}
            with open('datastore.json',) as json_file:    #opening JSON data file
                dict = json.load(json_file)
        except JSONDecodeError:
            pass
        if key in dict.keys():
            if(time.time()>self.dt[key] and self.dt[key]!=0):     #checking if the time to live exists for the asked key to delete
                print("Error Message: Key entered has expired due to time to live")
            elif(self.dt[key]==0 or time.time()<self.dt[key]):       #if not, print the JSON object value
                del dict[key]
                print("Key value deleted")
                with open('datastore.json', 'w') as outfile:
                    json.dump(dict, outfile)
        else:
            print("Error Message: Key entered doesn't exits")    