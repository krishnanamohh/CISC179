from .ElectronicDevice import ElectronicDevice
from flask import Flask, request

class Smartphone(ElectronicDevice):
    def __init__(self, power_source, manufacturer, model):
        super().__init__(power_source, manufacturer)
        self.model = model

    def make_call(self, number):
        print("Calling", number)

    def send_message(self, recipient, message):
        print("Sending message to", recipient)


