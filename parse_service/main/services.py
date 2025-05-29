import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional, Any
from .db import save_page, get_page_by_id, get_page_data
from .models import ParsedPage


def parse_content(response_text: str) -> Dict[str, Any]:
    soup = BeautifulSoup(response_text, "html.parser")

    h1_count: int = len(soup.find_all("h1"))
    h2_count: int = len(soup.find_all("h2"))
    h3_count: int = len(soup.find_all("h3"))
    a_tags: set = set([a.get("href") for a in soup.find_all("a", href=True)])

    data: Dict[str, Any] = {
        "h1_count": h1_count,
        "h2_count": h2_count,
        "h3_count": h3_count,
        "links": list(a_tags)
    }
    return data


def add_new_page(url: str) -> Optional[int]:
    try:
        response: requests.Response = requests.get(url, timeout=10)
        if not response.ok:
            raise RuntimeError("Failed to fetch url")
    except:
        raise RuntimeError("Failed to fetch url")

    page_data: Dict[str, Any] = parse_content(response.text)
    return save_page(page_data, url)


def get_page_data_by_id(object_id: int) -> Optional[ParsedPage]:
    return get_page_by_id(object_id)


def get_page_list(sort_field: str, field_name: Optional[str]) -> List[Dict[str, Any]]:
    if field_name is None:
        order_param: str = "created_at"
    else:
        order_param: str = f"{sort_field}links" if field_name == "a" else f"{sort_field}{field_name}_count"

    parsed_pages: List[ParsedPage] = get_page_data(order_param)

    data: List[Dict[str, Any]] = []
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
