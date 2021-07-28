from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from ..models import Meta
from rest_framework.permissions import AllowAny

fields = ['bannerTitle', 'bannerText', 'bannerImage', 'aboutUsText', 'aboutUsImage', 'lastPostsText', 'contactUsText']


class MetaView(RetrieveAPIView):
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        query = Meta.objects.filter(key__in=fields)
        metas = {}
        for meta in query:
            metas[meta.key] = {"value": meta.value, "image": meta.image.url if meta.image else None}
        return Response(metas)
