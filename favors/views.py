from django.shortcuts import render, get_object_or_404
from .models import EquipmentType, Favors, Producer

def favors(request):
    equipment = EquipmentType.objects.order_by()
    return render(request, 'favors/favors_home.html', {'equipment': equipment})

def equipment_detail(request, equipment_id):
    equipment = get_object_or_404(EquipmentType, id=equipment_id)
    favors = Favors.objects.filter(equipment_type=equipment)
    return render(request, 'favors/equipment_detail.html', {
        'equipment': equipment,
        'favors': favors,
    })


