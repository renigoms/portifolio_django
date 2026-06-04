from tasks import views
from django.urls import path

app_name = 'tasks'

urlpatterns = [
    # ─── Estilo 1: Function-Based Views ───
    path('v1/', views.task_list_create_fbv, name='list-fbv'),
    path('v1/<int:pk>', views.task_detail_fbv, name='detail-fbv'),

    # ─── Estilo 2: Class-Based Views (APIView) ───
    path('v2/', views.TaskListCreateApiView.as_view(), name='list-cbv'),
    path('v2/<int:pk>', views.TaskDetailApiView.as_view(), name='detail-cbv'),

    # ─── Estilo 3: Generic Views (RECOMENDADO) ───
    path('v3/', views.TaskListCreate.as_view(), name='list-generic'),
    path('v3/<int:pk>', views.TaskDetail.as_view(), name='detail-generic'),
]