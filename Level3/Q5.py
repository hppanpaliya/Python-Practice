class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = (self.hours * 60 + self.minutes) + \
                       (other_time.hours * 60 + other_time.minutes)
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

    def displayTime(self):
        return f"{self.hours} hr and {self.minutes} min"

    def displayMinute(self):
        return self.hours * 60 + self.minutes


if __name__ == '__main__':
    t1 = Time(2, 50)
    t2 = Time(1, 20)
    result = t1.addTime(t2)
    assert result.displayTime() == "4 hr and 10 min"

    t3 = Time(1, 2)
    assert t3.displayMinute() == 62

    