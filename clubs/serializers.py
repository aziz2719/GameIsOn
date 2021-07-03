from rest_framework import serializers
from .models import Club, ClubImage, Table, Reservation, ComputerClub, Announcement, PriceList, \
   Game, ClubRules, GameAccessoriesSpecification


class ClubImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubImage
        fields = ('__all__')


class ReservationSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Reservation
        fields = ('computer_club', 'seats', 'owner', 'time', 'using_time')


class TableSerializer(serializers.ModelSerializer):
    seats_reservation = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = ('id', 'club', 'place_number', 'seats_reservation')


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = ('__all__')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('__all__')


class ClubRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubRules
        fields = ('__all__')


class GameAccessoriesSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameAccessoriesSpecification
        fields = ('__all__')


class ClubSerializer(serializers.ModelSerializer):
    club_image = ClubImageSerializer(many=True, read_only=True)
    club_reservation = ReservationSerializer(read_only=True, many=True)
    club_table = TableSerializer(read_only=True, many=True)
    price_list = PriceListSerializer(read_only=True, many=True)
    game_list = GameSerializer(read_only=True, many=True)
    club_rules_list = ClubRulesSerializer(read_only=True, many=True)
    game_accessories_specification_list = GameAccessoriesSpecificationSerializer(read_only=True, many=True)

    class Meta:
        model = Club
        fields = ('id', 'club', 'address', 'phone', 'seat', 'club_image', 'club_table', 'club_reservation', 'price_list',
                  'game_list', 'club_rules_list', 'game_accessories_specification_list')


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('id', 'news', 'text', 'image')


class ComputerClubSerializer(serializers.ModelSerializer):
    announcement_computer_club = AnnouncementSerializer(many=True, read_only=True)
    club_computer_club = ClubSerializer(many=True, read_only=True)
    class Meta:
        model = ComputerClub
        fields = ('id', 'computer_club', 'club_computer_club', 'announcement_computer_club')



