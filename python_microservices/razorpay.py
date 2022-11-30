""" System modules for payments """
import hmac
import json
import logging
from hashlib import sha256

from fastapi import APIRouter, HTTPException, Request

from .model import PaymentCreation, PaymentVerificationResponse

router = APIRouter()


logger = logging.getLogger(__name__)


@router.post("/payment_verification", response_model=PaymentVerificationResponse)
def send_message(message: PaymentCreation, request: Request) -> PaymentVerificationResponse:
    """Send a message to a user"""
    try:
        key = bytes("987654321", "utf-8")
        body = bytes(json.dumps(message, separators=(",", ":")), "utf-8")

        signature = str(request.headers.get("x-razorpay-signature"))
        digest = str(hmac.new(key, body, sha256).hexdigest())
        if hmac.compare_digest(digest, signature):
            return PaymentVerificationResponse(message="Success", verification=True)
        return PaymentVerificationResponse(message="Failure", verification=False)
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error)) from error
