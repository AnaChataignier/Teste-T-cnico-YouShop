from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Profile, PlantedTree, Account
from .forms import ProfileForm, PlantedTreeForm
from django.contrib import messages


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(user)
        print(username)
        print(password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{username} logado com sucesso!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
            return render(
                request,
                "user_login.html",
            )
    else:
        return render(request, "user_login.html")


def home(request):
    return render(request, "home.html")


def my_profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = None
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, f"information saved successfully")
            return redirect("home")
        else:
            messages.error(request, "Something went wrong, please try again")
            return redirect("my_profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "my_profile.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("user_login")


def add_planted_tree(request):
    if request.method == "POST":
        form = PlantedTreeForm(request.user, request.POST)
        if form.is_valid():
            planted_tree = form.save(commit=False)
            planted_tree.user = request.user
            planted_tree.tree_id = form.cleaned_data[
                "tree"
            ].id  # Associando o ID da árvore selecionada
            planted_tree.account_id = form.cleaned_data[
                "account"
            ].id  # Associando o ID da conta selecionada
            planted_tree.save()
            return redirect("home")
        else:
            messages.error(request, "Something went wrong, please try again")
            return redirect("add_planted_tree")
    else:
        form = PlantedTreeForm(user=request.user)
    return render(request, "add_planted_tree.html", {"form": form})


def my_planted_trees(request):
    # Obtém todas as árvores plantadas pelo usuário atualmente logado
    planted_trees = PlantedTree.objects.filter(user=request.user)

    # Renderiza o template HTML com as árvores plantadas
    return render(request, "my_planted_trees.html", {"planted_trees": planted_trees})


def planted_tree_detail(request, pk):
    # making sure the user can only access his planted_trees by using user=request.user
    planted_tree = get_object_or_404(PlantedTree, pk=pk, user=request.user)
    return render(request, "planted_tree_detail.html", {"planted_tree": planted_tree})


def my_accounts(request):
    user_accounts = Account.objects.filter(members=request.user)
    return render(request, "my_accounts.html", {"user_accounts": user_accounts})
