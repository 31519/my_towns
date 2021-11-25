# from rest_framework.serializers import Serializer
from productivity.models import Celebrities
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import CelebritiesSerializers
from rest_framework import status


@api_view(['GET'])
def CelebritiesList(request):
    celebrities = Celebrities.objects.all()
    serializer = CelebritiesSerializers(celebrities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CelebritiesDetailList(request, pk):
    celebrities = Celebrities.objects.get(pk=pk)
    serializer = CelebritiesSerializers(celebrities, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CelebritiesCreate(request):
    data = request.data
    user = request.user
    celebrities = Celebrities.objects.create(
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
    serializer = CelebritiesSerializers(celebrities, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CelebritiesUpdate(request, pk):
    data = request.data
    celebrities = Celebrities.objects.get(pk=pk)
    celebrities.category =data['category']
    celebrities.country = data['country']
    celebrities.state = data['state']
    celebrities.address = data['address']
    celebrities.contact = data['contact']
    celebrities.image=data['image']
    celebrities.title = data['title']
    celebrities.content = data['content']
    celebrities.save()
    serializer = CelebritiesSerializers(celebrities, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def CelebritiesAdminUpdate(request, pk):
    data = request.data
    celebrities = Celebrities.objects.get(pk=pk)
    celebrities.category =data['category']
    celebrities.country = data['country']
    celebrities.state = data['state']
    celebrities.address = data['address']
    celebrities.contact = data['contact']
    celebrities.image=data['image']
    celebrities.title = data['title']
    celebrities.content = data['content']
    celebrities.isApproved = data['isApproved']
    celebrities.save()
    serializer = CelebritiesSerializers(celebrities, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def CelebritiesDelete(request, pk):
    if request.method == 'GET':
        celebrities = Celebrities.objects.get(pk=pk)
        serializer = CelebritiesSerializers(celebrities, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        celebrities = Celebrities.objects.get(pk=pk)
        celebrities.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
