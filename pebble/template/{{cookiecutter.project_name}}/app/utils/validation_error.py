from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ValidationError


class Error(BaseModel):
    location: str
    message: str
    error_type: str
    context: Optional[Dict[str, Any]] = None


class APIValidationError(BaseModel):
    """Schema for validation errors returned by the API with HTTP status code 422"""

    errors: List[Error]

    @classmethod
    def from_pydantic(cls, exc: ValidationError) -> "APIValidationError":
        """Create a new APIValidationError from a pydantic ValidationError"""
        return cls(
            errors=[
                Error(
                    location=" -> ".join(map(str, err["loc"])),
                    message=err["msg"],
                    error_type=err["type"],
                    context=err.get("ctx"),
                )
                for err in exc.errors()
            ],
        )

    class Config:
        schema_extra = {
            "example": {
                "errors": [
                    {
                        "origin": "body -> url",
                        "message": "invalid or missing URL scheme",
                        "error_type": "value_error.url.scheme",
                    },
                ],
            },
        }

# app = FastAPI(
#     debug=settings.DEBUG,
#     title=settings.PROJECT_NAME,
#     version=settings.PROJECT_VERSION,
#     description="Fast and reliable URL shortener powered by FastAPI and MongoDB.",
#     # Set current documentation specs to v1
#     openapi_url=f"/api/{settings.API_V1_STR}/openapi.json",
#     docs_url=None,
#     redoc_url=None,
#     default_response_class=ORJSONResponse,
#     openapi_tags=tags_metadata,
#     license_info={
#         "name": "GNU General Public License v3.0",
#         "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
#     },
#     responses={
#         status.HTTP_422_UNPROCESSABLE_ENTITY: {
#             "description": "Unprocessable Entity (Validation Error)",
#             "model": APIValidationError,  # This will add OpenAPI schema to the docs
#         },
#     },
# )

# Custom HTTPException handler
# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(_, exc: StarletteHTTPException) -> ORJSONResponse:
#     return ORJSONResponse(
#         content={
#             "message": exc.detail,
#         },
#         status_code=exc.status_code,
#         headers=exc.headers,
#     )
#
#
# @app.exception_handler(RequestValidationError)
# async def custom_validation_exception_handler(
#     _,
#     exc: RequestValidationError,
# ) -> ORJSONResponse:
#     return ORJSONResponse(
#         content=APIValidationError.from_pydantic(exc).dict(exclude_none=True),
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#     )