import json

import requests


class Service:
    def __init__(self):
        self.endpoint = "https://3xef1f6fnc.execute-api.eu-west-1.amazonaws.com/Testing/commandsfromshopper"
        self.productIDS = [10851, 60156, 76093, 41594, 75193]
        print("Welcome to the LEGO store")
        self.name = input("What is your name? ")
        print("The Lego store has in total 5 items.")
        print("These items have productIDs")
        print("Which of the following products would you like?")
        print(self.productIDS)
        self.productID = None
        while self.productID is None:
            pID = None
            try:
                pID = int(input("Please type the product ID you would like: "))
            except Exception as e:
                print(e)

            if pID in self.productIDS:
                self.productID = pID
                print("Getting the product now..")
                print("Please wait")
                self.send_request_with_id(pID)
            else:
                print("This id is not one of the following: ", self.productIDS)

    def start_service(self):
        print("Which of the following products would you like?")
        print(self.productIDS)
        while True:
            try:
                pID = int(input("Please type the product ID you would like: "))
                if pID in self.productIDS:
                    self.productID = pID

                else:
                    print("This id is not one of the following: ", self.productIDS)
            except Exception as e:
                print(e.with_traceback())
                print("This is not an ID!")

    def get_product(self):
        return self.productID

    def send_request_with_id(self, p_id):

        response = requests.post(self.endpoint, json.dumps({"name": self.name, "msg": "", "id": str(p_id)}))
        print(response.status_code)
        print(response.content)
        print(response.request)
