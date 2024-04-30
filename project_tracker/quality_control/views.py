from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest

def index(request):
    return render(request, 'quality_control/index.html')

def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})

def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
    
class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'
    
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'