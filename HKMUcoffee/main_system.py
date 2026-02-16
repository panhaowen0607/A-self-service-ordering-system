from user_classes import Student, Teacher, NormalUser
from menu_dish import Menu
from cart_order import Cart, Order
from sales_record import SalesRecord


class HKMUCoffeeSystem:
    def __init__(self):
        self.sales_record = SalesRecord()  
        self.menu = Menu()                 
        self.menu.init_default_dishes()   
        self.current_user = None          
        self.current_cart = None           
        self.orders = []                  

    def user_login(self):
        print("\n===== 👋 Welcome to HKMUcoffee Ordering System =====")
        while True:
            print("\nPlease select your identity:")
            print("1. HKMU Student (8-digit student ID required)")
            print("2. HKMU Teacher")
            print("3. Non-campus User")
            choice = input("Enter your choice (1/2/3): ")
            if choice not in ["1", "2", "3"]:
                print("❌ Invalid input! Please enter 1, 2 or 3.")
                continue
            while True:
                phone = input("Enter your 8-digit mobile phone number: ")
                if phone.isdigit() and len(phone) == 8:
                    break
                print("❌ Invalid phone number! Must be 8 digits (no letters/symbols). Please try again.")
            if choice == "1":
                while True:
                    student_id = input("Enter your 8-digit HKMU student ID: ")
                    if student_id.isdigit() and len(student_id) == 8:
                        break
                    print("❌ Invalid student ID! Must be 8 digits (no letters/symbols). Please try again.")
                self.current_user = Student(phone, student_id)
            elif choice == "2":
                teacher_id = input("Enter your HKMU teacher ID: ")
                self.current_user = Teacher(phone, teacher_id)
            else:
                self.current_user = NormalUser(phone)
            self.current_cart = Cart(self.current_user, self.menu)
            print(f"\n✅ Login successful! {self.current_user.__class__.__name__} | Phone: {phone} | Current Balance: ${self.current_user.get_balance():.2f}")
            break

    def cart_operation(self):
        while True:
            print("\n===== ⚙️  Cart Operations =====")
            print("1. View Menu and Add Dishes")
            print("2. View Cart and Delete Dishes")
            print("3. Checkout")
            print("4. Exit Ordering")
            choice = input("Enter your choice (1/2/3/4): ")
            if choice == "1":
                self.menu.show_menu()
                while True:
                    try:
                        dish_idx = int(input("Enter dish number to add (enter 0 to return): "))
                        if dish_idx == 0:
                            break
                        num = int(input("Enter quantity: "))
                        self.current_cart.add_dish(dish_idx, num)
                    except ValueError:
                        print("❌ Invalid input! Please enter a number.")
            elif choice == "2":
                self.current_cart.show_cart()
                if not self.current_cart.selected_dishes:
                    continue
                while True:
                    try:
                        dish_idx = int(input("Enter dish number to delete (enter 0 to return): "))
                        if dish_idx == 0:
                            break
                        num = int(input("Enter quantity: "))
                        self.current_cart.remove_dish(dish_idx, num)
                    except ValueError:
                        print("❌ Invalid input! Please enter a number.")
            elif choice == "3":
                self.checkout()
                break
            elif choice == "4":
                print("👋 Exited ordering system! Welcome back next time.")
                exit()
            else:
                print("❌ Invalid input! Please enter 1,2,3 or 4.")

    def checkout(self):
        total = self.current_cart.calculate_total()
        if total == 0:
            print("❌ Checkout failed: Cart is empty!")
            return
        print(f"\n===== 💵 Checkout Page =====")
        print(f"💰 Discounted Total: ${total:.2f}")
        print(f"💳 Current Balance: ${self.current_user.get_balance():.2f}")

        while self.current_user.get_balance() < total:
            if isinstance(self.current_user, NormalUser):
                print(f"✅ Non-campus user paid ${total:.2f} directly! Payment successful.")
                break
            print("⚠️  Insufficient balance! Please recharge first.")
            try:
                recharge_amount = float(input("Enter recharge amount: $"))
                self.current_user.recharge(recharge_amount)
            except ValueError:
                print("❌ Invalid recharge amount! Please enter a number.")
                continue

        if not isinstance(self.current_user, NormalUser):
            self.current_user.balance -= total
            print(f"✅ Balance deducted successfully! Remaining balance: ${self.current_user.get_balance():.2f}")


        new_order = Order(self.current_user, self.current_cart)
        self.orders.append(new_order)
        print(f"✅ Order created successfully! Order ID: {new_order.order_id}")
        new_order.show_order_detail()

        
        self.sales_record.add_sales(total)
        print(f"📈 Store Total Sales: ${self.sales_record.get_total():.2f}")

        self.current_cart.clear_cart()
        self.update_order_status(new_order)

    def update_order_status(self, order: Order):
        
        while True:
            print(f"\n===== 📊 Order [{order.order_id}] Status Management =====")
            print(f"Current Status: {order.status}")
            print("1. Update to Being Made")
            print("2. Update to Completed")
            print("3. Return to Main Menu")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                order.update_status(Order.MAKING)
            elif choice == "2":
                order.update_status(Order.COMPLETED)
                if order.status == Order.COMPLETED:
                    print(f"🍽️  Order [{order.order_id}] is completed! Enjoy your meal!")
                    break
            elif choice == "3":
                print("✅ Returned to main menu! Continue ordering.")
                break
            else:
                print("❌ Invalid input! Please enter 1,2 or 3.")

    def run(self):
        self.user_login()
        while True:
            self.cart_operation()
            continue_choice = input("\nContinue ordering? (y/n): ")
            if continue_choice.lower() != "y":
                print("👋 Thank you for using HKMUcoffee! Welcome back next time.")
                break

if __name__ == "__main__":
    coffee_system = HKMUCoffeeSystem()
    coffee_system.run()
