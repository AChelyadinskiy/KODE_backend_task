from rest_framework.views import APIView
from subscriptions.serializers import SubDetailSerializer
from rest_framework.response import Response
from subscriptions.models import Subscription


class SubCreateView(APIView):
    def get(self, request):
        queryset = Subscription.objects.all()
        serializer = SubDetailSerializer(queryset, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        subs = SubDetailSerializer(data=request.data)
        if subs.is_valid():
            email = subs.validated_data["email"]
            if "min_price" not in subs.validated_data and "max_price" not in subs.validated_data:
                return Response({"Error": "Не указано ни макисмальной, ни минимальной цены"}, status=400)
            sub = Subscription.objects.filter(ticker=subs.validated_data["ticker"], email=subs.validated_data["email"])
            if len(sub) > 0:
                return Response({"Error": "Такая подписка уже есть"}, status=400)
            count = Subscription.objects.filter(email=email).count()
            if count < 5:
                subs.save()
                return Response({"id": subs.data["id"]}, status=201)
            else:
                return Response({"Error": "На эту почту уже есть 5 подписок"}, status=400)
        else:
            return Response({"Errors": subs.errors}, status=400)

    def delete(self, request):
        if "email" in request.GET:
            if "ticker" in request.GET:
                sub_to_del = Subscription.objects.filter(ticker=request.GET["ticker"], email=request.GET["email"])
                if len(sub_to_del) < 1:
                    return Response({"Error": "Такой подписки не существует"}, status=400)
                sub_to_del.delete()
                return Response({"Success": "Запись удалена"}, status=200)
            else:
                queryset = Subscription.objects.filter(email=request.GET["email"])
                count = queryset.count()
                for sub in Subscription.objects.all():
                    if sub.email == request.GET["email"]:
                        sub.delete()
                return Response({"Success": "Удалено {} записей".format(count)}, status=200)
        return Response({"Error": "Неверный запрос"}, status=400)
