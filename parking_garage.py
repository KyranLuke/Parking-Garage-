class parking_Garage():
    def __init__(self): 
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_spots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.current_ticket = {}

    def take_ticket(self):
        if not self.parking_spots:
            print("Parking lot is full.")
            return
        else:
            ticket = self.tickets.pop(0)
            self.parking_spots.pop(0)
            self.current_ticket[ticket]="unpaid" 
            print(self.tickets, self.parking_spots, self.current_ticket)
        
    def pay_for_parking(self):
        ticket = int(input("What is your ticket no: "))

        if self.current_ticket[ticket] == "paid":
            print("Your ticket has been paid and you have fifteen minutes to leave the parking lot.")
        elif input("Please enter card number: "):
            print("Your ticket has been paid and you have fifteen minutes to leave the parking lot.")
            self.current_ticket[ticket]="paid"         
            print(self.tickets, self.parking_spots, self.current_ticket)
        else:
            print("Invaild Input")
        
class function():
    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def the_funk(self):
        while True:
            ask = input("Would you like to park, pay or quit: ")

            if ask.lower() == "park":
                self.parking_lot.take_ticket()
            elif ask.lower() == "pay":
                self.parking_lot.pay_for_parking()
            elif ask.lower() == "quit":
                print("Thank you have a great day!")
                break
            else:
                print("Invaild Input")

parking = function(parking_Garage())
parking.the_funk()