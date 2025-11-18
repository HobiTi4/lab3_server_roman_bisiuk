from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from mmorpg_app.models import Character
from .forms import CharacterForm
from .NetworkHelper import NetworkHelper

def character_list(request):
    all_characters = Character.objects.all()

    context = {
        'characters': all_characters
    }
    return render(request, 'web_client/character_list.html', context)


def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)

    context = {
        'character': character
    }
    return render(request, 'web_client/character_detail.html', context)

def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('character_list')
    else:
        form = CharacterForm()

    return render(request, 'web_client/character_form.html', {'form': form})


def character_edit(request, pk):
    character = get_object_or_404(Character, pk=pk)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('character_detail', pk=pk)
    else:
        form = CharacterForm(instance=character)

    return render(request, 'web_client/character_form.html', {'form': form})


def character_delete(request, pk):
    character = get_object_or_404(Character, pk=pk)

    if request.method == "POST":
        character.delete()
        return redirect('character_list')

    return redirect('character_detail', pk=pk)

#----------- Part 2 -----------

DanceClub_API_URL = "http://127.0.0.1:8001/api"

helper = NetworkHelper(DanceClub_API_URL, username = "hobiti4", password = "12345678")


def external_instructors_list(request):
    endpoint = 'instructors'

    if request.method == "POST":
        item_id = request.POST.get('item_id')
        if item_id:
            helper.delete_item(endpoint, item_id)
        return redirect('external_instructors_list')

    response_data = helper.get_list(endpoint)
    if response_data and isinstance(response_data, dict) and 'results' in response_data:
        items = response_data['results']
    elif response_data and isinstance(response_data, list):
        items = response_data
    else:
        items = []

    context = {
        'items': items,
        'endpoint': endpoint,
        'page_title': 'Instructors',
        'id_field_name': 'instructor_id'
    }
    return render(request, 'web_client/external_list_template.html', context)

def external_clients_list(request):
    endpoint = 'clients'

    if request.method == "POST":
        item_id = request.POST.get('item_id')
        if item_id:
            helper.delete_item(endpoint, item_id)
        return redirect('external_clients_list')

    response_data = helper.get_list(endpoint)
    if response_data and isinstance(response_data, dict) and 'results' in response_data:
        items = response_data['results']
    elif response_data and isinstance(response_data, list):
        items = response_data
    else:
        items = []

    context = {
        'items': items,
        'endpoint': endpoint,
        'page_title': 'Clients',
        'id_field_name': 'client_id'
    }
    return render(request, 'web_client/external_list_template.html', context)