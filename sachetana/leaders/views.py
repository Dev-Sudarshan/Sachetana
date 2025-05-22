from rest_framework import viewsets, generics
from .models import Leader
from .serializers import LeaderSerializer

class LeaderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LeaderSerializer

    def get_queryset(self):
        province = self.request.query_params.get('province')
        if province:
            return Leader.objects.filter(province=province)
        else:
            return Leader.objects.all()

class LeaderDetailView(generics.RetrieveAPIView):
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    lookup_field = 'id'  # Use 'id' as the lookup field

class PromiseViewSet(viewsets.ReadOnlyModelViewSet): # added PromiseViewSet
    queryset = Promise.objects.all()
    serializer_class = PromiseSerializer

# Create your views here.
