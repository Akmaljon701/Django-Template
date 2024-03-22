from rest_framework.decorators import throttle_classes
from rest_framework.throttling import UserRateThrottle


class IPThrottle(UserRateThrottle):
    rate = '1/min'   # 1 minute block after one request

# @throttle_classes([IPThrottle])  # for api functions
# throttle_classes = [IPThrottle]  # for api classes
