from django import forms

from market.apps.core.models import UserProfile
from market.apps.social.models import SocialProfile


class UserProfileForm(forms.Form):
    # This form is used in registration to automatically create both UserProfile and SocialProfile objects
    # Note that this is NOT the actual form seen by the user

    def signup(self, request, user):
        # Automatically create user profile for every user
        profile = UserProfile.objects.create(user=user, type=self.cleaned_data['type'], name=self.cleaned_data['name'])
        profile.save()

        # Create an empty SocialProfile if the user is a seller
        if profile.type == UserProfile.ACCOUNT_TYPE_CHOICES[1]:
            social_profile = SocialProfile.objects.create(user=user)
