import requests


def get_courses(url):
    return requests.get(url).json()

def has_course(query, title, description):
    query = query.lower()
    return query in title.lower() or query in description.lower()

def get_query_from_user_input(input):
    splitted_input = input.split(' ')
    if len(splitted_input) == 1:
        return None
    return ' '.join(splitted_input[1:])