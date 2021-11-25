# from rest_framework.serializers import Serializer
from productivity.models import Hotels
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import HotelsSerializers
from rest_framework import status


@api_view(['GET'])
def HotelsList(request):
    hotels = Hotels.objects.all()
    serializer = HotelsSerializers(hotels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def HotelsDetailList(request, pk):
    hotels = Hotels.objects.get(pk=pk)
    serializer = HotelsSerializers(hotels, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def HotelsCreate(request):
    data = request.data
    user = request.user
    hotels = Hotels.objects.create(
        user =user,
        category=data['category'],
        country=data['country'],
        state=data['state'],
        address=data['address'],
        contact=data['contact'],
        image=data['image'],
        title=data['title'],
        content=data['content']
    )
    serializer = HotelsSerializers(hotels, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def HotelsUpdate(request, pk):
    data = request.data
    hotels = Hotels.objects.get(pk=pk)
    hotels.category =data['category']
    hotels.country = data['country']
    hotels.state = data['state']
    hotels.address = data['address']
    hotels.contact = data['contact']
    hotels.image=data['image']
    hotels.title = data['title']
    hotels.content = data['content']
    hotels.save()
    serializer = HotelsSerializers(hotels, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def HotelsAdminUpdate(request, pk):
    data = request.data
    hotels = Hotels.objects.get(pk=pk)
    hotels.category =data['category']
    hotels.country = data['country']
    hotels.state = data['state']
    hotels.address = data['address']
    hotels.contact = data['contact']
    hotels.image=data['image']
    hotels.title = data['title']
    hotels.content = data['content']
    hotels.isApproved = data['isApproved']
    hotels.save()
    serializer = HotelsSerializers(hotels, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def HotelsDelete(request, pk):
    if request.method == 'GET':
        hotels = Hotels.objects.get(pk=pk)
        serializer = HotelsSerializers(hotels, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        hotels = Hotels.objects.get(pk=pk)
        hotels.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
