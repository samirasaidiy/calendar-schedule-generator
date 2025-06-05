from ics import Calendar, Event
from datetime import datetime
from pytz import timezone
import webbrowser
import os

# Set your local timezone
local_tz = timezone('Europe/Berlin')

def create_event(title, date_str, start_time, end_time):
    event = Event()
    event.name = f"🟣 {title} (Samira Work)"

    start_naive = datetime.strptime(f"{date_str} {start_time}", "%Y-%m-%d %H:%M")
    end_naive = datetime.strptime(f"{date_str} {end_time}", "%Y-%m-%d %H:%M")

    event.begin = local_tz.localize(start_naive)
    event.end = local_tz.localize(end_naive)
    return event

def main():
    # ✅ Update this list with your real schedule
    raw_schedule = """
    2025-06-10, 12:00, 17:00
    2025-06-11, 12:00, 17:00
    2025-06-24, 13:00, 17:00
    2025-06-05, 12:00, 13:00
    """

    calendar = Calendar()
    for line in raw_schedule.strip().splitlines():
        date_str, start, end = [x.strip() for x in line.split(",")]
        event = create_event("Work", date_str, start, end)
        calendar.events.add(event)

    filename = "work_schedule.ics"
    with open(filename, "w") as f:
        f.writelines(calendar)

    print(f"✅ Saved calendar to: {os.path.abspath(filename)}")
    webbrowser.open(filename)

if __name__ == "__main__":
    main()
