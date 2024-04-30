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
                # path('', views.bugs_list, name='bugs_list'),
                # path('<int:bug_id>/', views.bug_detail, name='bug_detail'),
                # path('new/', views.create_bug_report, name='create_bug_report'),
                # path('<int:bug_id>/update/', views.update_bug_report, name='update_bug_report'),
                # path('<int:bug_id>/delete/', views.delete_bug_report, name='delete_bug_report'),

                path('', views.BugsListView.as_view(), name='bugs_list'),
                path('<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_detail'),
                path('new/', views.BugReportCreateView.as_view(), name='create_bug_report'),
                path('<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug_report'),
                path('<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug_report'),
            ]
        ),
    ),
    path(
        'features/',
        include(
            [
                # path('', views.features_list, name='features_list'),
                # path('<int:feature_id>/', views.feature_detail, name='feature_detail'),
                # path('new/', views.create_feature_request, name='create_feature_request'),
                # path('<int:feature_id>/update/', views.update_feature_request, name='update_feature_request'),
                # path('<int:feature_id>/delete/', views.delete_feature_request, name='delete_feature_request'),

                path('', views.FeaturesListView.as_view(), name='features_list'),
                path('<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
                path('new/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
                path('<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature_request'),
                path('<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature_request'),
            ]
        ),
    ),
]