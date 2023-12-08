from django.shortcuts import render, redirect, get_object_or_404
from datetime import timedelta
from django.contrib.auth.decorators import login_required

from ..models import Machines, Recipes
from ..forms import MachinesModelForm

@login_required(login_url="/login")
def machine_page(request):
    machines = Machines.objects.all()
    # test = Recipe_Machines.objects.get(pk=1)

    if request.method == "POST":
        form = MachinesModelForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("machine_page")
    
    else:
        form = MachinesModelForm()

    title = "Machines"
    context = {
        "machines": machines,
        "form": form,
        "title": title,
    }

    return render(request, "landing_pages/machines.html", context)


@login_required(login_url="/login")
def edit_machine(request, machine_id):
    machine = get_object_or_404(Machines, id=machine_id)
    form = MachinesModelForm(instance=machine)

    if request.method == "POST":
        form = MachinesModelForm(request.POST, instance=machine)
        if form.is_valid():
            form.save()
            return redirect("machine_page")
        
    context = {
        "form": form,
        "title": "Edit Machine"
    }

    return render(request, "landing_pages/edit_machine.html", context)


@login_required(login_url="/login")
def delete_machine(request, machine_id):
    machine = get_object_or_404(Machines, id=machine_id)

    if request.method == "POST":
        # Update related Recipes' machine_duration to zero
        Recipes.objects.filter(machine=machine_id).update(machine_duration=timedelta())
        machine.delete()

        return redirect("machine_page")
    
    context = {
        "machine": machine,
        "title" : "Delete Machine"
    }

    return render(request, "landing_pages/delete_machine.html", context)