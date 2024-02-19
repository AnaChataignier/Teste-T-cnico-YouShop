from django.test import TestCase
from main.models import Account, User, PlantedTree


class TestScenario(TestCase):
    def setUp(self):
        # Criar duas contas
        account1 = Account.objects.create(name="Conta 1")
        account2 = Account.objects.create(name="Conta 2")

        # Criar três usuários distribuídos pelas duas contas
        user1 = User.objects.create(username="user1", account=account1)
        user2 = User.objects.create(username="user2", account=account1)
        user3 = User.objects.create(username="user3", account=account2)

        # Criar algumas árvores plantadas por cada usuário
        PlantedTree.objects.create(age=10, user=user1, location="Local 1")
        PlantedTree.objects.create(age=15, user=user1, location="Local 2")
        PlantedTree.objects.create(age=8, user=user2, location="Local 3")
        PlantedTree.objects.create(age=12, user=user3, location="Local 4")
        # Adicione mais árvores plantadas conforme necessário

    def test_scenario(self):
        # Verificar se as contas foram criadas corretamente
        self.assertEqual(Account.objects.count(), 2)

        # Verificar se os usuários foram distribuídos corretamente nas contas
        self.assertEqual(User.objects.filter(account__name="Conta 1").count(), 2)
        self.assertEqual(User.objects.filter(account__name="Conta 2").count(), 1)

        # Verificar se as árvores plantadas foram criadas corretamente
        self.assertEqual(PlantedTree.objects.count(), 4)
