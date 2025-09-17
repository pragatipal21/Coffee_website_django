from django.shortcuts import render, redirect
from django.core.mail import send_mail
from service.models import Service, Learn, OurServices, TableBook, pricing,Subscriber,Offer,MenuItem


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse





# View for the homepage
def home(request):
    # Initializing the message variable
    msg = ""
    
    # Handling POST request for form submission
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        person = request.POST.get('person')
        
        # Save form data to the TableBook model
        alldata = TableBook(name=name, email=email, date=date, time=time, person=person)
        alldata.save()
        
        # Confirmation message for form submission
        msg = "Data Inserted Successfully!"
        
        # Sending an email confirmation
        subject = 'Booking Confirmation'
        message = (
            f"Dear {name},\n\n"
            f"Your booking has been confirmed for {date} at {time} for {person} person(s).\n\n"
            "Thank you for choosing our service!"
        )
        from_email = 'pragaticraftcorner@gmail.com'  # Update with your email
        recipient_list = [email]
        
        # Send the email
        send_mail(subject, message, from_email, recipient_list)

    # Fetching data for rendering the homepage
    serviceData = Service.objects.all()
    learnData = Learn.objects.all()
    ourserviceData = OurServices.objects.all()
    pricingData = pricing.objects.all()
    offerData = Offer.objects.all()
    menuitemData = MenuItem.objects.all()
    
  
    
    # Combine the data into a dictionary
    data = {
        'serviceData': serviceData,
        'learnData': learnData,
        'ourserviceData': ourserviceData,
        'pricingData': pricingData,
        'msg': msg,
        'offerData' : offerData, 
        'menuitemData' : menuitemData# Pass the message to the template as well
    }
    
    # Render the template with the data
    return render(request, "index.html", data)




# View for reservation form
#def reservation(request):
    # Fetching all reservations (if you need to show them on the page)
    #reservations = Reservation.objects.all()
    
    # Render the reservation template with the reservations data
    #return render(request, "reservation.html", {'reservations': reservations})


# View to display all testimonials (for example purposes, you can modify as needed)
#def testimonial(request):
   # return render(request, "testimonial.html")



# View to create a testimonial for a specific reservation
#def create_testimonial(request, reservation_id):
   # reservation = Reservation.objects.get(id=reservation_id)
    
    # Handle POST request for creating a testimonial
    #if request.method == 'POST':
        #form = TestimonialForm(request.POST)
        
       # if form.is_valid():
            # Create a new testimonial and link it to the reservation
            #
            # Redirect to the reservation details page (you can create this view separately if needed)
            #return redirect('reservation_detail', reservation_id=reservation.id)
    
    # If GET request, just render the form
    #else:
#        form = TestimonialForm()

   # return render(request, 'testimonial.html', {'form': form, 'reservation': reservation})
import requests
from django.shortcuts import render

# View for displaying coffee data
def coffeeData(request):
    api_url = "https://api.sampleapis.com/coffee/hot"  # URL for Sample Coffee API
    
    try:
        # Fetch the data from the API
        response = requests.get(api_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            coffee_items = response.json()  # Parse the JSON response (returns a list)
        else:
            coffee_items = []  # If the API request fails, set coffee_items to an empty list

    except requests.exceptions.RequestException as e:
        # Handle any connection or request errors
        print(f"Error fetching coffee data: {e}")
        coffee_items = []  # Set coffee_items to an empty list in case of error

    # Pass the coffee data to the template
    return render(request, "display.html", {'coffee_items': coffee_items})

    
def aboutus(request):
    learnData = Learn.objects.all()
    data = {
        'learnData': learnData,
    }
    return render(request, "about.html", data)

    

def contact(request):
    return render(request, "contact.html")

def service(request):
    ourserviceData = OurServices.objects.all()
    data = {
        'ourserviceData': ourserviceData,
    }
    return render(request, "service.html", data)

def menu(request):
    menuitemData = MenuItem.objects.all()
    data = {
        'menuitemData' : menuitemData,
    }
    return render(request, "menu.html", data)

def testimonial(request):
    return render(request, "testimonial.html")
def reservation(request):
    return render(request, "reservation.html")


@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subscriber, created = Subscriber.objects.get_or_create(email=email)
            if created:
                return HttpResponse("Subscription successful!")
            else:
                return HttpResponse("You are already subscribed!")
    return redirect('/')







from django.shortcuts import render, redirect
from service.forms import TestimonialForm
from service.models import Testimonial



def reservation(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonial')  # after saving, redirect to testimonial page
    else:
        form = TestimonialForm()

    return render(request, 'reservation.html', {'form': form})

def testimonial(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'testimonial.html', {'testimonials': testimonials})

