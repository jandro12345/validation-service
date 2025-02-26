"""
Model for Payment
"""

from pydantic import BaseModel, constr, confloat


class AddPayment(BaseModel):
    """
    Model for post AddPayment
    """

    number: constr(max_length=16)
    expiration_date: constr(max_length=5)
    cvv: constr(max_length=3)
    amount: confloat(gt=0)

