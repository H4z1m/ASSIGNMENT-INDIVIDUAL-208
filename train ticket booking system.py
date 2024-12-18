class Train:
    def __init__(self, train_id, train_name, destination, available_seats, price):
        self.train_id = ("111", "112", "113")
        self.train_name = ("Platinum, Gold, Express Line")
        self.destination = ("Kangar", "Kota Bharu", "Johor Bahru")
        self.available_seats = ("Kangar : 50","Kota Bharu : 30","Johor Bahru : 120")
        self.price = ("Kangar : RM100","Kota Bharu : RM120","Johor Bahru : RM90")

    def book_ticket(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            total_cost = num_tickets * self.price
            return True, total_cost
        else:
            return False, 0

    def __str__(self):
        return f"Train ID: {self.train_id}, Name: {self.train_name}, Destination: {self.destination}, Available Seats: {self.available_seats}, Price per Ticket: {self.price}"

class TicketBookingSystem:
    def __init__(self):
        self.trains = [
            Train(111, "Platinum 111", "Kangar", 50),
            Train(112, "Gold 112", "Kota Bharu", 30),
            Train(113, "Express line 113", "Johor Bahru", 120)
        ]
        self.bookings = []

    def show_trains(self):
        print("\nAvailable Trains:")
        for train in self.trains:
            print(train)

    def book_ticket(self):
        self.show_trains()
        try:
            train_id = int(input("\nEnter Train ID to book ticket: "))
            num_tickets = int(input("Enter number of tickets to book: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return

        train = next((train for train in self.trains if train.train_id == train_id), None)
        if not train:
            print("Train ID not found!")
            return

        success, total_cost = train.book_ticket(num_tickets)
        if success:
            print(f"Successfully booked {num_tickets} ticket(s) on {train.train_name}. Total cost: ${total_cost}.")
            self.bookings.append({
                'train_id': train.train_id,
                'train_name': train.train_name,
                'destination': train.destination,
                'tickets': num_tickets,
                'total_cost': total_cost
            })
        else:
            print("Not enough available seats!")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings yet.")
        else:
            print("\nYour Bookings:")
            for booking in self.bookings:
                print(f"Train: {booking['train_name']}, Destination: {booking['destination']}, Tickets: {booking['tickets']}, Total Cost: ${booking['total_cost']}")


def main():
    system = TicketBookingSystem()

    while True:
        print("\nTrain Ticket Booking System")
        print("1. Show Available Trains")
        print("2. Book a Ticket")
        print("3. View Bookings")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a valid option.")
            continue

        if choice == 1:
            system.show_trains()
        elif choice == 2:
            system.book_ticket()
        elif choice == 3:
            system.view_bookings()
        elif choice == 4:
            print("Thank you for using the Train Ticket Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
