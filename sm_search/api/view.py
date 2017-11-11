from subprocess import check_output
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.conf import settings


class SearchProxy(GenericAPIView):

    def get(self, request, *args, **kwargs):
        search_type = request.GET.get('type', None)
        search_param = request.GET.get('param', None)
        if search_type is None or search_param is None:
            return Response(data={"error": "type or param not set"})
        exec_path = settings.SEARCH_ENGINE_PATH
        output = check_output([exec_path, search_type, search_param])
        return Response(output)
