from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
                            ListView,
                            DetailView,
                            CreateView,
                            UpdateView,
                            DeleteView
                            )
from .models import Trip


def home(request):
    context= {
        'trips': Trip.objects.all()
    }
    return render(request, 'travel_companion/home.html', context)

def about(request):
    return render(request, 'travel_companion/about.html')


class TripListView(ListView):
    """ ListView that list all trips """
    model = Trip
    # <app> / <model>_<viewtype>.html by django convention
    template_name = 'travel_companion/home.html'
    context_object_name = 'trips'
    ordering=['-date_posted']
    paginate_by = 3

class UserTripListView(ListView):
    """ ListView that list all trips of current loged in user """
    model = Trip
    # <app> / <model>_<viewtype>.html by django convention
    template_name = 'travel_companion/user_trips.html'
    context_object_name = 'trips'
    paginate_by = 3

    def get_queryset(self):
        """ get only trips from user ordering by date """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Trip.objects.filter(author=user).order_by('-date_posted')

class TripDetailView(DetailView):
    """ DetailView of Trip, linked on home.html page on each trip """
    model = Trip

class TripCreateView(LoginRequiredMixin, CreateView):
    """ CreateView to create new trip with LoginRequiredMixin
        that allows to create only if the User is loged in
    """
    model = Trip
    fields = ['title', 'details', 'point_of_destination']

    def form_valid(self, form):
        """ the form that the user trying to submit"""
        form.instance.author = self.request.user
        return super().form_valid(form)

class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ UpdateView to update existing trip with LoginRequiredMixin and
        UserPassesTestMixin that allows to update trips if the author of
        the trip is current loged in user
    """

    model = Trip
    fields = ['title', 'details', 'point_of_destination']

    def form_valid(self, form):
        """ the form that the user trying to submit"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ UserPassesTestMixin run in order to see if u user is correct  """
        trip = self.get_object()
        if self.request.user == trip.author:
            return True
        else:
            return False

class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ DeleteView to delete existing trip with LoginRequiredMixin and
        UserPassesTestMixin that allows to delete trips if the author of
        the trip is current loged in user
    """
    model = Trip
    success_url = '/'
    def test_func(self):
        """ UserPassesTestMixin run in order to see if u user is correct  """
        trip = self.get_object()
        if self.request.user == trip.author:
            return True
        else:
            return False
