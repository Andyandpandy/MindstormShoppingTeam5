import json

import requests


class Service:
    def __init__(self):
        self.endpoint = "https://3xef1f6fnc.execute-api.eu-west-1.amazonaws.com/Testing/commandsfromshopper"
        self.productIDS = [10851, 60156, 76093, 41594, 75193]
        print("Welcome to the LEGO store")
        self.name = input("What is your name? ")
        print("The Lego store has in total 5 items.")


    def start_service(self):

        while True:
            print("The product id's that exist are: ", self.productIDS)
            options = input("There are 5 options. Choose one of the following by entering the number: Would you like to insert the (1) productID, tell us about some (2) characteristics (age, hobbies), describe the product (3) textually you are looking for, describe it (4) verbally or show a (5) picture of what you are looking for?")
            if options == "1":
                self.id_option()
            elif options == "2":
                self.characteristics_option()

            else:
                print("That is not a number in the range of 1-5")


    def get_product(self):
        return self.productID

    def send_request_with_id(self, p_id):

        response = requests.post(self.endpoint, json.dumps({"name": self.name, "msg": "", "id": str(p_id)}))
        print(response.content)


    def id_option(self):
        try:
            print("Which of the following products would you like?")
            print(self.productIDS)
            pID = int(input("Please type the product ID you would like: "))
            if pID in self.productIDS:
                self.productID = pID
                self.send_request_with_id()
            else:
                print("This id is not one of the following: ", self.productIDS)
        except Exception as e:
            print(e.with_traceback())
            print("This is not an ID!")

    def characteristics_option(self):
        try:
            age = input("How old are you?")
            hobbies = input("What hobbies interest you?")
            self.send_request({"name": self.name, "msg": "", "age": str(age), "hobbies": hobbies})
        except Exception as e:
            print(e.with_traceback())
            print("This is not an ID!")

    def send_request(self, data):
        response = requests.post(self.endpoint, json.dumps(data))
        print(response.content)