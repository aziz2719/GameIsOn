from django.shortcuts import render
from rest_framework import filters

from .models import Club, ClubImage, Table, Reservation, ComputerClub, Announcement, PriceList, Game, ClubRules, GameAccessoriesSpecification
from .serializers import ClubSerializer, ClubImageSerializer, TableSerializer, ReservationSerializer, ComputerClubSerializer, AnnouncementSerializer, \
    PriceListSerializer, GameSerializer, ClubRulesSerializer, GameAccessoriesSpecificationSerializer
from .permissions import IsAdminUserClubCreate, IsAdminOrCreateClub

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class AnnouncementView(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminOrCreateClub, )

class ComputerClubView(ModelViewSet):
    queryset = ComputerClub.objects.prefetch_related('announcement_computer_club')
    serializer_class = ComputerClubSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminOrCreateClub, )
    #http_method_names = ['get', 'post']

class ClubView(ModelViewSet):
    queryset = Club.objects.prefetch_related('club_image', 'club_table', 'club_reservation', 'price_list', 'game_list', 'club_rules_list', \
        'game_accessories_specification_list').select_related('computer_club') # префетч есть связь от род класса clubs.Club селект дочерний clubs.computer_club если нету связи от род
    serializer_class = ClubSerializer 
    lookup_field = 'pk'
    #permission_classes = (IsAdminUserClubCreate, )

class ClubImageView(ModelViewSet):
    queryset = ClubImage.objects.all()
    serializer_class = ClubImageSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminUserClubCreate, )

class TableView(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminUserClubCreate, )

class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    #permission_classes = (IsAuthenticated, ) 
    lookup_field = 'pk'

    """def create(self, request, *args, **kwargs):
        'computer_club', 'owner', 'seats', 'date_slot', 'time1', 'time2', 'using_time', 'status2'
        computer_club = request.data.get('computer_club')
        user = request.user.owner_reservation
        seats = request.data.get('seats')
        time = request.data.get('time1')
        using_time = request.data.get('using_time')
        status = request.data.get('status2')
        resrvation = Reservation.objects.create(club=computer_club, client=user, seats=seats, \
            time=time, using_time=using_time, status=status)
        for seat in seats:
            self.status = Table.objects.get(id=seats.get('seats_id')).status
            status = self.status
            OrderProducts.objects.create(
                order=order_created,
                product_id=product.get('product_id'),
                count=product.get('count')
            )
        order_created.total_price = total_sum
        order_created.save()
        return Response('Success')"""

class PriceListView(ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminUserClubCreate, )

class GameView(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminUserClubCreate, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['game']

class ClubRulesView(ModelViewSet):
    queryset = ClubRules.objects.all()
    serializer_class = ClubRulesSerializer
    lookup_field = 'pk'
    #permission_classes = (IsAdminUserClubCreate, )

class GameAccessoriesSpecificationView(ModelViewSet):
    queryset = GameAccessoriesSpecification.objects.all()
    serializer_class = GameAccessoriesSpecificationSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['game_accessories_specification']
    #permission_classes = (IsAdminUserClubCreate, )