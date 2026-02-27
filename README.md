## COMP2090SEF_course_project-task1

Group member: Cao Fei(13755803), Pan HaoWen(13752390),

## 👀:Contents

- [The usage of the OOP concepts](#function)
- [Update](#update)
- [Contact](#contact)


## <a name="function"></a>🤔: The usage of the OOP concepts
1➡️ **Abstraction** hides complex implementation details and exposes only essential features (via abstract classes/methods).
- Dish and User in base_classes,py are abstract classes with @abstractmethod(These methods define a "contract" (required behavior) for subclasses but do not implement logic themselves.).
 ```shell
    from abc import ABC, abstractmethod
    class Dish(ABC):
        def __init__(self, name, student_price, teacher_price, normal_price):
            self.name = name          
            self.student_price = student_price  
            self.teacher_price = teacher_price  
            self.normal_price = normal_price   

        @abstractmethod
        def get_type(self):
            pass
 ```

2➡️ **Inheritance** allows a class to reuse code from a parent class and extend its functionality.eg: In the menu_dish.py, the parent calss is Dish. and the children class are Main Course, Snack, and Drink. 

![image alt](https://github.com/caofei351-ops/A-self-service-ordering-system/blob/bf5d1e309110b66c0719e8fdad8a9e12d1b72837/Inheritance.png)

3➡️ **Polymorphism** allows different subclasses to implement the same method in unique ways which makse the code more flexible and scalable.

(1) get-type() for Dishes
- MainCourse.get_type() → “Main Course"
- Snack.get_type() → “Snack"
- Drink.get_type() → “Drink"

The menu system (Menu.show_menu()) calls get_type() on any Dish subclass(no need to checj the exact type:
 ```shell
    type_dishes = [d for d in self.dishes if d.get_type() == t]
 ```
(2) get_discount() for Users
- Student.get_discount() → “0.9"(10% off)
- Teacher.get_discount() → “0.9"(10% off)
- NormalUser.get_discount() →“1.0"（no discount)

The cart (Cart.calculate_total()) uses user.get_discount():
 ```shell
    discount = self.user.get_discount() # work for any user subclass
 ```

4➡️ The **encapsulation** combines data (attributes) and the methods for operating on these data into a class, and restricts direct access to the internal state through access modifiers/conventions (Prevents invalid state and centralizes validation logic).
- Private/Protected Attributes: SalesRecord uses _instance to enforce the Singleton pattern (prevents direct modification).
 ```shell
    class SalesRecord:
    _instance = None 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
 ```
- Controlled Access via Methods: Instead of directly modifying balance, users call recharge() & Instead of directly changing selected_dishes, cart uses add_dish()/remove_dish().
```shell
    class Student(User):
    def recharge(self, amount):
        if amount >= 0:  # Validation logic
            self.balance += amount
        else:
            print("The amount cannot be negative!")
```
5➡️ **Singleton Pattern**:A specialized OOP pattern ensuring a class has only one instance (global access to a single object).
- SalesRecord in sales_record.py implements Singleton to track total sales across the system:
```shell
    class SalesRecord:
    _instance = None  
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.total_sales = 0.0  
        return cls._instance
```
- The HKMUCoffeeSystem initializes self.sales_record = SalesRecord()—all orders share the same SalesRecord instance, so total sales are aggregated correctly.

6➡️ **Composition** uses objects of other classes as attributes to build complex functionality (Builds modular, reusable components).
- Cart has-a User and Menu (depends on them to calculate totals/add dishes):
```shell
    class Cart:
    def __init__(self, user: User, menu: Menu):
        self.user: User = user        
        self.menu: Menu = menu   
```
- Order has-a copy of Cart details (uses copy.deepcopy to preserve order history):
```shell
    self.cart_detail: List[Tuple[Dish, int]] = copy.deepcopy(cart.selected_dishes)  
```

## <a name="update"></a>Update
- **2026.01.29**: We form our group and study what is Github and how to use it.
- **2026.02.03**: We reviewed the specific requirements for the group project. At the same time we analyzed some project examples from the previous semester and Github. Finally, we chose the ordering system of HLMU coffee as our task 1.
- **2026.02.06**:The specific process of the code has been determined.
- **2026.02.06**:The specific division of labor for Task 1 has been determined.
- **2026.02.17**:CaoFei finishs the major code for task1.
  
## <a name="contact"></a>💙:Contact
If you have any questions about our project, please email us with `s1375580@live.hkmu.edu.hk`,`s1375239@live.hkmu.edu.hk`,
