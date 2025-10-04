
*Automation with Windows Task Scheduler

- Daily ETL script runs automatically at 9:00 AM.
- Configured in Windows Task Scheduler:
  - Task Name: Daily ETL Load
  - Trigger: Every day at 09:00
  - Action: Start a program
      - Program/script: C:\Users\ninik\Desktop\Python-Step-II\.venv\Scripts\python.exe
      - Arguments: C:\Users\ninik\Desktop\Python-Step-II\etl\load.py

i have presented here the image of Task scheduler <img width="1467" height="1132" alt="image" src="https://github.com/user-attachments/assets/cf5baed1-6f70-4364-964b-d6a4024cebbd" />

