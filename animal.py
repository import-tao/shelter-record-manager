class Animal(object):
    '''
    Representation of an animal profile for use in shelter data management apps.
    
    Requires an id number at time of initialization, which should be incremented
    and tracked by the application.
    '''
    self.id = None
    self.name = None
    self.species = None
    self.breed = None
    self.color = None
    self.demeanor = None
    self.medical_needs = None
    self.dietary_needs = None
    self.location = None  # facility, room, cage number, etc.
    self.adoption_status = None
    self.caretaker = None  # dict, or custom class to be used?
    self.home_history = None  # where it lived, who it lived with

    def __init__(self, id):
        self.id = id
    
    def set_adopted(self, caretaker):
        '''
        Accepts a caretaker object.
        Sets self.caretaker to the accepted object.
        Sets adoption status to "adopted".
        '''
        self.caretaker = caretaker
        self.adoption_status = 'adopted'