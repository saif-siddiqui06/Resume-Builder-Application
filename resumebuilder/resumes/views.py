from django.shortcuts import render, redirect
from .forms import ResumeForm
from django.http import HttpResponse
from .forms import ResumeForm
from xhtml2pdf import pisa
from django.template.loader import get_template


def home(request):
    return render(request, 'resumes/home.html')

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            return redirect('resume_templates')
    else:
        form = ResumeForm()
    return render(request, 'resumes/resume_form.html', {'form': form})
  
def preview_resume(request):
    form_data = request.session.get('form_data')
    if not form_data:
        return redirect('resume_form')
    
    template = request.GET.get('template', 'template2')
    return render(request, f'resumes/preview_{template}.html', {'form_data': form_data})
    
def resume_templates(request):
    return render(request, 'resumes/resume_templates.html')

def generate_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/wordprocessing')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
  

def download_pdf(request):
    form_data = request.session.get('form_data')
    if not form_data:
        return redirect('resume_form')
    template_name = request.GET.get('template', 'template1') + '.html'
    return generate_pdf(f'resumes/preview_{template_name}', {'form_data': form_data, 'is_pdf': True})
