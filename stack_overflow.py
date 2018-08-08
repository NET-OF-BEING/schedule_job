#!/usr/local/python2.7
import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=10)
def timed_job():
    print('This job is run every 10 seconds.')
    subprocess.call(["curl","https://stackoverflow.com/users/9536653/singulatirypanda"])

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def scheduled_job():
    print('This job is run every weekday at 10am.')

#sched.configure(options_from_ini_file)

#sched.add_job(timed_job, 'interval', seconds=10)
sched.start()

