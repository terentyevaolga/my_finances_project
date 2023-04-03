from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import MoneySlotSerializer
from web.models import MoneySlot


@api_view(["GET"])
@permission_classes([])
def main_view(request):
    return Response({'status': 'ok'})


class MoneyslotModelViewSet(ModelViewSet):
    serializer_class = MoneySlotSerializer

    def get_queryset(self):
        return MoneySlot.objects.all().select_related('user').prefetch_related('tags').filter(user=self.request.user)


class TagsViewSet(ModelViewSet):

    def get_queryset(self):
        return MoneySlotTag.objects.all().filter(user=self.request.user)
