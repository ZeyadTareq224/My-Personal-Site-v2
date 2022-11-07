from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import View
from core.forms import ContactForm
from core.models import Resume, Project, Achievment, Skill


class IndexView(View):
    """ The entry point to the site (Index Page)"""

    # handel the rendering of the site entry point
    def get(self, request):

        # Resumee Queries
        my_resume = Resume.objects.first()

        #Project Queries
        projects = Project.objects.all()

        #Achievments Queries
        achievments = Achievment.objects.all()
        
        #Skills Queries
        skills = Skill.objects.all()

        context = {
            'resume_path':my_resume.get_resume_path,
            'projects':projects,
            'achievments': achievments,
            'skills': skills
        }
        return render(request, 'core/index.html', context)

    # handel the submission of the contact form    
    def post(self, request):
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.send()
        messages.success(request, "Thanks for contacting me, i'll reach to you as soon as possible.")
        return redirect('home')

