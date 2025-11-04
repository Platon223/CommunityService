from django.shortcuts import render, get_list_or_404
from .models import Community
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponseBadRequest
from .serializer import CommunitySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def find_community(request):
    try:
        unicode = request.body.decode('utf-8')
        data = json.loads(unicode)

        community_id = data.get('comm_id')

        if not community_id:
            return HttpResponseBadRequest("No community id provided")
        
        community = Community.objects.get(pk=community_id)

        serializer = CommunitySerializer(community)

        return Response(serializer.data)
    except json.JSONDecodeError:
        return HttpResponseBadRequest("Invalid JSON")
    except Exception as e:
        return HttpResponseBadRequest(f"Error occured: {e}")

@api_view(["POST"])
def create_community(request):
    serializer = CommunitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "success"}, status=200)
    return Response({"message": f"error occured: {serializer.errors}"}, status=400)
    


