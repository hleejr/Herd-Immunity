import person
import virus

def test_person_init():
    """confirm init complete"""
    my_person = person.Person(3,False)
    assert my_person._id is 3
    assert my_person.infection is None

def test_infection():
    my_virus = virus.Virus("cold",infection_rate=.5,mortality_rate=0)
    my_person = person.Person(3,False,my_virus)
    assert my_person._id is 3
    assert my_person.infection is my_virus

def test_person_death():
    # tests the did survive infection function
    my_virus = virus.Virus("death",infection_rate=.5,mortality_rate=1)
    my_person = person.Person(0,False,my_virus)
    my_person.did_survive_infection() #Has to kill you
    assert my_person.is_alive is False

def test_person_survive():
    my_virus = virus.Virus("cold",infection_rate=.5,mortality_rate=0)
    my_person = person.Person(0,False,my_virus)
    my_person.did_survive_infection() #Cant kill you
    assert my_person.is_alive is True
