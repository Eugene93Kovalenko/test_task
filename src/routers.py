from decimal import Decimal

import httpx
from fastapi import APIRouter, HTTPException

from src.schemas import ExchangeResponse
from src.services import get_exchange_rate
from src.log_config import logger

router = APIRouter()


@router.get('/rates', response_model=ExchangeResponse)
async def get_rate(from_currency: str, to_currency: str, value: Decimal) -> ExchangeResponse:
    async with httpx.AsyncClient() as client:
        rate = await get_exchange_rate(client, from_currency, to_currency)
    if rate is None:
        logger.error(f'Invalid currency. Tried: {from_currency} to {to_currency}')
        raise HTTPException(status_code=400, detail="Invalid currency")
    result = round(Decimal(rate) * value, 2)
    logger.info(f'Successful request: {from_currency} to {to_currency}. Result: {rate}')
    return ExchangeResponse(result=result)
