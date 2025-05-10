from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentProcessor):
    def authenticate(self):
        return "Credit card OTP verified."

    def pay(self, amount):
        return f"Paid ₹{amount} via Credit Card."


class PayPal(PaymentProcessor):
    def authenticate(self):
        return "Logged in with PayPal credentials."

    def pay(self, amount):
        return f"Paid ₹{amount} via PayPal."


class CryptoWallet(PaymentProcessor):
    def authenticate(self):
        return "Crypto wallet signed with private key."

    def pay(self, amount):
        return f"Paid ₹{amount} in Bitcoin."


# 🔄 Polymorphism
def process_payment(processor: PaymentProcessor, amount):
    print(processor.authenticate())
    print(processor.pay(amount))


# 🧪 Testing
p1 = CreditCard()
p2 = PayPal()
p3 = CryptoWallet()

process_payment(p1, 1000)
print("---")
process_payment(p2, 2500)
print("---")
process_payment(p3, 5000)
