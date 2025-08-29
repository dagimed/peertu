from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to PeerTu API! Visit /api/ for endpoints."})