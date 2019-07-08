from app import dramatiq
import settings


@dramatiq.actor(max_retries=1)
def sample():
    print("Hello from dramatiq")
