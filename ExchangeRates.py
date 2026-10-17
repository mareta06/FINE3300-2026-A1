#Import the csv module to read data from a CSV file
import csv

#Define the ExchangeRates class
class ExchangeRates:
    
    def __init__(self,filename):

        #Read the CSV file and retrieve the USD/CAD exchange rate from the last row
        with open(filename, "r") as file:
            reader= csv.DictReader(file)
    
            rows = list(reader)
    
            self.exchange_rate = float(rows[-1]["FXAUSDCAD"]) 


    #Check the currencies and calculate the converted amount
    def convert(self, amount, original_currency, target_currency):
        if original_currency == "USD" and target_currency == "CAD":
            return amount * self.exchange_rate
        elif original_currency == "CAD" and target_currency == "USD":
            return amount / self.exchange_rate
        #Raise an error if the currency conversion is invalid
        else:
            raise ValueError("Invalid currency conversion. Please use USD or CAD.")

#Create an object and load the exchange rate from the CSV file
a = ExchangeRates("BankOfCanadaExchangeRate.2026.csv") 

#Display the calculator introduction and current exchange rate
print("Welcome to the USD/CAD Currency Exchange Calculator! The current exchange rate for USD to CAD is:", a.exchange_rate)
print("Please enter the following information:")

#Space for readability     
print()

#Ask the user for the amount and currencies
amount = float(input("What is the amount of money you would like to convert?: $"))
original_currency = input("What is the original currency? (Enter USD or CAD): ")
target_currency = input("What is the target currency? (Enter USD or CAD): ")

#Space for readability     
print()

#Convert the amount and display the result to two decimal places
print(f"This is your converted amount: ${a.convert(amount, original_currency, target_currency):.2f} {target_currency}")
