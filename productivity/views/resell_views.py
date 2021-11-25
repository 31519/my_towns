# from rest_framework.serializers import Serializer
from productivity.models import Resell
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import ResellSerializers
from rest_framework import status


@api_view(['GET'])
def ResellList(request):
    resell = Resell.objects.all()
    serializer = ResellSerializers(resell, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ResellDetailList(request, pk):
    resell = Resell.objects.get(pk=pk)
    serializer = ResellSerializers(resell, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ResellCreate(request):
    data = request.data
    user = request.user
    resell = Resell.objects.create(
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
    serializer = ResellSerializers(resell, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ResellUpdate(request, pk):
    data = request.data
    resell = Resell.objects.get(pk=pk)
    resell.category =data['category']
    resell.country = data['country']
    resell.state = data['state']
    resell.address = data['address']
    resell.contact = data['contact']
    resell.image=data['image']
    resell.title = data['title']
    resell.content = data['content']
    resell.save()
    serializer = ResellSerializers(resell, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def ResellAdminUpdate(request, pk):
    data = request.data
    resell = Resell.objects.get(pk=pk)
    resell.category =data['category']
    resell.country = data['country']
    resell.state = data['state']
    resell.address = data['address']
    resell.contact = data['contact']
    resell.image=data['image']
    resell.title = data['title']
    resell.content = data['content']
    resell.isApproved = data['isApproved']
    resell.save()
    serializer = ResellSerializers(resell, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def ResellDelete(request, pk):
    if request.method == 'GET':
        resell = Resell.objects.get(pk=pk)
        serializer = ResellSerializers(resell, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        resell = Resell.objects.get(pk=pk)
        resell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
