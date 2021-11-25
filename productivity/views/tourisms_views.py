# from rest_framework.serializers import Serializer
from productivity.models import Tourisms
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import TourismsSerializers
from rest_framework import status


@api_view(['GET'])
def TourismsList(request):
    tourisms = Tourisms.objects.all()
    serializer = TourismsSerializers(tourisms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TourismsDetailList(request, pk):
    tourisms = Tourisms.objects.get(pk=pk)
    serializer = TourismsSerializers(tourisms, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TourismsCreate(request):
    data = request.data
    user = request.user
    tourisms = Tourisms.objects.create(
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
    serializer = TourismsSerializers(tourisms, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TourismsUpdate(request, pk):
    data = request.data
    tourisms = Tourisms.objects.get(pk=pk)
    tourisms.category =data['category']
    tourisms.country = data['country']
    tourisms.state = data['state']
    tourisms.address = data['address']
    tourisms.contact = data['contact']
    tourisms.image=data['image']
    tourisms.title = data['title']
    tourisms.content = data['content']
    tourisms.save()
    serializer = TourismsSerializers(tourisms, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def TourismsAdminUpdate(request, pk):
    data = request.data
    tourisms = Tourisms.objects.get(pk=pk)
    tourisms.category =data['category']
    tourisms.country = data['country']
    tourisms.state = data['state']
    tourisms.address = data['address']
    tourisms.contact = data['contact']
    tourisms.image=data['image']
    tourisms.title = data['title']
    tourisms.content = data['content']
    tourisms.isApproved = data['isApproved']
    tourisms.save()
    serializer = TourismsSerializers(tourisms, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def TourismsDelete(request, pk):
    if request.method == 'GET':
        tourisms = Tourisms.objects.get(pk=pk)
        serializer = TourismsSerializers(tourisms, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        tourisms = Tourisms.objects.get(pk=pk)
        tourisms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
