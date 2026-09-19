from rest_framework.generics import GenericAPIView

from example.permissions import SamplePermission, NewPermission


# Create your views here.
class SampleView(GenericAPIView):
    permission_classes = [SamplePermission | NewPermission]
