from django.contrib import admin

from clubs.models import Club, ClubImage, ComputerClub, Table, Reservation, ComputerClub, Announcement, PriceList, \
    Game, ClubRules, GameAccessoriesSpecification


class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 0


class ClubImageAdmin(admin.ModelAdmin):
    inlines = [ClubImageInline]


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['pk', 'computer_club', 'seats', 'time', 'using_time', 'time1', 'owner' ]
admin.site.register(Reservation, ReservationAdmin)

admin.site.register(ComputerClub)
admin.site.register(Announcement)
admin.site.register(Club, ClubImageAdmin)
admin.site.register(Table)
admin.site.register(PriceList)
admin.site.register(Game)
admin.site.register(ClubRules)
admin.site.register(GameAccessoriesSpecification)
