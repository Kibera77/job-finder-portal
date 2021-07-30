from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail, BadHeaderError

from jobs_finder.settings import EMAIL_HOST_USER
from .models import JobPost, Employees
from .filters import JobFilter
from .forms import EmployeeForm


# Create your views here.


def home(request):
    return render(request, 'jobs/index.html')


def about(request):
    return render(request, 'jobs/about.html')


def job_search(request):
    job_posts = JobPost.objects.all()

    # a querry set to filter out items by selected values
    myFilter = JobFilter(request.GET, queryset=job_posts)
    job_posts = myFilter.qs

    paginator = Paginator(job_posts, 10)  # show 10 job posts per page

    page_number = request.GET.get('page')
    try:

        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {'job_posts': job_posts, 'myFilter': myFilter, 'page_obj': page_obj}

    return render(request, 'jobs/job_search.html', context)


def contact(request):
    return render(request, 'jobs/contact.html')


def send_email(request):
    if request.method == 'POST':
        template = render_to_string('jobs/email_temp.html', {

            'subject': request.POST['subject'],
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            EMAIL_HOST_USER, ['EMAIL_ADDRESS']
        )
        email.fail_silently = False
        email.send()
    return render(request, 'jobs/email_sent.html')


def success(request):
    return HttpResponse('Successful, Thank You!')


@login_required(login_url='login')
def apply(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

            name = form.cleaned_data.get('name')
            messages.success(request,
                             f"Thank you {name}! Application successful, We'll get back to you as soon as possible. ")

            return redirect('job_search')
        else:

            form = EmployeeForm()

    context = {'form': form}

    return render(request, 'Jobs/apply_form.html', context)
