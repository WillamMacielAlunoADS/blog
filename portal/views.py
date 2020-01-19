from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Area, Noticia
from .forms import AreaForm, NoticiaForm

def area_list(request):
	areas = Area.objects.filter()
	return render(request, 'portal/area_list.html', {'areas': areas})

def not_list(request):
	nots = Noticia.objects.filter()
	#nots = Noticia.objects.filter(published_date__lte=timezone.now())
	return render(request, 'portal/not_list.html', {'nots': nots})

def not_list_visita(request):
	nots = Noticia.objects.filter()
	areas = Area.objects.filter()
	return render(request, 'portal/not_visitante.html', {'nots': nots, 'areas': areas})

def area_detail(request, pk):
	area = get_object_or_404(Area, pk=pk)
	return render(request, 'portal/area_detail.html', {'area': area})

def not_detail(request, pk):
	noti = get_object_or_404(Noticia, pk=pk)
	return render(request, 'portal/not_detail.html', {'noti': noti})

def area_new(request):
	if request.method == "POST":
		form_area = AreaForm(request.POST)
		if form_area.is_valid():
			area = form_area.save(commit=False)
			area.save()
			return redirect('area_detail', pk=area.pk)
	else:
		form_area = AreaForm()
	return render(request, 'portal/area_edit.html', {'form_area': form_area})

def not_new(request):
	if request.method == "POST":
		form_not = NoticiaForm(request.POST, request.FILES)
		if form_not.is_valid():
			noti = form_not.save(commit=False)
			noti.author = request.user
			#noti.published_date = timezone.now()
			noti.save()
			return redirect('not_detail', pk=noti.pk)
	else:
		form_not = NoticiaForm()
	return render(request, 'portal/not_edit.html', {'form_not': form_not})


def area_edit(request, pk):
	area = get_object_or_404(Area, pk=pk)
	if request.method == "POST":
		form_area = AreaForm(request.POST, instance=area)
		if form_area.is_valid():
			area = form_area.save(commit=False)
			area.save()
			return redirect('area_detail', pk=area.pk)
	else:
		form_area = AreaForm(instance=area)
	return render(request, 'portal/area_edit.html', {'form_area': form_area})

def not_edit(request, pk):
	noti = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form_not = NoticiaForm(request.POST, request.FILES, instance=noti)
		if form_not.is_valid():
			noti = form_not.save(commit=False)
			noti.author = request.user
			noti.save()
			return redirect('not_detail', pk=noti.pk)
	else:
		form_not = NoticiaForm(instance=noti)
	return render(request, 'portal/not_edit.html', {'form_not': form_not})

def area_remove(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.delete()
	return redirect('area_list')

def not_remove(request, pk):
	noti = get_object_or_404(Noticia, pk=pk)
	noti.delete()
	return redirect('not_list')

def publicar(request, pk):
	noti = get_object_or_404(Noticia, pk=pk)
	noti.published_date = timezone.now()
	noti.save()
	return render(request, 'portal/not_detail.html', {'noti': noti, 'pk': noti.pk})

def ativar(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.status = timezone.now()
	area.save()
	return render(request, 'portal/area_detail.html', {'area': area, 'pk': area.pk})

def desativar(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.status = None
	area.save()
	return render(request, 'portal/area_detail.html', {'area': area, 'pk': area.pk})