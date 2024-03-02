import calendar 
class Event:
    def __init__(self, name, start_time, end_time=None, location=None, description=None):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.description = description

    def __str__(self):
        if self.end_time:
            return f"{self.name} from {self.start_time} to {self.end_time}"
        else:
            return f"{self.name} at {self.start_time}"

class CalendarDay:
    def __init__(self, date):
        self.date = date
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_events(self):
        return self.events

    def __str__(self):
        events_info = '\n'.join(str(event) for event in self.events)
        return f"Date: {self.date.strftime('%Y-%m-%d')}\nEvents:\n{events_info}"

# Example usage
date = datetime(2024, 3, 1)
day = CalendarDay(date)

# Add events to the day
event1 = Event("Meeting with John", datetime(2024, 3, 1, 10, 0), datetime(2024, 3, 1, 11, 0), "Office", "Discuss project")
event2 = Event("Lunch", datetime(2024, 3, 1, 12, 0), datetime(2024, 3, 1, 13, 0), "Restaurant", "Meet with friends")
event3 = Event("Gym", datetime(2024, 3, 1, 17, 30), datetime(2024, 3, 1, 19, 0), "Gym", "Workout session")

day.add_event(event1)
day.add_event(event2)
day.add_event(event3)

# Print the day's information
print(day)




