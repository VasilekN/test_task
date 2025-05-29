import requests
from bs4 import BeautifulSoup
from .db import save_page, get_page_by_id, get_page_data


def parse_content(response_text):
    soup = BeautifulSoup(response_text, "html.parser")

    h1_count = len(soup.find_all("h1"))
    h2_count = len(soup.find_all("h2"))
    h3_count = len(soup.find_all("h3"))
    a_tags = set([a.get("href") for a in soup.find_all("a", href=True)])

    data = {
        "h1_count": h1_count,
        "h2_count": h2_count,
        "h3_count": h3_count,
        "links": list(a_tags)
    }

    return data


def add_new_page(url):
    try:
        response = requests.get(url, timeout=10)
        if not response.ok:
            raise RuntimeError("Failed to fetch url")
    except:
        raise RuntimeError("Failed to fetch url")

    page_data = parse_content(response.text)
    return save_page(page_data, url)


def get_page_data_by_id(object_id):
    return get_page_by_id(object_id)


def get_page_list(sort_field, field_name):
    if field_name is None:
        order_param = "created_at"
    else:
        order_param = f"{sort_field}links" if field_name == "a" else f"{sort_field}{field_name}_count"

    parsed_pages = get_page_data(order_param)

    data = []
    for page in parsed_pages:
        data.append({
            "url": page.url,
            "h1": page.h1_count,
            "h2": page.h2_count,
            "h3": page.h3_count,
            "a": page.links if page.links else [],
            "created_at": page.created_at
        })
    return data
