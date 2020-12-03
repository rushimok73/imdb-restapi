from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from webapp.models import moviedata
from webapp.serializers import movieSerializer
from rest_framework.decorators import api_view
from . import scraper
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes


@api_view(['GET','DELETE'])
@authentication_classes((TokenAuthentication,))
def movie_list(request):
    if request.method == 'GET':
        filter = request.GET['filter']
        filter = int(filter)
        ret = []
        if filter == 1:
            for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata ORDER BY moviename'):
                temp = {}
                temp['moviename'] = results.moviename
                temp['movieyear'] = results.movieyear
                temp['movierating'] = results.movierating
                temp['movieimage'] = results.movieimage
                ret.append(temp)
            return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
        elif(filter is -1):
            for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata ORDER BY moviename DESC'):
                temp = {}
                temp['moviename'] = results.moviename
                temp['movieyear'] = results.movieyear
                temp['movierating'] = results.movierating
                temp['movieimage'] = results.movieimage
                ret.append(temp)
            return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
        elif(filter is 2):
            for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata ORDER BY movieyear'):
                temp = {}
                temp['moviename'] = results.moviename
                temp['movieyear'] = results.movieyear
                temp['movierating'] = results.movierating
                temp['movieimage'] = results.movieimage
                ret.append(temp)
            return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
        elif(filter is -2):
            for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata ORDER BY movieyear DESC'):
                temp = {}
                temp['moviename'] = results.moviename
                temp['movieyear'] = results.movieyear
                temp['movierating'] = results.movierating
                temp['movieimage'] = results.movieimage
                ret.append(temp)
            return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
        elif(filter is 3):
            for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata ORDER BY movierating'):
                temp = {}
                temp['moviename'] = results.moviename
                temp['movieyear'] = results.movieyear
                temp['movierating'] = results.movierating
                temp['movieimage'] = results.movieimage
                ret.append(temp)
            return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
        elif(filter is -3):
            for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata ORDER BY movierating DESC'):
                temp = {}
                temp['moviename'] = results.moviename
                temp['movieyear'] = results.movieyear
                temp['movierating'] = results.movierating
                temp['movieimage'] = results.movieimage
                ret.append(temp)
            return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
        else:
            return JsonResponse({'message': 'Send valid filter key'}, status=status.HTTP_201_CREATED)
        return JsonResponse({'message': 'Error'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = moviedata.objects.all().delete()
        return JsonResponse({'message': '{} Movie were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
def scrape(request):
    if request.method == 'GET':
        res = scraper.scraperfn()
        flag = 1
        for movie_data in res:
            movie_serializer = movieSerializer(data=movie_data)
            if movie_serializer.is_valid():
                movie_serializer.save()
            else:
                flag = 0
                break

        if(flag):
            return JsonResponse({'message': 'Movies scraped and stored to db successfully'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
def movie_name(request):
    if request.method == 'POST':
        name = request.data['name']
        print(name)
        ret = []
        for results in moviedata.objects.raw('SELECT * FROM webapp_moviedata WHERE moviename = %s', [name]):
            temp = {}
            temp['moviename'] = results.moviename
            temp['movieyear'] = results.movieyear
            temp['movierating'] = results.movierating
            temp['movieimage'] = results.movieimage
            ret.append(temp)
        return JsonResponse(ret, status=status.HTTP_201_CREATED, safe = False)
