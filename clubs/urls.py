from django.urls import path
from clubs.views import ComputerClubView, ClubView, ClubImageView, TableView, ReservationView, AnnouncementView, \
    PriceListView, GameView, ClubRulesView, GameAccessoriesSpecificationView

#from rest_framework.routers import DefaultRouter


"""router = DefaultRouter()
router.register(r'computer_clubs', ComputerClubView, basename='computer_clubs')
slovar0 = {'get': 'list', 'post': 'create'}
slovar1 = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
"""

urlpatterns = [
    path('computer_clubs/', ComputerClubView.as_view({'get': 'list', 'post': 'create'})),
    path('computer_clubs/<int:pk>/', ComputerClubView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('club/', ClubView.as_view({'get': 'list', 'post': 'create'})),
    path('club/<int:pk>/', ClubView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('club_image/', ClubImageView.as_view({'get': 'list', 'post': 'create'})),
    path('club_image/<int:pk>/', ClubImageView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('table/', TableView.as_view({'get': 'list', 'post': 'create'})),
    path('table/<int:pk>/', TableView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('reservation/', ReservationView.as_view({'get': 'list', 'post': 'create'})),
    path('reservation/<int:pk>/', ReservationView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('announcement/', AnnouncementView.as_view({'get': 'list', 'post': 'create'})),
    path('announcement/<int:pk>/', AnnouncementView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('price_list/', PriceListView.as_view({'get': 'list', 'post': 'create'})),
    path('price_list/<int:pk>/', PriceListView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('game/', GameView.as_view({'get': 'list', 'post': 'create'})),
    path('game/<int:pk>/', GameView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('club_rules/', ClubRulesView.as_view({'get': 'list', 'post': 'create'})),
    path('club_rules/<int:pk>/', ClubRulesView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),

    path('game_accessories_specification/', GameAccessoriesSpecificationView.as_view({'get': 'list', 'post': 'create'})),
    path('game_accessories_specification/<int:pk>/', GameAccessoriesSpecificationView.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'})),
]

#urlpatterns += router.urls