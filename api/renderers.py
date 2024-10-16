from icecream import ic
from rest_framework import status
from rest_framework.renderers import JSONRenderer


class ApiRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        ic(renderer_context['request'].__dict__)
        if not str(status_code).startswith('2'):
            data = None
        response = {
          # "status": 'a',
          "code": status_code,
          "data": data,
        }

        return super(ApiRenderer, self).render(response, accepted_media_type, renderer_context)