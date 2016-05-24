from django.http.response import HttpResponse


def home(request):
    return HttpResponse("hello world")

def room(request, room_id):
    zigbang = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + str(room_id)
#    return HttpResponse("This is a room detail " + room_id)
    return HttpResponse(zigbang)
