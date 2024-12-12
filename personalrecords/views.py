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
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['exercise', 'date_achieved']
    search_fields = ['exercise', 'notes']
    ordering_fields = ['date_achieved', 'weight', 'reps']

    def get_queryset(self):
        owner_id = self.request.query_params.get('owner', None)
        if owner_id:
            return PersonalRecord.objects.filter(
                    owner_id=owner_id).order_by('-date_achieved')
        elif self.request.user.is_authenticated:
            return PersonalRecord.objects.filter(
                owner=self.request.user).order_by('-date_achieved')
        else:
            return PersonalRecord.objects.all().order_by('-date_achieved')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PersonalRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a personal record, or update or delete it by id if users owns it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PersonalRecordSerializer
    queryset = PersonalRecord.objects.all().order_by('-date_achieved')
