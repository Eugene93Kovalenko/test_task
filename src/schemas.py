from pydantic import BaseModel
from decimal import Decimal


class ExchangeResponse(BaseModel):
    result: Decimal
