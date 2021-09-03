import time

import requests
from datetime import datetime

AUTH = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SWQiOiI5NzExMDE0NCIsImNyZWF0ZWRBdCI6MTYzMDY2MDQ4ODc1Miwic3VwZXJVc2VyIjpmYWxzZSwiaWF0IjoxNjMwNjYwNDg4fQ.q5sHBEYhQR3N0XeGDpXiRCFN2HbwyC-UDEAHh-YnNbA"
RAND = 11
# List of (course_id, units)
COURSES = [
    ("40324-1", 3),  # ‌بازیابی

    ("40364-1", 3),  # ‌طراحی زبان
    ("40717-2", 3),  # یادگیری ماشین

    ("40456-1", 3),  # نظریه بازی
    ("40494-1", 3),  # بیو

    ("40419-1", 3),  # وب
    ("40462-1", 3),  # نهفته

    ("40474-1", 3),  # مهندسی نرم‌افزار

    ("37446-8", 2),  # ابوالحسینی
    ("37447-4", 2),  # طباطبائی
    ("37447-2", 2),  # یحیی صباغچی فیروز آباد
    ("37446-4", 2),  # فیضی
    ("37446-2", 2),  # فیضی
    ("37446-6", 2),  # صباغچی


    # ("40424-1", 3),  # ok
]

while datetime.now().hour != RAND:
    # break
    time.sleep(0.00001)
    continue
time.sleep(0.1)
for course in COURSES:
    print(course)
    cnt = 0
    while cnt < 5:
        cnt += 1
        print('try')
        result = requests.post(
            url="https://my.edu.sharif.edu/api/reg",
            headers={
                "authorization": AUTH,
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "origin": "https://my.edu.sharif.edu",
                "pragma": "no-cache",
                "referer": "https://my.edu.sharif.edu/courses/marked",
                "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                "sec-ch-ua-mobile": "?0",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            },
            data={
                "action": "add",
                "course": course[0],
                "units": course[1]
            }
        )

        print(result.text)
        try:
            print(result.json()['jobs'][0]['result'])
        except Exception:
            pass
        if "REPEATED_REQUEST" in result.text or result.json()['jobs'][0]['result'] == 'REGISTRATION_TIME_LIMIT':
            time.sleep(1)
            continue
        break
    # exit(0)
