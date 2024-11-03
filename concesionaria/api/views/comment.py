from rest_framework.viewsets import ModelViewSet

from cars.repositories.car_components_repository import CommentRepository
from cars.repositories.car_repository import CarsRepository
from api.serializers.comment_serializer import CommentSerializer

class CommentViewSet(ModelViewSet):
    commentRepo = CommentRepository()
    carRepo = CarsRepository()
    
    queryset = commentRepo.get_all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        carid = self.kwargs['carid']
        car = self.carRepo.get_by_id(carid)
        carComments = super().get_queryset().filter(car=car)
        return carComments
