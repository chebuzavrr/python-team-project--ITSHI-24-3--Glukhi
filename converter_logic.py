import datetime

RATES = {
    "USD": 44.9256,
    "EUR": 51.8352,
    "GBP": 60.0431,
    "PLN": 12.1888,
    "UAH": 1.0  # базова валюта
}

def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
    if from_curr not in RATES or to_curr not in RATES:
        raise ValueError("Обрано невідому валюту.")
    amount_in_uah = amount * RATES[from_curr]
    result = amount_in_uah / RATES[to_curr]
    return round(result, 2)

def log_operation(amount: float, from_curr: str, to_curr: str, result: float, filename: str = "journal.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Конвертація: {amount} {from_curr} -> {result} {to_curr}\n"
    with open(filename, "a", encoding="utf-8") as file:
        file.write(log_entry)