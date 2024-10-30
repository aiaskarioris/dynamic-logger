r"""Helper class for logging

Allows for printing messages with selectable log levels as well as
measuring time in execution.

"""

import time

class DynLogger():
    def __init__(self, enabled=True, loglevel=5):
        self.enabled=enabled
        self.loglevel=loglevel
        self.timers = []
    
    def print(self, msg, loglevel=5):
        if self.loglevel >= loglevel:
            print(msg)

    # Starts a timer; Multiple `start_timer`
    # can be called without a `stop_timer` call.
    # When `stop_timer` is called, the last
    # timer started will be used.
    # The new timer's ID is returned
    def startTimer(self):
        self.timers.append(time.monotonic_ns())
        return len(self.timers) - 1
    
    # Stops the timer started last and returns
    # the ellapsed. Returns the nanoseconds ellapsed
    def stopTimer(self):
        end_time = time.monotonic_ns()
        start_time = self.timers.pop()
        return end_time-start_time


