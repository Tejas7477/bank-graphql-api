import graphene
from graphene_django.types import DjangoObjectType
from .models import Bank, Branch

# --- Define BankType ---
class BankType(DjangoObjectType):
    class Meta:
        model = Bank
        fields = "__all__"  # Exposes all fields of the Bank model

# --- Define BranchType ---
class BranchType(DjangoObjectType):
    class Meta:
        model = Branch
        fields = "__all__"  # Exposes all fields of the Branch model

# --- Define Queries ---
class Query(graphene.ObjectType):
    all_banks = graphene.List(BankType)
    all_branches = graphene.List(BranchType)
    branches_by_city = graphene.List(BranchType, city=graphene.String(required=True))  # filter by city

    def resolve_all_banks(self, info, **kwargs):
        return Bank.objects.all()

    def resolve_all_branches(self, info, **kwargs):
        return Branch.objects.select_related('bank').all()

    def resolve_branches_by_city(self, info, city):
        return Branch.objects.filter(city__iexact=city)

# --- Create Schema ---
schema = graphene.Schema(query=Query)
