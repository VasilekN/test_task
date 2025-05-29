import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.core.exceptions import ObjectDoesNotExist
from .services import add_new_page, get_page_data_by_id, get_page_list


@csrf_exempt
@require_POST
def create_page(request):
    try:
        data = json.loads(request.body)
        url = data.get("url")

        if not url:
            return JsonResponse({"error": "URL parameter is required"}, status=400)

        saved_page_id = add_new_page(url)
        return JsonResponse({"id": saved_page_id})
    except RuntimeError as e:
        return JsonResponse({"Error": f"{str(e)}"}, status=400)


@require_GET
def get_object(request, object_id):
    try:
        parsed_page = get_page_data_by_id(object_id)
        page_json = {
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
def get_list(request):
    order_value = request.GET.get("order", None)
    sort_field = field_name = None
    if order_value is not None:
        sort_field = "-" if order_value.startswith('-') else ""
        field_name = order_value.lstrip('-')

        if field_name not in ["h1", "h2", "h3", "a"]:
            return JsonResponse({"error": "Invalid value in order parameter"}, status=400)

    parsed_pages = get_page_list(sort_field, field_name)
    return JsonResponse(parsed_pages, safe=False)
