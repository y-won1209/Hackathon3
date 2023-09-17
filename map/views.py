from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *
from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response
from django.db.models import Q
import json


def load_json_and_save_to_model(file_path):
    with open(file_path, 'rt',encoding='UTF8') as json_file:
        json_data = json.load(json_file)

    for entry in json_data:
        name = entry.get('name')
        category = entry.get('category')
        latitude = entry.get('latitude')
        longitude = entry.get('longitude')
        address = entry.get('address')
        parking = entry.get('parking')
        dis_parking = entry.get('dis_parking')
        big_parking = entry.get('big_parking')
        wheelchair = entry.get('wheelchair')
        toilet = entry.get('toilet')
        braille = entry.get('braille')
        audio = entry.get('audio')

        existing_place = Place.objects.filter(name=name).first()
        if existing_place:
            print(f"Place '{name}' already exists. Skipping...")
            return

        place = Place(
            name=name,
            category=category,
            latitude=latitude,
            longitude=longitude,
            address=address,
            parking=parking,
            dis_parking=dis_parking,
            big_parking=big_parking,
            wheelchair = wheelchair,
            toilet = toilet,
            braille = braille,
            audio = audio

        )
        place.save()
load_json_and_save_to_model('map.json')


class PlaceFilterView(views.APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Place.objects.all()

        category_filter = request.query_params.get('category')
        if category_filter:
            categories = category_filter.split(',')
            queryset = queryset.filter(category__in=categories)

        parking_filter = request.query_params.get('parking')
        if parking_filter:
            parkings = parking_filter.split(',')
            queryset = queryset.filter(parking__in=parkings)

        dis_parking_filter = request.query_params.get('dis_parking')
        if dis_parking_filter:
            dis_parkings = dis_parking_filter.split(',')
            queryset = queryset.filter(dis_parking__in=dis_parkings)

        wheelchair_filter = request.query_params.get('wheelchair')
        if wheelchair_filter:
            wheelchairs = wheelchair_filter.split(',')
            queryset = queryset.filter(wheelchair__in=wheelchairs)

        toilet_filter = request.query_params.get('toilet')
        if toilet_filter:
            toilets = toilet_filter.split(',')
            queryset = queryset.filter(toilet__in=toilets)

        braille_filter = request.query_params.get('braille')
        if braille_filter:
            brailles = braille_filter.split(',')
            queryset = queryset.filter(braille__in=brailles)

        audio_filter = request.query_params.get('audio')
        if audio_filter:
            audios = audio_filter.split(',')
            queryset = queryset.filter(audio__in=audios)


        
        result_count = queryset.count()
        serializer = PlaceSerializer(queryset, many=True)
        
        if result_count > 0:
            return Response({'message': '필터링 조회 성공', 
                            'result_count': result_count,
                            'data': serializer.data,
                            })  # Include result count in the response
        else:
            return Response({'message': '필터링 결과가 없어요. 다른 선택을 해 주세요?'}, status=HTTP_204_NO_CONTENT)
class PlaceSearchView(views.APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        queryset = Place.objects.all()
        search_query = request.query_params.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |  
                Q(address__icontains=search_query) 
            )
            search_result_count = queryset.count()
            
            if search_result_count > 0:
                serializer = PlaceSerializer(queryset, many=True)
                return Response({
                    'message': '검색 조회 성공',
                    'data': serializer.data,
                    'result_count': search_result_count  # Include the result count in the response
                })
            else:
                return Response({'message': '검색결과가 없어요. 다시 시도해주시겠어요?'}, status=HTTP_204_NO_CONTENT)
        else:
            return Response({'message': '검색어를 입력하세요.'}, status=HTTP_400_BAD_REQUEST)
        
class PlaceDetailView(views.APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request,pk,format=None):
        place = get_object_or_404(Place, pk=pk)
        serializer = PlaceDetailSerialiser(place)
        return Response(serializer.data)

'''
class PlaceListView(views.APIView):
    
    def get(self, request):
        order_by = request.query_params.get('order_by')
        queryset = Place.objects.all()

        if order_by == 'alphabetical': #최신순으로
            queryset = queryset.order_by('name')
            
        if order_by == 'distance': #최신순으로
            queryset = queryset.order_by('distance')

        serializer = PlaceSerializer(queryset, many=True)
        post_count = Place.objects.count()  # Post 모델의 총 갯수 계산
        message = f"현재 등록된 포스트 갯수: {post_count}"
        
        return Response({'message': message, 'data':serializer.data})
'''


import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # Result in kilometers
    return distance

class PlaceListView(views.APIView):
    def get(self, request):
        order_by = request.query_params.get('order_by')
        user_latitude = 37.4685064  # Your fixed latitude value
        user_longitude = 127.0391872   # Your fixed longitude value

        queryset = Place.objects.all()

        if order_by == 'alphabetical':
            queryset = queryset.order_by('name')

        if order_by == 'distance':
            queryset = sorted(queryset, key=lambda place: haversine_distance(
                user_latitude, user_longitude,
                place.latitude, place.longitude
            ))
        
        serializer = PlaceSerializer(queryset, many=True)  # Only fetch the first 30 places
        #message = f"현재 등록된 포스트 갯수: {len(queryset)}"
        
        return Response({'message': "정렬 조회", 'data':serializer.data})
'''  
class DistanceView(views.APIView):

    def get(self, request):
        order_by = request.query_params.get('order_by')
        user_latitude = 37.4685064  # Your fixed latitude value
        user_longitude = 127.0391872 # Your fixed longitude value

        queryset = Place.objects.all()



        if order_by == 'distance':
            queryset = sorted(queryset, key=lambda place: haversine_distance(
                user_latitude, user_longitude,
                place.latitude, place.longitude
            ))

        serializer = PlaceSerializer(queryset[:30], many=True)  # Only fetch the first 30 places
        #message = f"현재 등록된 포스트 갯수: {len(queryset)}"
        
        return Response({'message': "거리 순 정렬 성공", 'data':serializer.data})

'''


class MyViews(views.APIView):
    def get(self, request):
        return Response(status=HTTP_200_OK)

    def post(self,request, format=None):
        serializer = MySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({'message': '현 위치 정보가 저장되었습니다.'})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)