from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Create your views here.
def logout(request):
    """
    A view that logs the user out and redirects back to the index page.
    """
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect(reverse('index'))


def login(request):
    """
    A view that manages the login form.
    """
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                # Clear an item from the session.
                if "group" in request.session:
                    del request.session["group"]

                # Set a session to user's group. There should only be one..for now.
                group = Group.objects.filter(user=request.user).values_list('name', flat=True)
                print("Group = " + group[0])

                request.session["group"] = group[0]
                print("Session group = " + str(request.session["group"]))
                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect.")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """
    A view that displays the profile page of a logged in user with 
    group that user belongs to.
    """
    # Filter the Group model for current logged in user instance.
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
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
