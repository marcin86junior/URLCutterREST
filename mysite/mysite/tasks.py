from celery import shared_task
from celery.utils.log import get_task_logger

#from urlcut.models import Link

logger = get_task_logger(__name__)

@shared_task
def sample_task(x=2, y=2):
    #links = Link.objects.filter(count=0)
    #links.delete()
    logger.info("The sample test - remove all links never used every minute.")
    return x + y

@shared_task
def collect_data_task():
    from urlcut.models import Links
    logger.info("Working 1...")
    # do something

@shared_task
def backup_task():
    from urlcut.models import Links
    logger.info("Working 2...")
    # do something
