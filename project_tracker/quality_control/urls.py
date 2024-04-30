from django.urls import path, include
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
     path(
        '',
        include(
            [
                # path('', views.index, name='index'),
                path('', views.IndexView.as_view(), name='index'),
            ]
        ),
    ),
    path(
        'bugs/',
        include(
            [
                path('', views.bugs_list, name='bugs_list'),
                path('<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
                path('new/', views.create_bug_report, name='create_bug_report'),
            ]
        ),
    ),
    path(
        'features/',
        include(
            [
                path('', views.features_list, name='features_list'),
                path('<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
                path('new/', views.create_feature_request, name='create_feature_request'),
            ]
        ),
    ),
]