from graphene import ObjectType, String


class User(ObjectType):
    field = String()
