from simulation import Simulation
from viruses import viruses

def test_sim_init():
    myVirus = viruses[5]
    sim = Simulation(20,.3,myVirus)
    assert sim.population_size == 20
    assert sim.virus is myVirus

def test_sim_create_pop():
    myVirus = viruses[5]
    sim = Simulation(20,.3,myVirus)
    assert len(sim.population) == 20
    assert sim.population[0].infection is myVirus

def test_sim_should_continue():
    myVirus = viruses[5]
    sim = Simulation(20,.3,myVirus)
    assert sim._simulation_should_continue()
    sim.population[0].did_survive_infection()
    sim.all_infected = []
    assert not sim._simulation_should_continue()

def test_time_step():
    myVirus = viruses[5]
    sim = Simulation(20,0,myVirus)
    assert sim.population[0].infection is myVirus

    sim.time_step(0)
    print(sim.population[0].infection)
    assert 0 not in sim.all_infected
