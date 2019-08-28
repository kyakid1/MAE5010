#					TITLE BLOCK
#**************************************************
#Author:	Brandon White
#Date:		08/26/2019
#Desc:		Creates a MAV object with mass, moment
#           of inertia, and gravity properties
#**************************************************

#Calling the class with an aircraft name below creates an MAV object
class MAV:
    def __init__(self, aircraft = "None"):
       #All units listed in English units as denoted
       self.name = aircraft
       self.mass = 10  # Mass (lbf)
       #Inert = [Ixz, Ix, Iy, Iz]
       self.inert = [20, 10, 10, 10]  # Moment of Inertia (lbf*ft^2)
       self.gravity_needed = False
       #State = [p_n, p_e, p_d, u, v, w, e0, e1, e2, e3, p, q, r]
       self.state0 = [0, 0, -500, 50, 0, 0, 1, 0, 0, 0, 0, 0, 0]
            #Level flight at 500 ft at 50 ft/s
       #FM = [Fx, Fy, Fz, Ell, M, N]
       self.FM = [0, 0, self.mass*32.2, 0, 0, 0]
            #Gravity ONLY in base model

       if aircraft != "None":
           try:
               method_to_call = getattr(self, aircraft.lower())
               method_to_call()
           except:
               print("No preconfig by given name: " + aircraft.lower())

    def update_mass(self, new_mass):
        #NOTE: Automatically updates gravity force in FM
        self.FM[2] -= self.mass * 32.2
        self.mass = new_mass
        self.FM[2] += self.mass * 32.2

    def update_inert(self, new_inert):
        self.inert = new_inert

    def update_state0(self, new_state):
        if len(new_state) != 12:
            print("Error - Not 13 items! \n You might need to convert angular\
                    values to quaternions...")
        else:
            self.state0 = new_state

    #Add templated aircraft below this line to pregenerate aircraft
    def temp(self):
        self.update_mass(500)
        self.update_inert([200, 50, 50, 50])
