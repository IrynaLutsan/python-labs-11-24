class Sneakers:
    def __init__(self, brand, price, size, color, material):
        self.__brand = brand
        self.__size = size
        self.__color = color
        self.__price = price
        self.__material = material
    
    def __repr__(self):
        return f'Sneakers("{self.__brand}",\t{self.__price},\t{self.__size},\t{self.__color},\t{self.__material})'
    
    
    def get_brand(self):
        return self.__brand
    
    def get_size(self):
        return self.__size
    
    def get_color(self):
        return self.__color
    
    def get_price(self):
        return self.__price
    
    def get_material(self):
        return self.__material
    

      
class SportShoesStore:
    def __init__(self):
        self.__stock = []
        self.__soldItems = []
        
    def __listOfShoes2Str(self, lst):
        str = "["
        for sneakers in lst:
            str += "\n\t\t\t" + repr(sneakers)
        str += "]"
        return str
        
    def __str__(self):
        return f'SportShoesStore(\n\tstock = {self.__listOfShoes2Str(self.__stock)}, \n\tsoldItems = {self.__listOfShoes2Str(self.__soldItems)})'
        
        
    def updateStock(self, items):
        self.__stock.extend(items)
                
                
    def get_bestSellerBrand(self):
        tmp_dict = {}
        for shoes in self.__soldItems:
            if shoes.get_brand() in tmp_dict.keys():
                tmp_dict[shoes.get_brand()] += 1
            else:
                tmp_dict[shoes.get_brand()] = 1
        bestSeller = None
        sold = 0
        for brand in tmp_dict.keys():
            if tmp_dict[brand] > sold:
                sold = tmp_dict[brand]
                bestSeller = brand
        return bestSeller 
                
    
    def sellItems(self, items):
        for shoes in items:     #items - list
            found = False
            for i in range(0, len(self.__stock)):
                if shoes.get_brand() == self.__stock[i].get_brand() and shoes.get_price() == self.__stock[i].get_price() and shoes.get_size() == self.__stock[i].get_size() and shoes.get_color() == self.__stock[i].get_color() and shoes.get_material() == self.__stock[i].get_material():
                    found = True
                    del self.__stock[i]
                    self.__soldItems.append(shoes)
                    break
            if not found:
                print(f"Sneakers of brand '{shoes.get_brand()}', at price {shoes.get_price()}, size {shoes.get_size()}, color {shoes.get_color()}, material {shoes.get_material()} not available on the stock")
              
if __name__ == "__main__":
    store = SportShoesStore()
    print(store) #store is empty

    shipment1 =         [
                        Sneakers("Nike", 4999, 39, "black", "leather"),
                        Sneakers("Nike", 12500, 37, "orange", "leather"),
                        Sneakers("Nike", 7280, 41, "white", "fabric"),
                        Sneakers("Puma", 4999, 39, "black", "leather"),
                        Sneakers("Puma", 3000, 38, "red", "leather"),
                        Sneakers("Puma", 15999, 43, "purple", "leather"),
                        Sneakers("Puma", 2700, 35, "yellow", "fabric"),
                        Sneakers("Adidas", 6900, 39, "green", "leather"),
                        Sneakers("Adidas", 8000, 38, "blue", "leather"),
                        Sneakers("Adidas", 2399, 41, "white", "fabric"),
                        Sneakers("Adidas", 7099, 45, "black", "leather"),
                        ]

    shipment2 = [Sneakers("Nike", 25000, 39, "black", "leather")]
    store.updateStock(shipment1)
    print(store)   
    store.updateStock(shipment2)
    print(store)

    store.sellItems([
                        Sneakers("Puma", 4999, 39, "black", "leather"),
                        Sneakers("Puma", 3000, 38, "red", "leather"),
                        Sneakers("Adidas", 2399, 41, "white", "fabric"),
                        Sneakers("Puma", 1499, 37, "white", "fabric"),
                        Sneakers("Nike", 3700, 38, "pink", "fabric"),
                        Sneakers("Puma", 15999, 43, "purple", "leather"),
                        Sneakers("Adidas", 6900, 39, "green", "leather"),
                        Sneakers("Puma", 2700, 35, "yellow", "fabric")])
    print(store)
    store.sellItems([
                        Sneakers("Puma", 4999, 39, "black", "leather"),
                        Sneakers("Nike", 3700, 38, "pink", "fabric"),
                        Sneakers("Puma", 7280, 41, "white", "fabric"),
                        Sneakers("Pumba", 4699, 45, "black", "leather")])

    bestSeller = store.get_bestSellerBrand()
    print(f'bestseller of our store is: {bestSeller}')