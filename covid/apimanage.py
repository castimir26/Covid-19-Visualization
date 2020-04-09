from __future__ import unicode_literals
import json
#from django.db import migrations
from django.core.management import call_command
def load_file(apps, schema_editor):

    Survived = apps.get_model('survived', 'Survived')
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports'
    date = str((pd.to_datetime('today') - pd.Timedelta('5 days')).strftime('%m-%d-%Y'))
    url_date = '/'.join([url,date])
    file = '.csv'
    final_url = ''.join([url_date,file])
    frm = pd.read_csv(final_url)

    #your_model = YourModel.objects.create(key=p['key'], name=p['name'], tier=['tier'])
