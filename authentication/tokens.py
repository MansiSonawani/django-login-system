from django.contrib.auth.tokens import PasswordResetTokenGenerator



from six import text_type


class tokengenerator(PasswordResetTokenGenerator):
    def make_hash_values(self, user, timestamp):
       return (
        text_type(user.pk)  + text_type(timestamp)

       )


generate_token = tokengenerator()