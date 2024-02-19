from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    # Se necessário, adicione outros campos aqui
    accounts = models.ManyToManyField(Account, related_name="members", blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        related_name="custom_user_set",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        related_name="custom_user_set",
    )

    def plant_tree(self, tree, location):
        PlantedTree.objects.create(user=self, tree=tree, location=location)

    def plant_trees(self, tree_locations):
        for tree, location in tree_locations:
            PlantedTree.objects.create(user=self, tree=tree, location=location)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    joined = models.DateTimeField(auto_now_add=True)


class Tree(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.tree.name
