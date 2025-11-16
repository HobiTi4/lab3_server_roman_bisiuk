from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from mmorpg_app.models import Character
from .forms import CharacterForm

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