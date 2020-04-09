from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from updater import updateData

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(updateData.update_data, 'interval', minutes=1440)
    scheduler.start()
