import requests
from survived import models
from survived.models import Survived, World
import pandas as pd

from datetime import date, datetime, timedelta
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
new_update_place = 5

def world_totals(data, date):
    print("in world totals")

    current = World.objects.all()
    if current.exists():
        #print("exists")
        current_confirmed = current[0].confirmed
        #print(current_confirmed)
        current_recovered = current[0].recovered
        #print(current_recovered)
        current_deaths = current[0].deaths
        #print(current_deaths)
        current_active = current[0].active
        #print(current_active)
        final_confirmed = current_confirmed + data[new_confirm_place]
        #print(final_confirmed)
        final_recovered = current_recovered + data[new_recovered_place]
        #print(final_recovered)
        final_deaths = current_deaths + data[new_deaths_place]
        #print(final_deaths)
        final_active = current_active + data[new_active_place]
        #print(final_active)
        current.update(confirmed=final_confirmed, recovered=final_recovered, deaths=final_deaths, active=final_active)
    else:
        print("doesn't exist")
        new_world = World.objects.create(last_update=date, confirmed=data[new_confirm_place], recovered=data[new_recovered_place], deaths=data[new_deaths_place], active=data[new_active_place])
        new_world.save()
        print(new_world)





def create_new_totals(exist_obj, new_obj, date):
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
    exist_obj.update(last_update=date, province=province_now, country=country_now, confirmed=final_confirm, recovered=final_recovered, deaths=final_deaths, active=final_deaths)
    #print("Can update")
    #exist_obj.save()
    #print(exist_obj[0].confirmed)
    print("record saved")


def update_us(province, data, date):
    '''
    Since US data has to be rolled up into state-level data, while all other countries
    come in province/country format, this exists solely to reduce the number of US
    records.
    '''
    try:
        #print("Made it to US updates")
        print("Printing state: ", province)
        #print(type(province))
        us_total = Survived.objects.filter(province="total_us", country=data[3])
        #print("ok")
        p = Survived.objects.filter(province=province)
        #If this didn't work, create the record in the first place.
        #The above code is only possible based on how Django implements database
        #lookups.
        if not us_total:
            create_us = Survived.objects.create(last_update=date, province="total_us", country=data[3], confirmed=data[new_confirm_place], recovered=data[new_recovered_place], deaths=data[new_deaths_place], active=data[new_active_place])
            print(create_us)
            create_us.save()
        else:
            create_new_totals(us_total, data)

        if not p:
            print("none")
            q = Survived.objects.create(last_update=date, province=data[2], country=data[3], confirmed=data[new_confirm_place], recovered=data[new_recovered_place], deaths=data[new_deaths_place], active=data[new_active_place])
            print(q)
            q.save()
        #This is where we call the custom county roll-up code.
        else:
            create_new_totals(p, data)
    except Survived.DoesNotExist as e:
        print(e)


def update_world(country, data, date):
    print("updating non-world")
    try:
        print("Beginning country: ", country)
        p = Survived.objects.filter(country=country)
        if not p:
            q = Survived.objects.create(country=data[3], last_update=date, confirmed=data[new_confirm_place], recovered=data[new_recovered_place], deaths=data[new_deaths_place], active=data[new_active_place])
            q.save()

        #Some countries report the same province multiple times.
        #No idea why, but the data is messy. This SHOULD force all data to be
        #At province level.
        else:
            create_new_totals(p, data)
    except Survived.DoesNotExist as e:
        print(e)



def update_data():
    print("flushing data")
    Survived.objects.all().delete()
    print("reloading data please wait")
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
    d0 = date(2020, 1, 23)
    d1 = datetime.today().date()

    delta = d1 - d0
    #print(delta)
    for x in range(delta.days):
        print("in loop")
        #print(x)
        date_now = (datetime.now() - timedelta(days=(x+1))).strftime('%m-%d-%Y')
        #print(date_now)
        url_date = '/'.join([url,date_now])
        file = '.csv'
        final_url = ''.join([url_date,file])
        print(final_url)
        frm = pd.read_csv(final_url)
        #print("made a csv")
        if frm is not None:
            #print("frm is not none")
            try:
                print(len(frm))
                for x in range(len(frm)):
                    print(x)
                    print("going over csvs")
                    print("printing: ", frm.loc[x]["Province"])
                    if frm.loc[x]["Country_Region"] == "US":
                        print("us")
                        update_us(frm.loc[x]["Province_State"],frm.loc[x], date_now)
                    else:
                        print("world")
                        update_world(frm.loc[x]["Country_Region"],frm.loc[x], date_now)
                    world_totals(frm.loc[x], date_now)
                #print("finished adding")

            except:
                 pass
        else:
            print("Either date is wrong or epidemic is over. Congrats?")
