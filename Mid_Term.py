class Star_Cinema:
    _hall_list = []
    def entry_hall(self):
        self._hall_list.append(self)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.seats = {}
        self.show_list = []
        self.entry_hall()
        super().__init__()

    def entry_show(self,id,Movie_name,time):
        self.id = id
        self.Movie_name = Movie_name
        self.time = time
        self.show_list.append((id, Movie_name, time))
        seat_arrangement = [['0' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.seats[id] = seat_arrangement

    def book_seats(self,id,seat_list):
        if id not in self.seats:
            print("Invalid ID. Please give correct ID!")
            return
        for i in range(0,len(seat_list),2):
            row = seat_list[i]
            col = seat_list[i+1]
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print("There is no such seat!")
                return
            elif self.seats[id][row][col] == '1':
                print("This seat is not available. Try another one!")
                return
            else:
                self.seats[id][row][col] = '1'
                print("Congrats!!You did it...Now enjoy.....")

    def view_show_list(self):
        for show in self.show_list:
            print(show)
    
    def view_available_seats(self,id):
        if id not in self.seats:
            print("Invalid ID.")
            return
        for row in range(self.__rows):
            for col in range(self.__cols):
                print(self.seats[id][row][col], end=" ")
            print()

star = Star_Cinema()
Cinoplex = Hall(5,5,1001)
Cinoplex.entry_show(1,'Spider_Man','9:00 AM')
Cinoplex.entry_show(2,'Iron_Man','12:00 PM')
Cinoplex.entry_show(3,'Super_Man','3:00 PM')

Square = Hall(6,6,1002)
Square.entry_show(1,'Avengers','12:00 PM')
Square.entry_show(2,'Fury','3:00 PM')
Square.entry_show(3,'Pirates','9:00 PM')

Monihar = Hall(7,7,1003)
Monihar.entry_show(1,'Instraller','9:00 AM')
Monihar.entry_show(2,'Breaking_Bad','12:00 PM')
Monihar.entry_show(3,'Openheighmar','3:00 PM')
Monihar.entry_show(4,'Openheighmar','6:00 PM')
Monihar.entry_show(5,'Conjuring','9:00 PM')

run = True
while run:
    print("\n---------------Welcome to our show---------------")

    print("\n1 : View all show today")
    print("\n2 : Show available seat")
    print("\n3 : Booking seat")
    print("\n4 : Exit")

    ch = int(input("\nEnter option: "))

    if ch == 1:
        id = int(input("Give hall id: "))
        if id == 1001:
            Cinoplex.view_show_list()
        elif id == 1002:
            Square.view_show_list()
        elif id == 1003:
            Monihar.view_show_list()
        else:
            print("\nID not found.\n")
    
    elif ch == 2:
        id = int(input("Give hall id: "))
        show_id = int(input("Enter show ID: "))
        if id == 1001:
            Cinoplex.view_available_seats(show_id)
        elif id == 1002:
            Square.view_available_seats(show_id)
        elif id == 1003:
            Monihar.view_available_seats(show_id)
    
    elif ch == 3:
        id = int(input("Give hall id: "))
        show_id = int(input("Enter show ID: "))
        seat_list = tuple(map(int,input("Which seat you want: ").split()))
        if id == 1001:
            Cinoplex.book_seats(show_id,seat_list)
        elif id == 1002:
            Square.book_seats(show_id,seat_list)
        elif id == 1003:
            Monihar.book_seats(show_id,seat_list)
    
    elif ch == 4:
        break
        
        