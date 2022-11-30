"""Module imports for razor pay model."""
from pydantic import BaseModel

razorpay_payment_confirmation = {
    "entity": "event",
    "account_id": "acc_G72vxaouAxEfTp",
    "event": "payment.captured",
    "contains": ["payment"],
    "payload": {
        "payment": {
            "entity": {
                "id": "pay_KjqqJ8bYhTlGTW",
                "entity": "payment",
                "amount": 300000,
                "currency": "INR",
                "status": "captured",
                "order_id": "order_KjqpGXsEy7GhS3",
                "invoice_id": None,
                "international": False,
                "method": "card",
                "amount_refunded": 0,
                "refund_status": None,
                "captured": True,
                "description": "Palavv Checkout ",
                "card_id": "card_KjqqJBB6abG80R",
                "card": {
                    "id": "card_KjqqJBB6abG80R",
                    "entity": "card",
                    "name": "",
                    "last4": "1111",
                    "network": "Visa",
                    "type": "debit",
                    "issuer": None,
                    "international": False,
                    "emi": False,
                    "sub_type": "consumer",
                    "token_iin": None,
                },
                "bank": None,
                "wallet": None,
                "vpa": None,
                "email": "malikarif13@gmail.com",
                "contact": "+917506811767",
                "notes": {"uid": "order_KjqpGXsEy7GhS3", "item": "Long coat grey", "contact": "07506811767"},
                "fee": 7080,
                "tax": 1080,
                "error_code": None,
                "error_description": None,
                "acquirer_data": {"auth_code": "417304"},
                "created_at": 1669287531,
                "base_amount": 300000,
            },
        },
    },
    "created_at": 1669287582,
}


class Card(BaseModel):
    id: str
    entity: str
    name: str
    last4: str
    network: str
    type: str
    issuer: str
    international: bool
    emi: bool
    sub_type: str
    token_iin: str


class Entity(BaseModel):
    id: str
    entity: str
    amount: int
    currency: str
    status: str
    order_id: str
    invoice_id: str
    international: bool
    method: str
    amount_refunded: int
    refund_status: str
    captured: bool
    description: str
    card_id: str
    card: Card
    bank: str
    wallet: str
    vpa: str
    email: str
    contact: str
    notes: dict
    fee: int
    tax: int
    error_code: str
    error_description: str
    acquirer_data: dict
    created_at: int
    base_amount: int


class Payment(BaseModel):
    entity: Entity


class Payload(BaseModel):
    payment: Payment


class PaymentCreation(BaseModel):
    entity: str
    account_id: str
    event: str
    contains: list
    payload: Payload
    created_at: int

    class Config:
        schema_extra = razorpay_payment_confirmation


class PaymentVerificationResponse(BaseModel):
    message: str
    verification: bool
