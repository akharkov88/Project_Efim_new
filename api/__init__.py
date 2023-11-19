from fastapi import APIRouter

from . import (
    auth,
    operations,
    reports,
    # js_router,
    main,
)


router = APIRouter()
router.include_router(auth.router)
router.include_router(operations.router)
router.include_router(reports.router)
# router.include_router(js_router.router)
router.include_router(main.router)
