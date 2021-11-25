from rest_framework.serializers import Serializer
from productivity.models import Jobs
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from productivity.serializers import JobsSerializers
from rest_framework import status


@api_view(['GET'])
def JobsList(request):
    jobs = Jobs.objects.all()
    serializer = JobsSerializers(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def JobsDetailList(request, pk):
    jobs = Jobs.objects.get(pk=pk)
    serializer = JobsSerializers(jobs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JobsCreate(request):
    data = request.data
    user = request.user
    jobs = Jobs.objects.create(
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
    serializer = JobsSerializers(jobs, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JobsUpdate(request, pk):
    data = request.data
    jobs = Jobs.objects.get(pk=pk)
    jobs.category =data['category']
    jobs.country = data['country']
    jobs.state = data['state']
    jobs.address = data['address']
    jobs.contact = data['contact']
    jobs.image=data['image']
    jobs.title = data['title']
    jobs.content = data['content']
    jobs.save()
    serializer = JobsSerializers(jobs, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def JobsAdminUpdate(request, pk):
    data = request.data
    jobs = Jobs.objects.get(pk=pk)
    jobs.category =data['category']
    jobs.country = data['country']
    jobs.state = data['state']
    jobs.address = data['address']
    jobs.contact = data['contact']
    jobs.image=data['image']
    jobs.title = data['title']
    jobs.content = data['content']
    jobs.isApproved = data['isApproved']
    jobs.save()
    serializer = JobsSerializers(jobs, many=False)
    return Response(serializer.data)



@api_view(['DELETE', 'GET'])
@permission_classes([IsAdminUser])
def JobsDelete(request, pk):
    if request.method == 'GET':
        jobs = Jobs.objects.get(pk=pk)
        serializer = JobsSerializers(jobs, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        jobs = Jobs.objects.get(pk=pk)
        jobs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
