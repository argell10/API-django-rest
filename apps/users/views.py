from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from apps.users.api.serializers import UserTokenSerializer


class UserToken(APIView):
    """
    Recibe una solicitud o query con parametros username:user y
    retorna el token actual de dicho usuario
    """
    def get(self,request,*args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UserTokenSerializer().Meta.model.objects.filter(username = username).first()
            )
            
            return Response({
                'token': user_token.key
            })
        except:
            return Response({
                'error': 'Creadenciales enviadas incorrectas'
            },status=status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):
    """
    Recibe como body username, pasword y valida si el usuario
    con esos datos existe y de ser asi le crea un token
    """
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if login_serializer.is_valid():
            # Si los datos enviados por post son validos:
            user = login_serializer.validated_data['user']
            if user.is_active:
                # Si el usuario existe crea un token para que este pueda acceder
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Token created'
                    }, status=status.HTTP_201_CREATED)
                else:
                    # Verifica si existe una sesion activa con el id del usuario que se este ingresando por post y si existe elimina esa sesion.
                    all_sessions = Session.objects.filter(
                        expire_date__gte=datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    # Elimina el token existente y crea uno nuevo
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Token created'
                    }, status=status.HTTP_201_CREATED)
                    # Si ya existe un token con esa sesion entonces no permitira acceder y ademas elimina el token por seguridad de si alguien intenta ingresar a nuestra cuenta
                    '''
                    token.delete()
                    return Response({
                        'error': 'Ya se ha iniciado sesion con ese usuario.'
                    }, status=status.HTTP_400_BAD_REQUEST)
                    '''
            else:
                return Response({'error': 'Este usuario no puede iniciar sesion.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
    Recibe como parametro un query token:token y si encuentra una sesion activa con ese token la elimina y tambien al token
    """
    def get(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key=token).first()

            if token:
                user = token.user

                all_sessions = Session.objects.filter(
                    expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()
                session_message = 'Sesiones de usuario eliminadas con existo.'
                token_message = 'Token eliminado con exito.'
                
                return Response({'session message': session_message, 'token message': token_message}, status=status.HTTP_200_OK)

            return Response({'error': 'No se ha encontrado usuario con estas credenciales o  token recibido'}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({'error': 'No se ha encontrado token en la peticion.'}, status=status.HTTP_409_CONFLICT)
