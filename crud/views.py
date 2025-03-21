from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Player
from .forms import PlayerForm
from django.contrib import messages

#Create
def player_create(request):
    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("crud:player_list")
    else:
        return render(
            request,
            "crud/player_create.html",
            {
                "form" : PlayerForm()
            },)
    
#Read All
def player_list(request):
    all_players = Player.objects.all()
    return render(
        request,
        "crud/player_list.html",
        {
            "all_players":all_players
        },
    )

#Update
def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)

    if request.method == "POST":
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, f"{player.name} updated successfully!")
        return redirect("crud:player_list")
    else:
        form = PlayerForm(instance=player)
        return render(
            request,
            "crud/player_update.html",
            {
                "form":form,
                "player":player,
            },
        )
    
#Delete
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    messages.success(request, f'"{player.name}" deleted successfully!')
    return redirect("crud:player_list")

#create super user
def create_super(request):
    if not Player.objects.filter(username="root").exists():
        Player.objects.create_superuser("root", "", "root")
        return HttpResponse("Superuser created! Username: root, Password: root")
    return HttpResponse("Superuser already exists!")