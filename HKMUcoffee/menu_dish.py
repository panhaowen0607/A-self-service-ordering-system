from base_classes import Dish

class MainCourse(Dish):
    def get_type(self):
        return "Main Course"

class Snack(Dish):
    def get_type(self):
        return "Snack"

class Drink(Dish):
    def get_type(self):
        return "Drink"

class Menu:
    def __init__(self):
        self.dishes = [] 

    def add_dish(self, dish):
        if isinstance(dish, Dish):
            self.dishes.append(dish)
        else:
            print("Add failed: Not a valid Dish object!")

    def show_menu(self):
        print("\n===== 📋 HKMUcoffee Menu =====")
        dish_types = ["Main Course", "Snack", "Drink"]
        for t in dish_types:
            print(f"\n【{t}】")
            type_dishes = [d for d in self.dishes if d.get_type() == t]
            if not type_dishes:
                print("  No dishes available")
                continue
            for idx, dish in enumerate(type_dishes, 1):
                print(f"  {idx}. {dish.name:12} Student: ${dish.student_price:5.2f} | Teacher: ${dish.teacher_price:5.2f} | Normal: ${dish.normal_price:5.2f}")

    def get_dish_by_index(self, idx):
        if 0 <= idx < len(self.dishes):
            return self.dishes[idx]
        return None

    def init_default_dishes(self):
        self.add_dish(MainCourse("x", 1,2,3))
        self.add_dish(MainCourse("y", 1,2,3))
        self.add_dish(MainCourse("z", 1,2,3))
        self.add_dish(Snack("h", 1,2,3))
        self.add_dish(Snack("y", 1,2,3))
        self.add_dish(Snack("j", 1,2,3))
        self.add_dish(Drink("s", 1,2,3))
        self.add_dish(Drink("o", 1,2,3))
        self.add_dish(Drink("3", 1,3,3))
