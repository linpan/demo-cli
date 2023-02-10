# But if you import the models before calling SQLModel.metadata.create_all(), it will work:

# fixme from .user import  User

# todo: beanies register models
# import sys
# from typing import Sequence, Type, TypeVar
#
# from beanie import Document
#
# # All database models must be imported here to be able to
# # initialize them on startup.
# from .url import ShortUrl
# from .user import User
#
# DocType = TypeVar("DocType", bound=Document)
#
#
# def gather_documents() -> Sequence[Type[DocType]]:
#     """Returns a list of all MongoDB document models defined in `models` module."""
#     from inspect import getmembers, isclass
#
#     return [
#         doc
#         for _, doc in getmembers(sys.modules[__name__], isclass)
#         if issubclass(doc, Document) and doc.__name__ != "Document"
#     ]

# class DateTimeModelMixin(BaseModel):
#     created_at: Optional[datetime] = Schema(..., alias="createdAt")
#     updated_at: Optional[datetime] = Schema(..., alias="updatedAt")