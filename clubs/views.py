from django.shortcuts import render
from rest_framework import filters

from .models import Club, ClubImage, Table, Reservation, ComputerClub, Announcement, PriceList, Game, ClubRules, GameAccessoriesSpecification
from .serializers import ClubSerializer, ClubImageSerializer, TableSerializer, ReservationSerializer, ComputerClubSerializer, AnnouncementSerializer, \
    PriceListSerializer, GameSerializer, ClubRulesSerializer, GameAccessoriesSpecificationSerializer
from .permissions import IsAdminUserClubCreate, IsAdminOrCreateClub

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ClubView(ModelViewSet):
    queryset = Club.objects.prefetch_related('club_image', 'club_table', 'club_reservation',
        'price_list', 'game_list', 'club_rules_list', \
        'game_accessories_specification_list').select_related('computer_club')
    serializer_class = ClubSerializer 
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )

class AnnouncementView(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminOrCreateClub, )

class ComputerClubView(ModelViewSet):
    queryset = ComputerClub.objects.prefetch_related('announcement_computer_club', 'club_computer_club')
    serializer_class = ComputerClubSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminOrCreateClub, )

class ClubImageView(ModelViewSet):
    queryset = ClubImage.objects.all()
    serializer_class = ClubImageSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )

class TableView(ModelViewSet):
    queryset = Table.objects.prefetch_related('seats_reservation')
    serializer_class = TableSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )

class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, ) 
    lookup_field = 'pk'

class PriceListView(ModelViewSet):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )

class GameView(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['game']

class ClubRulesView(ModelViewSet):
    queryset = ClubRules.objects.all()
    serializer_class = ClubRulesSerializer
    lookup_field = 'pk'
    permission_classes = (IsAdminUserClubCreate, )

class GameAccessoriesSpecificationView(ModelViewSet):
    queryset = GameAccessoriesSpecification.objects.all()
    serializer_class = GameAccessoriesSpecificationSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['game_accessories_specification']
    permission_classes = (IsAdminUserClubCreate, )