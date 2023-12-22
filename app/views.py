from django.shortcuts import render,get_object_or_404,redirect
from .models import  Booking
from .forms import BookingForm
# Create your views here.
def index(request):
    
    return render(request,'index.html')
def booking(request):
    already_booked=Booking.objects.filter(booked=True)
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            # Before saving, check if the date and day combination is already booked
            date = form.cleaned_data['date']

            existing_booking = Booking.objects.filter(date=date, booked=True).first()

            if existing_booking:
                form = BookingForm()
                # If already booked, handle the error (e.g., show a message to the user)
                return render(request, 'Booking.html', {'message': 'This date  has already been booked.','form':form,'already_booked':already_booked})
            else:
                # If not booked, save the new booking
                booking = form.save(commit=False)
                booking.booked = True 
                booking.save()
                date=booking.date

                # Redirect or show a success message
                return render(request, 'Booking.html', {'success': f'Turf Booked On {date}.','form':form,'already_booked':already_booked})
    else:
        form = BookingForm()

    return render(request, 'Booking.html', {'form': form,'already_booked':already_booked})
