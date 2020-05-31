from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
import traceback
import logging

# A default group of Agent can be set in the session, if user's group is not found in database.
# This is the lowest level of access for a signed-in user.
DEFAULT_AGENT_GROUP = 'Agent'

# Default Admin group constant is compared with the user's actual group to control access to various
# functions in the app via the template language. If the name of the Administrator group changes then it
# only needs to be changed here once for the whole app.
DEFAULT_ADMIN_GROUP = 'Admin'


# Create your views here.
def logout(request):
    """
    A view that logs the user out and redirects back to the index page.
    """
    auth.logout(request)
    messages.success(request, 'You are signed out.')
    return redirect(reverse('index'))


def login(request):
    """
    A view that manages the login form.
    """
    # Clear any existing default_admin_group from the session.
    if "default_admin_group" in request.session:
        del request.session["default_admin_group"]

    # Store the string literals for the two main types of users in the session.
    # These are used throughout app to give or restrict permissions to certain pages.
    request.session["default_agent_group"] = DEFAULT_AGENT_GROUP
    request.session["default_admin_group"] = DEFAULT_ADMIN_GROUP

    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                # Clear any existing group, user belongs to, from the session.
                if "group" in request.session:
                    del request.session["group"]

                # Set session to user's group stored in database. There should only be one group per user..for now!
                try:
                    group = Group.objects.filter(user=request.user).values_list('name', flat=True)
                    if group:
                        request.session["group"] = group[0]
                        if len(group) > 1:
                            messages.error(request, "Too many groups have been found for your user, so you have been "
                                                    "assigned, for this session, to the first one found: [ "
                                                    + group[0] + " ]. "
                                                    "Please contact your Administrator to place you in just one.")

                    if request.GET and request.GET['next'] != '':
                        next = request.GET['next']
                        return HttpResponseRedirect(next)
                    else:
                        return redirect(reverse('index'))
                except Exception:
                    logging.error(traceback.format_exc())
                    messages.error(request, "Sorry, a technical problem was logged when signing you in. "
                                            "Please contact your Administrator.")
            else:
                user_form.add_error(None, "Your username or password are incorrect.")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """
    A view that displays the profile page of a signed in user with
    group that user belongs to.
    """
    # Filter the Group model for current signed in user instance.
    groups = Group.objects.filter(user=request.user)

    return render(request, 'profile.html', {'groups': groups})


def register(request):
    """
    A view that manages the registration form.
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, "You have successfully registered. Please sign in.")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Unable to sign you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
