from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Formulario
from .forms import FormularioForm
from django.urls import reverse_lazy

# Create your views here.

def listar_formulario(request):
    formulario = Formulario.objects.all()
    return render(request, "Registro/listar_formulario.html", {'formulario': formulario})

def agregar_formulario(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_formulario")
    else:
        form = FormularioForm()
        return render(request, "Registro/agregar_formulario.html", {'form': form})

def borrar_formulario(request, formulario_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Formulario.objects.get(id=formulario_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_formulario')

def editar_formulario(request, formulario_id):
    # Recuperamos la instancia de la carrera
    instancia = Formulario.objects.get(id=formulario_id)

    # Creamos el formulario con los datos de la instancia
    form = FormularioForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = FormularioForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_formulario.html", {'form': form})

# --clases Generics -------
class FormularioCreate(CreateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'Registro/agregar_formulario.html'
    success_url = reverse_lazy("list_formulario")

class FormularioList(ListView):
    model = Formulario
    template_name = 'Registro/list_formulario.html'
    # paginate_by = 4

class FormularioUpdate(UpdateView):
    model = Formulario
    form_class = FormularioForm
    template_name = 'Registro/agregar_formulario.html'
    success_url = reverse_lazy('list_formulario')

        

class FormularioDelete(DeleteView):
    model = Formulario
    template_name = 'Registro/formulario_delete.html'
    success_url = reverse_lazy('list_formulario')