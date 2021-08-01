from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            from django.contrib.auth.models import User, AnonymousUser
            from rest_framework.authtoken.models import Token
            user, created = User.objects.get_or_create(username='AnonymousUser', first_name='Anonymous', last_name='User')
            user.set_unusable_password()
            user.save()
            token, created = Token.objects.get_or_create(user=user)

        return token.user, token