import requests

class CryptoModel:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3/simple/price"

    def get_prices(self, crypto_ids: list, currency: str = "dkk") -> dict:

        ids_param = ",".join(crypto_ids)
        params = {
            "ids": ids_param,
            "vs_currencies": currency,
            "include_24hr_change": "true"
        }
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(self.base_url, params=params, headers=headers, timeout=5)
            response.raise_for_status() 
            return response.json()      
        except requests.exceptions.RequestException:
            return None