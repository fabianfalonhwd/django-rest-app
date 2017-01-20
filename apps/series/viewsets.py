from rest_framework import viewsets
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .models import Serie
from .serializers import SerieSerializer


class SerieViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    paginate_by = 10

    def create(self, request):
        Serie.objects.create(
            name=request.POST['name'],
            release_date=request.POST['release_date'],
            rating=request.POST['rating'],
            category=request.POST['category'])
        return Response(status=status.HTTP_201_CREATED)
