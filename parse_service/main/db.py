from typing import Dict, Any, Optional, List
from .models import ParsedPage


def save_page(page_data: Dict[str, Any], url: str) -> int:
    saved_page: ParsedPage = ParsedPage.objects.create(
        url=url,
        h1_count=page_data.get("h1_count"),
        h2_count=page_data.get("h2_count"),
        h3_count=page_data.get("h3_count"),
        links=page_data.get("links"),
    )
    return saved_page.id


def get_page_by_id(object_id: int) -> Optional[ParsedPage]:
    return ParsedPage.objects.get(id=object_id)


def get_page_data(order_param: str) -> List[ParsedPage] :
    return ParsedPage.objects.all().order_by(order_param)
