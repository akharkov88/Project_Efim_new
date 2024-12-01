from fastapi import APIRouter

from . import (
    auth,
    operations,
    reports,
    BaseFile,
    main,
    techTask,
    techTaskForm,
    suggest,
    UserProfile,
    Telegram,
    searchCompanyINN,
)


router = APIRouter()
router.include_router(auth.router)
router.include_router(operations.router)
router.include_router(reports.router)
# router.include_router(js_router.router)
router.include_router(main.router)
router.include_router(techTask.router)
router.include_router(techTaskForm.router)
router.include_router(BaseFile.router)
router.include_router(suggest.router)
router.include_router(UserProfile.router)
router.include_router(searchCompanyINN.router)
