import csv


class ExchangeRates:
    """Read the latest USD-to-CAD exchange rate and convert between currencies."""

    def __init__(self, filename):
        # Read the CSV rows and keep the final row, which has the latest rate.
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            rows = csv.DictReader(file)
            latest_row = None
            for row in rows:
                latest_row = row

        if latest_row is None:
            raise ValueError("The exchange-rate CSV file does not contain any data.")

        self.exchange_rate = float(latest_row["FXAUSDCAD"])

    def convert(self, amount, original_currency, target_currency):
        """Convert an amount between USD and CAD."""
        original_currency = original_currency.upper()
        target_currency = target_currency.upper()

        if original_currency == "USD" and target_currency == "CAD":
            return amount * self.exchange_rate
        if original_currency == "CAD" and target_currency == "USD":
            return amount / self.exchange_rate
        if original_currency == target_currency and original_currency in ("USD", "CAD"):
            return amount

        raise ValueError("Supported currencies are USD and CAD.")


# Ask the user for the amount and the currencies to convert.
filename = "BankOfCanadaExchangeRate.2026.csv"
exchange_rates = ExchangeRates(filename)

amount = float(input("Enter the amount to convert: "))
original_currency = input("Enter the original currency (USD or CAD): ").strip().upper()
target_currency = input("Enter the target currency (USD or CAD): ").strip().upper()

# Display the latest exchange rate and the converted amount.
converted_amount = exchange_rates.convert(amount, original_currency, target_currency)
print(f"Current exchange rate (USD to CAD): {exchange_rates.exchange_rate:.4f}")
print(f"Converted amount: ${converted_amount:.2f} {target_currency}")