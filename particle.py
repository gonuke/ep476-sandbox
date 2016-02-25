class Particle(object):
    """
    A basic class for defining many types of particle
    for this package, all masses are in units of electron mass
    """
    # start my class here
    def __init__(self,new_mass=1,new_charge=-1,new_position=(0,0,0)):
         
        self.mass = new_mass
 	self.charge = new_charge
	self.position = new_position

    def report(self):

	rep = ("This is a particle with a mass of " + str(self.mass) +
              " a charge of " + str(self.charge) + 
              " at a location of (x,y,z)=" + str(self.position)   )
        return str(rep)

class Quark(Particle):

    def __init__(self,flav):
        Particle.__init__(self)
        self.flavor = flav











   
