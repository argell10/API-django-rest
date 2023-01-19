from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication


class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(
            seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired = True
            # token.delete()
        return is_expire

    def authenticate_credentials(self,key):
        user,token,message = None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user

        except self.get_model().DoesNotExist:
            message = 'Token invalid'

        if token is not None:
            if not token.user.is_active:
                message = 'User is not active or invalid'

            is_expired = self.token_expire_handler(token)
            
            if is_expired:
                message = 'Token expired'

        return (user,token,message,self.expired)
