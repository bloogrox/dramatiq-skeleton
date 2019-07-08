from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from tasks.sample import sample


if __name__ == "__main__":
    scheduler = BlockingScheduler()

    scheduler.add_job(
        sample.send,
        CronTrigger.from_crontab("* * * * *"),
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
