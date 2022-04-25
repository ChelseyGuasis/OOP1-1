#PROGRAM.1

def main():
 class TemperatureConversion:
  def __init__(self, temp=1):
   self._temp = temp

 class CelsiusToFahrenheit(TemperatureConversion):
  def conversion(self):
   return (self._temp * 9) / 5 + 32

 class CelsiusToKelvin(TemperatureConversion):
  def conversion(self):
   return self._temp + 273.15

 class FahrenheitToCelsius(TemperatureConversion):
  def conversion(self):
   return (self._temp - 32) * 5/9

 class KelvinToCelsius(TemperatureConversion):
  def conversion(self):
   return self._temp - 273.15

 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit")

 tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
 convert = FahrenheitToCelsius(tempInFahrenheit)
 print(str(convert.conversion()) + " Celsius")

 tempInKelvin = float(input("Enter the temperature in Kelvin: "))
 convert = KelvinToCelsius(tempInKelvin)
 print(str(convert.conversion()) + " Celsius")


main()

#PROGRAM 2.
import tkinter
from tkinter import*

window = Tk()
window.title("Midterm in OOP")
window.geometry("500x300+20+10")

lbl = Label(window, text="Enter your fullname:", fg="red")
lbl.place(x=50,y=100)

txtfld = Entry(window, bd=5, font=("Arial",12))
txtfld.place(x=250, y=100)

txtfld1 = Entry(window, bd=5, font=("Arial",12))
txtfld1.place(x=250, y=150)

def clicked():
    value=txtfld.get()
    txtfld1.insert(END, str(value))

bttn= Button(window, text="Click to display your Fullname", fg="red", command=clicked)
bttn.place(x=50,y=150)

window.mainloop()