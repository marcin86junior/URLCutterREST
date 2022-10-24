from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def test_task():
    from urlcut.models import Link
    links = Link.objects.filter(count=0)
    logger.info("Test task - remove links never used every minute")
    links.delete()

@shared_task
def remove1_task():
    from urlcut.models import Link
    from datetime import datetime, timedelta
    links = Link.objects.filter(created_at__range=["2020-01-01", datetime.now()-timedelta(hours=24)]).filter(count=0)
    logger.info('Removed links never used - 1 day from "create time"')
    links.delete()

@shared_task
def remove2_task():
    from urlcut.models import Link
    from datetime import datetime, timedelta
    links = Link.objects.filter(last_time_used__range=["2020-01-01", datetime.now()-timedelta(days=5)])
    logger.info('Removed used links - 5 day from "last time used"')
    links.delete()
