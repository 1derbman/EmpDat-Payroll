from tkinter import *

# from PIL import imageTk, Image
from UserData import *
from GuiValues import *
import main as m

''' to use images yoy need to install pillow
install with "pip install pillow" on your python to use
ImageTk.PhotoImage(Image.open("imagename.png"))
put image in widget
then put on page
'''

''' everything is a widget
start with a self
 widget
this shoudl be first every time you use tkinter'''
'''define the action the function will take'''


class EnterNewEmployee(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        gv = GuiValues(self, controller)
        gv.create_nav_bar()

        gv.newEmployeeButton.place(x=0, y=40)
        gv.findEmployeeButton.place(x=0, y=80)
        gv.importEmployeeButton.place(x=0, y=120)
        gv.saveProfileButton.place(x=0, y=160)

        # Labels
        gv.fNameLabel.place(x=200, y=40)
        gv.lNameLabel.place(x=200, y=65)
        gv.addressLabel.place(x=200, y=90)
        gv.addressLineTwoLabel.place(x=200, y=115)
        gv.cityLabel.place(x=200, y=140)
        gv.stateLabel.place(x=200, y=165)
        gv.zipCodeLabel.place(x=200, y=190)
        gv.phoneLabel.place(x=200, y=215)
        gv.classificationLabel.place(x=200, y=240)
        gv.empNumberLabel.place(x=200, y=265)
        gv.passwordLabel.place(x=200, y=290)
        gv.departmentLabel.place(x=200, y=315)
        gv.payRateLabel.place(x=200, y=340)
        gv.payYTDLabel.place(x=200, y=365)
        gv.securityAccessLabel.place(x=200, y=390)

        # Inputs
        gv.fNameInput.place(x=340, y=40, width=gv.inputWidth, height=gv.inputHeight)
        gv.lNameInput.place(x=340, y=65, width=gv.inputWidth, height=gv.inputHeight)
        gv.addressInput.place(x=340, y=90, width=gv.inputWidth, height=gv.inputHeight)
        gv.addressTwoInput.place(x=340, y=115, width=gv.inputWidth, height=gv.inputHeight)
        gv.cityInput.place(x=340, y=140, width=gv.inputWidth, height=gv.inputHeight)
        gv.stateInput.place(x=340, y=165, width=gv.inputWidth, height=gv.inputHeight)
        gv.zipInput.place(x=340, y=190, width=gv.inputWidth, height=gv.inputHeight)
        gv.phoneInput.place(x=340, y=215, width=gv.inputWidth, height=gv.inputHeight)
        gv.classInput.place(x=340, y=240, width=gv.inputWidth, height=gv.inputHeight)
        gv.empNumInput.place(x=340, y=265, width=gv.inputWidth, height=gv.inputHeight)
        gv.passwordInput.place(x=340, y=290, width=gv.inputWidth, height=gv.inputHeight)
        gv.departmentInput.place(x=340, y=315, width=gv.inputWidth, height=gv.inputHeight)
        gv.payRateInput.place(x=340, y=340, width=gv.inputWidth, height=gv.inputHeight)
        gv.payYTDInput.place(x=340, y=365, width=gv.inputWidth, height=gv.inputHeight)
        gv.securityInput.place(x=340, y=390, width=gv.inputWidth, height=gv.inputHeight)

    def pay(self):
        self.controller.show_frame("PayrollProcessing")

    def employees(self):
        self.controller.show_frame("FindEmployee")

    def timecards(self):
        pass

    def sales(self):
        pass

    def myProfile(self):
        self.controller.show_frame("MyProfile")

    def newEmployee(self):
        self.controller.show_frame("EnterNewEmployee")

    def findEmployee(self):
        self.controller.show_frame("FindEmployee")

    def importEmployee(self):
        pass

    def saveChanges(self):
        pass