import requests
import urllib.request , json
import ast
from datetime import datetime


# basic functions
def sortli(li, key, reverse=False):
    if reverse == True:
        li.sort(key= lambda x:x[key], reverse = True)    
    else:
        li.sort(key= lambda x:x[key])
    return li


# the get country class will first collect the list of fstate names and will fetch the current world values
class worldwide():
    def __init__(self):
        country_names = urllib.request.urlopen("https://covid19.mathdro.id/api/countries")   
        country_dict = eval(country_names.read().decode())
        country_i = country_dict["countries"]
        worldwide_values = urllib.request.urlopen("https://covid19.mathdro.id/api")
        worldwide_dict = eval(worldwide_values.read().decode())
        self.__worldwide_values={}
        count = 0
        for x,y in worldwide_dict.items():
            if count>2:
                break
            self.__worldwide_values[x]=y['value']
            count +=1 
        self.__country_list = []
        self.__all_state_data_list=[]
        self.__state_data_list=[]
        self.__update_date =""
        self.__state_list=[]
        for i in country_i:
            self.__country_list.append(i['name'].lower())

    # returns list of countries
    def country_list(self):
        return self.__country_list 

    # returns a dictionary with the three values
    def worldwide_data(self):
        return self.__worldwide_values

    def last_date(self):
        return self.__update_date

    #returns a dictionary of confirmed recovered and deaths of the country
    def get_country_data(self, country):
        if country.lower() not in self.__country_list:
            raise ValueError("The country does not exist, make sure you chose the correct country")
        else:    
            city_data = urllib.request.urlopen("https://covid19.mathdro.id/api/countries/"+country)   
            country_dict = eval(city_data.read().decode())
            local_val_dict={}
            for x,y in country_dict.items():
                if type(y) == str:
                    self.__update_date = y
                else:
                    local_val_dict[x]= y['value']
        return local_val_dict    


    def save_state_data(self, country):
        if country.lower() not in self.__country_list:
            raise ValueError("The country does not exist, make sure you chose the correct country")
        else:
            city_data = urllib.request.urlopen("https://covid19.mathdro.id/api/countries/"+country+"/confirmed")
            state_list = json.loads(city_data.read().decode())
            if len(state_list) == 1:
                self.__state_list = ["no data"]
                return
            else:
                self.__state_list=[]
                for fstate in state_list:
                    local_dict={}
                    
                    if fstate["provinceState"] not in self.__state_list:
                        self.__state_list.append(fstate["provinceState"])
                    local_dict["state"] = fstate["provinceState"]
                    local_dict["confirmed"]= fstate['confirmed']
                    local_dict["recovered"]= fstate['recovered']
                    local_dict["detahs"]= fstate['deaths']
                    local_dict["active"]= fstate['active']
                    local_dict["user"] = "Ayush"
                    local_dict["lastupdate"]= str(datetime.fromtimestamp(int(str(fstate['lastUpdate'])[:-3])))
                    self.__all_state_data_list.append(local_dict)
    def state_list(self,country):
        self.save_state_data(country)
        return self.__state_list    

    def get_state_data(self,country=None,state=None, latest = False):
        if country is None:
            raise ValueError("please enter country name")
        else:
            self.save_state_data(country)
        if latest == False:
            if state is None:
                li2 = sortli(self.__all_state_data_list, key="state")
                return li2
            else:
                for fstate in self.__all_state_data_list:
                    if state == fstate['state']:
                        self.__state_data_list.append(fstate)
                return self.__state_data_list        
        else:
            if state is None:
                li=[]
                li2 = sortli(self.__all_state_data_list, key="confirmed", reverse=True)
                for lstate in self.__state_list:
                    for i in li2:
                        if i['state'] == lstate:
                            li.append(i)
                            break
                return li
            else:
                for fstate in self.__all_state_data_list:
                    if state == fstate['state']:
                        self.__state_data_list.append(fstate)
                        break
                return self.__state_data_list


        