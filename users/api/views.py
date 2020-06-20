from rest_framework.generics import ListAPIView
from .serializers import ProfileListSerializer
from ..models import Profile


class ProfileListAPIView(ListAPIView):
    serializer_class = ProfileListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Profile.objects.all()
        return queryset_list