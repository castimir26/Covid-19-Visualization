import requests
from survived import models
from survived.models import Survived
import pandas as pd
import datetime
import numpy as np

'''
Implements the Python Advanced Scheduler to update the data in the database.
'''

#I got lazy and made some globals
#Please don't hate me
new_confirm_place = 7
new_recovered_place = 9
new_deaths_place = 8
new_active_place = 10


def create_new_totals(exist_obj, new_obj):
    '''
    The county records for the US have to be agglomerated into state records.
    I could extend the app to include county data at some point, but currently
    the scope of the project didn't allow for it.
    '''
    #I left a bunch of diagnostic printouts in case I have problems with the description
    #Will have to refactor at some point as a debug option
    #print("create new totals")
    #Create a copy of the old data
    current_confirmed = exist_obj[0].confirmed

    current_recovered = exist_obj[0].recovered

    current_deaths = exist_obj[0].deaths

    current_active = exist_obj[0].active

    #aggregate all province data
    final_confirm = new_obj[new_confirm_place] + current_confirmed
    final_recovered = new_obj[new_recovered_place] + current_recovered
    final_deaths = new_obj[new_deaths_place] + current_deaths
    final_active = new_obj[new_active_place] + current_active
    province_now = new_obj[2]
    country_now = new_obj[3]
    #print("old: ", exist_obj[0].confirmed)
    exist_obj.update(province=province_now, country=country_now, confirmed=final_confirm, recovered=final_recovered, deaths=final_deaths, active=final_deaths)
    #print("Can update")
    #exist_obj.save()
    #print(exist_obj[0].confirmed)
    #print("record saved")


def update_us(province, data):
    '''
    Since US data has to be rolled up into state-level data, while all other countries
    come in province/country format, this exists solely to reduce the number of US
    records.
    '''
    try:
        #print("Made it to US updates")
        #print("Printing state: ", province)
        print(type(province))

        p = Survived.objects.filter(province=province)
        #If this didn't work, create the record in the first place.
        #The above code is only possible based on how Django implements database
        #lookups.
        if not p:
            #print("none")
            q = Survived.objects.create(province=data[2], country=data[3], confirmed=data[new_confirm_place], recovered=data[new_recovered_place], deaths=data[new_deaths_place], active=data[new_active_place])
            print(q)
            q.save()
        #This is where we call the custom county roll-up code.
        else:
            create_new_totals(p, data)
    except Survived.DoesNotExist as e:
        print(e)


def update_world(country, data):
    try:
        #print("Beginning country: ", country)
        p = Survived.objects.filter(country=country)
        if not p:
            q = Survived.objects.create(country=data[3], confirmed=data[new_confirm_place], recovered=data[new_recovered_place], deaths=data[new_deaths_place], active=data[new_active_place])
            q.save()

        #Some countries report the same province multiple times.
        #No idea why, but the data is messy. This SHOULD force all data to be
        #At province level.
        else:
            create_new_totals(p, data)
    except Survived.DoesNotExist as e:
        print(e)



def update_data():
    print("reloading data please wait")
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
    date = str((pd.to_datetime('today') - pd.Timedelta('2 days')).strftime('%m-%d-%Y'))
    url_date = '/'.join([url,date])
    file = '.csv'
    final_url = ''.join([url_date,file])
    frm = pd.read_csv(final_url)

    if frm is not None:
        try:

            for x in range(len(frm)):
                if frm.loc[x]["Country_Region"] == "US":
                    update_us(frm.loc[x]["Province_State"],frm.loc[x])
                else:
                    update_world(frm.loc[x]["Country_Region"],frm.loc[x])
            #print("finished adding")

        except:
            pass
    else:
        print("Either date is wrong or epidemic is over. Congrats?")
