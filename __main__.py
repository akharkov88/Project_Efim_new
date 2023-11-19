import uvicorn

import settings


uvicorn.run(
    'accountr.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
