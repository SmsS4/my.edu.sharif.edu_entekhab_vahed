import time

import requests
from datetime import datetime
AUTH = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdHVkZW50SWQiOiI5NzExMDE0NCIsImNyZWF0ZWRBdCI6MTYxMjMyODUzMTIwNiwic3VwZXJVc2VyIjpmYWxzZSwiaWF0IjoxNjEyMzI4NTMxfQ.cYWiXuO9PPSvF_mkmrW9DuW9wyI2sk3qX9CkCHBdSBs"
RAND = 9
# List of (course_id, units)
COURSES = [
    ("40418-1", 3),  # Tahlil system
    ("40634-1", 3),  # Shabih sazi
    ("40429-1", 3),  # Mobile
    ("40415-1", 3),  # Nzarayi zaban
    ("37123-2", 2),  # Akhlagh
    ("37123-4", 2),  # Akhlagh
    ("37127-2", 2),  # Ayin
    ("40203-6", 1),  # DSD
    ("40203-5", 1),  # DSD
    ("40203-1", 1),  # DSD
    ("30004-18", 1),  # ٰVarzesh
    ("30004-11", 1),  # ٰVarzesh
]

while datetime.now().hour != RAND:
    break
    time.sleep(0.00001)
    continue
for course in COURSES:
    print(course)
    while True:
        print(course, AUTH)
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
    exit(0)
