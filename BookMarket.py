
import mesa
import random

class BookSeller(mesa.Agent):
    def __init__(self, unique_id, model, avg_price):
        super().__init__(unique_id, model)
        self.price = self.price = round(random.uniform(avg_price - avg_price * 0.5, avg_price + avg_price * 0.5), 2)

    def step(self):
        print(f"seller {self.unique_id} Selling book at price: {self.price}$")

class BookBuyer(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.best_price = float('inf')
        self.best_seller = None

    def step(self):
        # Check all sellers for the best price
        for seller in self.model.plan.agents:
            if isinstance(seller, BookSeller):
                if seller.price < self.best_price:
                    self.best_price = seller.price
                    self.best_seller = seller.unique_id
        
        if self.best_seller is not None:
            print(f"Buyer {self.unique_id} found best price {self.best_price}$ from Seller {self.best_seller}")


class BookMarket(mesa.Model):
    def __init__(self, avg_price):
        self.num_sellers = 5
        self.plan = mesa.time.BaseScheduler(self)



        # Create sellers
        for i in range(self.num_sellers):
            seller = BookSeller(i + 2, self, avg_price)
            self.plan.add(seller)

        buyer = BookBuyer(1, self)
        self.plan.add(buyer)

    def step(self):
        print("the buyer want a book !!!!")
        self.plan.step()

# Example usage
avg_price = random.randint(50, 200)
model = BookMarket(avg_price=avg_price)
model.step()

