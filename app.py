import dramatiq
from dramatiq.brokers.redis import RedisBroker
import settings


broker = RedisBroker(url=settings.REDIS_URL)

dramatiq.set_broker(broker)
