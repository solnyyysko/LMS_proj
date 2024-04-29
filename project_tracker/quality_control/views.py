from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest

# def index(request):
#     bugs_list_url = reverse('quality_control:bugs_list')
#     features_list_url = reverse('quality_control:features_list')
#     html = f"<h1>Система контроля качества</h1><a href='{bugs_list_url}'>Список всех багов</a><br><a href='{features_list_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

def bugs_list(request):
    bugs = BugReport.objects.all()
    bug_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bug_html += f'<li><a href="{bug.id}/">{bug.title} {bug.status}</a></li>'
    bug_html += "</ul>"
    return HttpResponse(bug_html)

def features_list(request):
    features = FeatureRequest.objects.all()
    feature_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        feature_html += f'<li><a href="{feature.id}/">{feature.title} {feature.status}</a></li>'
    feature_html += "</ul>"
    return HttpResponse(feature_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>Детали бага {bug_id}</h1><h2>{bug.title}</h2><p>description: {bug.description}<br>status: {bug.status}<br>priority: {bug.priority}<br>project: {bug.project}<br>task: {bug.task}</p>'
    return HttpResponse(response_html)

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>Детали улучшения {feature_id}</h1><h2>{feature.title}</h2><p>description: {feature.description}<br>status: {feature.status}<br>priority: {feature.priority}<br>project: {feature.project}<br>task: {feature.task}</p>'
    return HttpResponse(response_html)

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_list_url = reverse('quality_control:bugs_list')
        features_list_url = reverse('quality_control:features_list')
        html = f"<h1>Система контроля качества</h1><a href='{bugs_list_url}'>Cписок отчетов об ошибках</a><br><a href='{features_list_url}'>Список запросов на улучшение</a>"
        return HttpResponse(html)
    
class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>Детали бага {bug.id}</h1><h2>{bug.title}</h2><p>description: {bug.description}<br>status: {bug.status}<br>priority: {bug.priority}<br>project: {bug.project}<br>task: {bug.task}</p>'
        return HttpResponse(response_html)
    
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>Детали улучшения {feature.id}</h1><h2>{feature.title}</h2><p>description: {feature.description}<br>status: {feature.status}<br>priority: {feature.priority}<br>project: {feature.project}<br>task: {feature.task}</p>'
        return HttpResponse(response_html)