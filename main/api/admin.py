from django.contrib import admin

from .models import City, Cinema, Hall, Film, Seat


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class CinemaAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'number_phone', 'address')


class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'cinema', 'number', 'count_seats')


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'country', 'duration')


class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'hall', 'number', 'available')


admin.site.register(City, CityAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Seat, SeatAdmin)
