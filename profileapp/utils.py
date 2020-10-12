import random
import string
from django.utils.text import slugify
# from unidecode import unidecode
# from django.template import defaultfilters
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils import six
import six
import math


def random_string_generator(size=10,
                            chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        # slug = defaultfilters.slugify(unidecode(instance.title))
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class PasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )


password_reset_token = PasswordResetTokenGenerator()


def generateOTP(length):
    """
        generates an random OTP of given no. of 

        digits
    """
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += digits[math.floor(random.random() * 10)]
    return otp