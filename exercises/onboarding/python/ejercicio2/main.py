"""
Recientemente en la startup donde trabajas se decidió comenzar a explorar las
criptomonedas como posible mecanismo de inversión. Es por esto que el manager
del equipo de data te sugiere a ti como Data Engineer de la empresa que
investigues acerca del tema. Además menciona que existen muchas APIs gratuitas
que proveen información en tiempo real del Bitcoin. Pero, él te sugiere que
investigues acerca de la API Messari (https://data.messari.io/api/v1/assets/bitcoin/metrics)
ya que es gratuita. Además te pide que para el final del día le muestres una
implementación en Python de como extraer la información diariamente del precio
del Bitcoin de forma recurrente. Las variables que se deberían capturar son
fecha, volume_last_24_hours, open, close, low y high como se muestra a
continuación:


{
    'fecha': '2023-07-10T19:21:23.001268478Z',
    'volume_last_24_hours': 6482076059.128203,
    'open': 30348.621341725313,
    'low': 30348.621341725313,
    'close': 30530.379477108152,
    'high': 30530.379477108152
}
"""

import requests


def main():
    url = "https://data.messari.io/api/v1/assets/bitcoin/metrics"
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Invalid url response")

    response_json = response.json()
    data = response_json["data"]
    status_timestamp = response_json["status"]["timestamp"]
    market_data = data["market_data"]
    
    output = {
        "fecha": status_timestamp,
        "volume_last_24_hours": market_data["volume_last_24_hours"],
        "open": market_data["ohlcv_last_1_hour"]["open"],
        "low": market_data["ohlcv_last_1_hour"]["low"],
        "close": market_data["ohlcv_last_1_hour"]["close"],
        "high": market_data["ohlcv_last_1_hour"]["high"],
    }

    print(output)


if __name__ == "__main__":
    main()
