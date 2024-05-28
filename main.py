from datetime import datetime

class Customer:
    def __init__(self, name, category, plan, subscription_plan):
        self.name = name
        self.category = category
        self.plan = plan
        self.meal_off_lunch = False
        self.meal_off_dinner = False
        self.subscription_plan = subscription_plan

    # Feature 1
    def turn_off_meal(self, meal_type):
        current_hour = datetime.now().hour
    
        if meal_type == "lunch" and not self.meal_off_lunch and 0 <= current_hour < 22:
            print(f"{self.name}: Turning off lunch")
            self.meal_off_lunch = True
        elif meal_type == "dinner" and not self.meal_off_dinner and 0 <= current_hour < 15:
            print(f"{self.name}: Turning off dinner")
            self.meal_off_dinner = True
        elif meal_type == "both" and not self.meal_off_lunch and not self.meal_off_dinner and 0 <= current_hour < 22:
            print(f"{self.name}: Turning off both lunch and dinner")
            self.meal_off_lunch = True
            self.meal_off_dinner = True


class SubscriptionPlan:
    def __init__(self, days):
        self.days = days
        self.lunch_balance = 5 * days  # Suppose, $5 per meal
        self.dinner_balance = 8 * days  # Suppose, $8 per meal

    # Feature 2
    def balance_reduce(self, meal_type):
        if meal_type == "both":
            self.lunch_balance -= 5
            self.dinner_balance -= 8
        elif meal_type == "lunch":
            self.lunch_balance -= 5
        elif meal_type == "dinner":
            self.dinner_balance -= 8

# Feature 3
class AdminPanel:
    def __init__(self, customers):
        self.customers = customers

    def visualize_orders(self):
        orders = []
        
        for customer in self.customers:
            if not customer.meal_off_lunch:
                orders.append({"category": customer.category, "meal_type": "lunch"})
            if not customer.meal_off_dinner:
                orders.append({"category": customer.category, "meal_type": "dinner"})


        basic_lunch_orders = sum(1 for order in orders if order["category"] == "Basic" and order["meal_type"] == "lunch")
        premium_lunch_orders = sum(1 for order in orders if order["category"] == "Premium" and order["meal_type"] == "lunch")
        basic_dinner_orders = sum(1 for order in orders if order["category"] == "Basic" and order["meal_type"] == "dinner")
        premium_dinner_orders = sum(1 for order in orders if order["category"] == "Premium" and order["meal_type"] == "dinner")

        print("Today's Orders:")
        print("For Lunch:")
        print("Basic =", basic_lunch_orders)
        print("Premium =", premium_lunch_orders)
        print("For Dinner:")
        print("Basic =", basic_dinner_orders)
        print("Premium =", premium_dinner_orders)


if __name__ == '__main__':
    customer1 = Customer("Customer 1", "Basic", "7 Days", SubscriptionPlan(7))
    customer2 = Customer("Customer 2", "Premium", "30 Days", SubscriptionPlan(30))
    customer3 = Customer("Customer 3", "Premium", "7 Days", SubscriptionPlan(7))
    customer1.turn_off_meal("lunch")
    customer3.turn_off_meal("both")
    
    admin_panel = AdminPanel([customer1, customer2, customer3])
    admin_panel.visualize_orders()
