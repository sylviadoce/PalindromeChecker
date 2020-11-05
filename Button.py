#
# Sylvia Chin
#
# Button class module - drawing left and right buttons, enabling click function
#
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The activeandclicked(pt) method
    returns true if the button is active and pt is inside it,
    and the clicked(pt) method returns true just if the pt is
    inside it."""

    def __init__(self, win, center, width, height, label):
        "Creates a rectangular button"

        # Define what center means using the width and height
            # dimensions
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, pt):
        "Returns true if pt is inside button"
        return (self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def activeandclicked(self, pt):
        "Returns true if button active and pt is inside"
        return (self.active and
                self.xmin <= pt.getX() <= self.xmax and
                self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def setLabel(self, newText):
        "Changes the label string of this button to newText."
        self.label.setText(newText)
            
    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill("darkgray")
        self.rect.setWidth(1)
        self.active = False

    def undraw(self):
        "Undraws the button from the window."
        self.rect.undraw()
        self.label.undraw()
    
