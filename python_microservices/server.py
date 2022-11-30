""" system module for fastapi endpoints """
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

import razorpay

app = FastAPI(
    title="Palavv FastAPI Microservices",
    openapi_url="/api/v1/openapi.json",
)

app.include_router(razorpay.router, prefix="/payments", tags=["payments"])

# pylint: disable=duplicate-code
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """Custom swagger UI"""
    if os.environ.get("STAGE") == "dev":
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title="Palavv API",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        )
    return {"Not Allowed": "Send requests to appropriate microservices"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
