from __future__ import absolute_import, unicode_literals
from celery import shared_task
from landing_pages.models import Machines, Products
from django.utils import timezone

@shared_task
def reset_machine_status(machine_id):
    machine = Machines.objects.get(id=machine_id)
    machine.status="Free"
    machine.save()