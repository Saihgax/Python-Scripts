from datetime import datetime
from pprint import pprint

def sort_dict_by_date_string(dicts):
    sorted_list = sorted(
        dicts,
        key=lambda x: (datetime.strptime(x['date'], '%Y-%m-%d'), x['number'])
    )

    return sorted_list


# Example list of dictionaries
data = [
    {"date": "2023-09-01", "string": "apple", "number": 2},
    {"date": "2023-08-30", "string": "banana", "number": 5},
    {"date": "2023-09-01", "string": "orange", "number": 3},
    {"date": "2023-08-30", "string": "apple", "number": 4}
]

sorted_data = sort_dict_by_date_string(data)
pprint(sorted_data)