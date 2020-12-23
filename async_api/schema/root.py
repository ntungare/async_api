from graphene import Field, ID, NonNull, ObjectType

from async_api.resolvers.user_resolver import get_user
from .user import User


class Query(ObjectType):
    user = Field(User, resolver=get_user, args={"id": NonNull(ID)})
