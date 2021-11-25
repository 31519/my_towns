# from rest_framework.serializers import Serializer
from productivity.models import Advertisement
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import AdvertisementSerializers
from rest_framework import status


@api_view(['GET'])
def AdvertisementList(request):
    advertisement = Advertisement.objects.all()
    serializer = AdvertisementSerializers(advertisement, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AdvertisementDetailList(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    serializer = AdvertisementSerializers(advertisement, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AdvertisementCreate(request):
    data = request.data
    user = request.user
    advertisement = Advertisement.objects.create(
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
    serializer = AdvertisementSerializers(advertisement, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AdvertisementUpdate(request, pk):
    data = request.data
    advertisement = Advertisement.objects.get(pk=pk)
    advertisement.category =data['category']
    advertisement.country = data['country']
    advertisement.state = data['state']
    advertisement.address = data['address']
    advertisement.contact = data['contact']
    advertisement.image=data['image']
    advertisement.title = data['title']
    advertisement.content = data['content']
    advertisement.save()
    serializer = AdvertisementSerializers(advertisement, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def AdvertisementAdminUpdate(request, pk):
    data = request.data
    advertisement = Advertisement.objects.get(pk=pk)
    advertisement.category =data['category']
    advertisement.country = data['country']
    advertisement.state = data['state']
    advertisement.address = data['address']
    advertisement.contact = data['contact']
    advertisement.image=data['image']
    advertisement.title = data['title']
    advertisement.content = data['content']
    advertisement.isApproved = data['isApproved']
    advertisement.save()
    serializer = AdvertisementSerializers(advertisement, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def AdvertisementDelete(request, pk):
    if request.method == 'GET':
        advertisement = Advertisement.objects.get(pk=pk)
        serializer = AdvertisementSerializers(advertisement, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        advertisement = Advertisement.objects.get(pk=pk)
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
