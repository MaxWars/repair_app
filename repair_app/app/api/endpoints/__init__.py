from .users import router as users_router
from .devices import router as devices_router
from .requests import router as requests_router

__all__ = ["users_router", "devices_router", "requests_router"]