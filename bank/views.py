from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import LoanApplicationForm
from .models import LoanApplication
from django.contrib import messages

def home(request):
    return render(request, 'bank/home.html')

def services(request):
    return render(request, 'bank/services.html')

def about(request):
    return render(request, 'bank/about.html')

def testimonials(request):
    return render(request, 'bank/testimonials.html')

def apply_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            return redirect('application_result', application_id=application.application_id)
    else:
        form = LoanApplicationForm()
    
    return render(request, 'bank/apply_loan.html', {'form': form})

def application_result(request, application_id):
    application = get_object_or_404(LoanApplication, application_id=application_id)
    
    context = {
        'application': application,
        'total_assets': application.total_assets(),
        'application_date': application.created_at.strftime('%B %d, %Y'),
    }
    
    if application.is_approved:
        template = 'bank/application_approved.html'
    else:
        template = 'bank/application_rejected.html'
    
    return render(request, template, context)