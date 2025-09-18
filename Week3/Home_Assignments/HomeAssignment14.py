""" Assignment Details: 
 
You are building a payment system that supports multiple payment methods. 
 
Requirements: 
a) Create three classes: CreditCardPayment, PayPalPayment, and BankTransferPayment. 
b) In each class, define a method process_payment(amount) that prints how the payment is 
processed. Examples: 
 CreditCardPayment → "Processing credit card payment of $<amount>" 
 PayPalPayment → "Processing PayPal payment of $<amount>" 
 BankTransferPayment → "Processing bank transfer of $<amount>" 
c) Write a function make_payment(payment_method, amount) that accepts an object and 
calls its process_payment(amount) method. 
d) In the main section: 
 Create one object of each payment class. 
 Call make_payment() with different payment objects to demonstrate polymorphism. 
Hints: 
1. Each class implements the same method name process_payment() but with different logic. 
2. Polymorphism is shown when the same function (make_payment) can work with different 
object types. 
3. Use a loop to call make_payment() for multiple payment objects.  """

class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

# Main execution
if __name__ == "__main__":
    # Create payment method objects
    cc = CreditCardPayment()
    pp = PayPalPayment()
    bt = BankTransferPayment()

    # List of methods and amounts
    payments = [cc, pp, bt]
    amounts = [100, 75.5, 250]

    # Demonstrate polymorphism
    for method, amt in zip(payments, amounts):
        make_payment(method, amt)