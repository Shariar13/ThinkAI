from django.urls import path
from .views import (
    home,
    about,
    contact,
    service,
    community,
    generate_pptx,
    generate_pptx_upload,
    generate_pdf_upload,
    generate_doc_upload,
    fix_your_grammar,
    paraphase,
    upload_your_project,
    ProjectDetail,
    buy_project,
    job_application,
    visualize,

)

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('community', community, name='community'),
    path('generate_pptx', generate_pptx, name='generate_pptx'),
    path('generate_pptx_upload', generate_pptx_upload, name='generate_pptx_upload'),
    path('generate_pdf_upload', generate_pdf_upload, name='generate_pdf_upload'),
    path('generate_doc_upload', generate_doc_upload, name='generate_doc_upload'),
    path('fix_your_grammar', fix_your_grammar, name='fix_your_grammar'),
    path('paraphase', paraphase, name='paraphase'),
    path('upload_your_project', upload_your_project, name='upload_your_project'),
    path('ProjectDetail/<int:pk>', ProjectDetail.as_view(), name='ProjectDetail'),
    path('buy_project', buy_project, name='buy_project'),
    path('job_application', job_application, name='job_application'),
    path('visualize', visualize, name='visualize'),
]
