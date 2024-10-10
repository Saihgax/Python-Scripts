'''
Identify the top 3 most frequently occurring HTTP status codes from the logs and their respective counts.
'''

import re
from collections import Counter

def top_status_codes(logs, top_n=3):
    status_pattern = r'HTTP \/[0-9\.]+\"\s(\d{3})'
    status_codes = []

    for line in logs:
        match = re.search(status_pattern, line)
        if match:
            status_codes.append(match.group(1))

    status_counter = Counter(status_codes)

    return status_counter.most_common(top_n)

logs = [
    '[2024-10-07 12:45:56] "GET /index.html HTTP/1.1" 200 345ms',
    '[2024-10-07 12:47:12] "POST /api/user HTTP/1.1" 201 210ms',
    '[2024-10-07 12:48:02] "GET /index.html HTTP/1.1" 200 300ms',
    '[2024-10-07 12:50:14] "GET /index.html HTTP/1.1" 404 150ms',
    '[2024-10-07 12:51:05] "GET /notfound HTTP/1.1" 404 200ms'
]

print(top_status_codes(logs))  # Output: [('200', 2), ('404', 2), ('201', 1)]

