
import json
import urllib.request
import pandas as pd
import requests
from datetime import datetime
from django.db import migrations

def load_file(apps, schema_editor):

   Survived = apps.get_model('survived', 'Survived')
   url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
   date = str((pd.to_datetime('today') - pd.Timedelta('5 days')).strftime('%m-%d-%Y'))
   url_date = '/'.join([url,date])
   file = '.csv'
   final_url = ''.join([url_date,file])
   frm = pd.read_csv(final_url)
   print(frm.columns)
   Data = apps.get_model('survived','Survived')

   for x in range(len(frm)):
       #print(frm.loc[x]['Country_Region'])

       p = Survived(province=frm.loc[x]["Province_State"],country=frm.loc[x]["Country_Region"],confirmed=frm.loc[x]["Confirmed"],deaths=frm.loc[x]["Deaths"],recovered=frm.loc[x]["Recovered"],active=frm.loc[x]["Active"])
       p.save()

           #p.province = prov[0]
           #p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('survived', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_file)
    ]
