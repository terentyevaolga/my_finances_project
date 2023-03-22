from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.serializers import MoneySlotSerializer
from web.models import MoneySlot


@api_view(["GET"])
@permission_classes([])
def main_view(request):
    return Response({'status': 'ok'})


@api_view(["GET"])
def moneyslots_view(request):
    money_slots = MoneySlot.objects.all().select_related('user').prefetch_related('tags')
    serializer = MoneySlotSerializer(money_slots, many=True)
    return Response(serializer.data)


