# from rest_framework.serializers import Serializer
from productivity.models import Shops
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import ShopsSerializers
from rest_framework import status


@api_view(['GET'])
def ShopsList(request):
    shops = Shops.objects.all()
    serializer = ShopsSerializers(shops, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShopsDetailList(request, pk):
    shops = Shops.objects.get(pk=pk)
    serializer = ShopsSerializers(shops, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ShopsCreate(request):
    data = request.data
    user = request.user
    shops = Shops.objects.create(
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
    serializer = ShopsSerializers(shops, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ShopsUpdate(request, pk):
    data = request.data
    shops = Shops.objects.get(pk=pk)
    shops.category =data['category']
    shops.country = data['country']
    shops.state = data['state']
    shops.address = data['address']
    shops.contact = data['contact']
    shops.image=data['image']
    shops.title = data['title']
    shops.content = data['content']
    shops.save()
    serializer = ShopsSerializers(shops, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def ShopsAdminUpdate(request, pk):
    data = request.data
    shops = Shops.objects.get(pk=pk)
    shops.category =data['category']
    shops.country = data['country']
    shops.state = data['state']
    shops.address = data['address']
    shops.contact = data['contact']
    shops.image=data['image']
    shops.title = data['title']
    shops.content = data['content']
    shops.isApproved = data['isApproved']
    shops.save()
    serializer = ShopsSerializers(shops, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def ShopsDelete(request, pk):
    if request.method == 'GET':
        shops = Shops.objects.get(pk=pk)
        serializer = ShopsSerializers(shops, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        shops = Shops.objects.get(pk=pk)
        shops.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
