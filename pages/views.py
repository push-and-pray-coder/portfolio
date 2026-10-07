from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    #POST the visitor submitted the form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): #Django validates all fields
            #Extract the cleaned, validated data
            name = form.cleaned_data['name']
            #challenge get the email and message cleaned data
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # build the email body
            message_body=(
                f"New message from your portfolio\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}"
            )

            try:
                send_mail(
                    "Message from your Portfolio",
                    message_body,
                    None,
                    ['titanchenlee@gmail.com']
                )
                
                return render(request, 'pages/contact.html', {'form' : form})
            except Exception as e:
                print("EMAIL ERROR:", e)
                return render(request, 'pages/contact.html', {'form': form})
        else:
            return render(request, 'pages/contact.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html' , {'form' : form})

def experience_view(request):
    return render(request, 'pages/experience.html')

