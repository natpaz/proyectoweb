from django.urls import path, include
from . import views

urlpatterns = [

    # Acá añadimos las funcionalidades de la app Registro.
    path('listar_formulario', views.listar_formulario, name="listar_formulario"),

    path('agregar_formulario', views.agregar_formulario, name="agregar_formulario"),

    path('editar_formulario/<int:formulario_id>', views.editar_formulario,name="editar_formulario"),

    path('borrar_formulario/<int:formulario_id>', views.borrar_formulario, name="borrar_formulario"),
    
    # Acá llamamos a las clases.
    path('add_formulario', views.FormularioCreate.as_view(), name="add_formulario"),

    path('list_formulario/', views.FormularioList.as_view(), name='list_formulario'),

    path('editar_formulario/<int:pk>', views.FormularioUpdate.as_view(), name='editar_formulario'),

    path('del_formulario/<int:pk>', views.FormularioDelete.as_view(), name='del_formulario'),
    
]


