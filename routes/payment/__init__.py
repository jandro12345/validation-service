"""
Route for payment
"""

import json
import jwt
from fastapi import APIRouter, Response, Depends
from psycopg2.extras import RealDictCursor
from psycopg2 import connect
from psycopg2.errors import UniqueViolation

from models.payment import AddPayment
from tool import DSN, verification_token

payment_route = APIRouter(prefix="/payment")


@payment_route.post("/add", dependencies=[Depends(verification_token)])
async def add_payment(payment_data: AddPayment, response: Response):
    """
    Route for add_payment
    """
    body = {}
    with connect(dsn=DSN, cursor_factory=RealDictCursor) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select
                    pm.payment_method_id,
                    c.names,
                    c.mail,
                    case
                        when pm.validate_fund < %(amount)s
                        then
                        False
                        else
                        True
                        end as validate_fund
                from
                    tbl_payment_method as pm
                left join
                    tbl_client as c
                on
                    c.client_id=pm.client_id
                where
                    pm.status='t' and
                    pm.number=%(number)s and
                    pm.expiration_date=%(expiration_date)s and
                    pm.cvv_static=%(cvv_static)s
                """,
                {
                    "number": payment_data.number,
                    "expiration_date": payment_data.expiration_date,
                    "cvv_static": payment_data.cvv,
                    "amount": payment_data.amount
                },
            )
            data = cur.fetchone()
            if not data:
                response.status_code = 400
                body = {
                    "Message": "Invalid Credencials",
                    "Error": True,
                }
                return body
            elif not data.get("validate_fund"):
                response.status_code = 400
                body = {
                    "Message": "Insufficient Funds",
                    "Error": True,
                }
                return body
            send_data = {
                "payment_method_id": data["payment_method_id"],
                "info_user": {
                    "names": data["names"],
                    "mail": data["mail"]
                },
                "amount": payment_data.amount
            }
            body = {
                "data": send_data
            }
    return body
