from src.config import settings
from src.log_config import logger
import httpx


async def get_exchange_rate(client: httpx.AsyncClient, from_currency: str, to_currency: str) -> float | None:
    url = f'{settings.base_url}/{settings.api_key}/latest/{from_currency}'
    response = await client.get(url)
    if response.status_code == 200:
        rates = response.json().get('conversion_rates', None)
        return rates.get(to_currency)
    else:
        logger.warning(f'Response status code is {response.status_code}, 200 expected')
        return None


