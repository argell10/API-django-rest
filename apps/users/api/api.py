from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

# APIView con funciones y decorador
@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        #to_representaion()
        users = User.objects.all().values('id', 'username', 'email', 'password')
        users_serializer = UserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    # registro de usuario con post
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_datail_api_view(request, id=None):
    # queryset
    user = User.objects.filter(id=id).first()
    # validation queryset
    if user:
        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Delete user Success!'}, status=status.HTTP_200_OK)
    return Response({'message':'User not found!'}, status=status.HTTP_400_BAD_REQUEST)
