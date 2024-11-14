from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from chalk_talk_api.permissions import IsOwnerOrReadOnly
from .models import PersonalRecord
from .serializers import PersonalRecordSerializer


class PersonalRecordList(generics.ListCreateAPIView):
    """ 
    List personal records or create one if logged in
    """
    serializer_class = PersonalRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PersonalRecord.objects.all().order_by('-date_achieved')
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
    filterset_fields = ['exercise', 'date_achieved']
    search_fields = ['exercise', 'notes']
    ordering_fields = ['date_achieved', 'weight', 'reps']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PersonalRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a personal record, or update or delete it by id if users owns it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PersonalRecordSerializer
    queryset = PersonalRecord.objects.all().order_by('-date_achieved')
