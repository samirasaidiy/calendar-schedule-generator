# 🗓️ Calendar Schedule Generator

This is a personal Python script by [Samira](https://github.com/samirasaidiy) to create `.ics` calendar event files for Apple Calendar — perfect for organizing your work shifts with clean purple events.

---

## 🚀 Features

- Convert plain text work schedules into Apple Calendar events
- Automatically generates `.ics` files
- Timezone-aware (Europe/Berlin)
- Syncs to your iPhone via iCloud
- All events are added to your custom **purple "Samira Work" calendar**

---

## ✍️ How to Use

1. **Open the script** `schedule_creator.py` in VS Code.
2. In the section labeled `raw_schedule`, paste your schedule like this:

   ```python
   raw_schedule = """
   2025-07-01, 09:00, 14:00
   2025-07-02, 12:00, 17:00
   2025-07-05, 10:00, 16:00
   """Run the script:
python3 schedule_creator.py
The script creates work_schedule.ics.
Import into Apple Calendar:
Open Calendar app
Go to File → Import
Choose work_schedule.ics
Select your "Samira Work" calendar
✅ Your events are now in your calendar — correctly timed and beautifully color-coded.

📌 Requirements

Python 3.9+
ics and pytz libraries:
pip install ics pytz

Run the script:
python3 schedule_creator.py

The script creates work_schedule.ics.

Import into Apple Calendar:
Open Calendar app
Go to File → Import
Choose work_schedule.ics
Select your "Samira Work" calendar

 Your events are now in your calendar — correctly timed and beautifully color-coded.

📌 Requirements

Python 3.9+
ics and pytz libraries:
pip install ics pytz


Author :  Samira Saidiy

