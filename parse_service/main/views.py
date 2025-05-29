import json
from typing import Any, Dict, List, Optional

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ObjectDoesNotExist

from .services import add_new_page, get_page_data_by_id, get_page_list
from .models import ParsedPage


@csrf_exempt
@require_POST
def create_page(request: HttpRequest) -> JsonResponse:
    try:
        data: Dict[str, Any] = json.loads(request.body)
        url: Optional[str] = data.get("url")

        if not url:
            return JsonResponse({"error": "URL parameter is required"}, status=400)

        saved_page_id: int = add_new_page(url)
        return JsonResponse({"id": saved_page_id})
    except RuntimeError as e:
        return JsonResponse({"Error": f"{str(e)}"}, status=400)


@require_GET
def get_object(request: HttpRequest, object_id) -> JsonResponse:
    try:
        parsed_page: ParsedPage = get_page_data_by_id(object_id)
        page_json: Dict[str, Any] = {
            "url": parsed_page.url,
            "h1": parsed_page.h1_count,
            "h2": parsed_page.h2_count,
            "h3": parsed_page.h3_count,
            "a": parsed_page.links,
        }
        return JsonResponse(page_json)
    except ObjectDoesNotExist:
        return JsonResponse({"error": f"Object not found for object_id={object_id}"}, status=404)


@require_GET
def get_list(request: HttpRequest) -> JsonResponse:
    order_value: Optional[str] = request.GET.get("order", None)
    sort_field: str = ""
    field_name: Optional[str] = None
    if order_value is not None:
        sort_field = "-" if order_value.startswith('-') else ""
        field_name = order_value.lstrip('-')

        if field_name not in ["h1", "h2", "h3", "a"]:
            return JsonResponse({"error": "Invalid value in order parameter"}, status=400)

    parsed_pages: List[Dict] = get_page_list(sort_field, field_name)
    return JsonResponse(parsed_pages, safe=False)
