class Time:

    @staticmethod
    def cont_time(distance, speed):
        time = distance / speed
        return time


print(Time.cont_time(500, 100))
