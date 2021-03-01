from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from validators import url as validate_url
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from .models import UrlModel
from .utils import encode, get_url_idx
from app.settings import SITE_NAME


@csrf_exempt
def index_view(request):
    if request.method == 'POST':
        long_url = request.POST.get('original_url', '')
        #    Для избежания дублирования в БД используется get_or_create
        if not validate_url(long_url):
            return HttpResponse("Not valid url is got", status=status.HTTP_400_BAD_REQUEST)
        url = UrlModel.objects.get_or_create(original_url=long_url)
        short_url = SITE_NAME + encode(url[0].id)
        return HttpResponse(short_url, status=status.HTTP_200_OK)

@csrf_exempt
def decode_view(request, code):
    try:
        id = get_url_idx(code)
        url = UrlModel.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("There is no such url", status=status.HTTP_400_BAD_REQUEST)

    return redirect(url.original_url)



