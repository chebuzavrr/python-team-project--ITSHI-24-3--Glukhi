from converter_logic import convert_currency, log_operation, RATES


def main():
    print("=== Консольний конвертер валют ===")
    print(f"Доступні валюти: {', '.join(RATES.keys())}")

    while True:
        try:
            print("-" * 35)
            amount_str = input("Введіть суму (або '0' для виходу): ")
            amount = float(amount_str)

            if amount == 0:
                print("Роботу завершено. Гарного дня!")
                break

            from_curr = input("З якої валюти (наприклад, USD): ").strip().upper()
            to_curr = input("У яку валюту (наприклад, UAH): ").strip().upper()

            # Викликаємо функції з модуля логіки
            result = convert_currency(amount, from_curr, to_curr)
            print(f"\n=> РЕЗУЛЬТАТ: {amount} {from_curr} = {result} {to_curr}")

            log_operation(amount, from_curr, to_curr, result)
            print("=> [Операцію успішно збережено в journal.txt]")

        except ValueError as e:
            if "could not convert" in str(e):
                print("Помилка: введіть коректне число!")
            else:
                print(f"Помилка: {e}")
        except Exception as e:
            print(f"Сталася непередбачувана помилка: {e}")


main()