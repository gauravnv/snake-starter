import time

def timer(handler):
    def timer_wrapper(*args, **kwargs):
        start = int(round(time.time() * 1000))
        res = handler()
        end = int(round(time.time() * 1000))
        delta = end - start
        print "Response time: %d ms" % delta
    return timer_wrapper
