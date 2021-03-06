import random
import sys
from viruses import viruses
import virus
random.seed(43)
from person import Person
from logger import Logger

'''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    _____Attributes______
    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.
    population_size: Int.  The size of the population for this simulation.
    population: [Person].  A list of person objects representing all people in
        the population.
    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.
    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.
    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.
    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.
    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.
    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.
    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.
    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.
    _____Methods_____
    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.
    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
'''

class Simulation(object):
    
    def __init__(self, population_size, vacc_percentage, virus, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.all_infected = []
        self.all_alive = []
        self.next_person_id = 0
        self.virus_name = virus.name
        self.mortality_rate = virus.mortality_rate
        self.basic_repro_num = virus.infection_rate
        self.virus = virus
        self.dead = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            self.virus_name, self.population_size, vacc_percentage, initial_infected)

        # TODO: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        print("Logger start")
        self.logger = Logger(self.file_name)
        print('logger start')
        self.logger.write_metadata(self.population_size, vacc_percentage, self.virus_name,
                     self.mortality_rate, self.basic_repro_num, initial_infected)

        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.  At the end of each time step, we'll call
        # self._infect_newly_infected() and then reset .newly_infected back to an empty
        # list.
        self.population = self._create_population(self.population_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.

    def _create_population(self, population_size, vacc_percentage, initial_infected):
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        population = []
        infected_count = 0
        for i in range(population_size):
            self.all_alive.append(i)
            if infected_count <  initial_infected:
                population.append(Person(i,False,self.virus))
                self.all_infected.append(i)
                infected_count+=1
                # TODO: Create all the infected people first, and then worry about the rest.
                # Don't forget to increment infected_count every time you create a
                # new infected person!
            else:
                if(random.random()<=vacc_percentage):
                    population.append(Person(i,True))
                    # print(population[i]._id)
                else:
                    population.append(Person(i,False))
                # Now create all the rest of the people.
                # Every time a new person will be created, generate a random number between
                # 0 and 1.  If this number is smaller than vacc_percentage, this person
                # should be created as a vaccinated person. If not, the person should be
                # created as an unvaccinated person.
            # TODO: After any Person object is created, whether sick or healthy,
            # you will need to increment self.next_person_id by 1. Each Person object's
            # ID has to be unique!
        return population

    def _simulation_should_continue(self):
        if(len(self.all_infected)==0 or len(self.all_alive)==0):
            if(len(self.all_infected)==0):
                # print((self.all_alive))
                self.logger.log_end_game("The Infection has been eradicated, there were {} people left".format(len(self.all_alive)))
            else:
                self.logger.log_end_game("The Population has been eradicated")

            return False
        return True
        # TODO: Complete this method!  This method should return True if the simulation
        # should continue, or False if it should not.  The simulation should end under
        # any of the following circumstances:
        #     - The entire population is dead.
        #     - There are no infected people left in the population.
        # In all other instances, the simulation should continue.
        

    def run(self):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0
        # TODO: Remember to set this variable to an intial call of
        # self._simulation_should_continue()!
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.logger.log_time_step(time_step_counter,True)
            self.time_step(time_step_counter)
            time_step_counter+=1
            should_continue = self._simulation_should_continue()
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()!
        print('The simulation has ended after {} turns.'.format(time_step_counter))

    def time_step(self,time_step_counter):
        for person in self.all_infected:
            for i in range(100):
                person2 = self.all_alive[random.randint(0,len(self.all_alive)-1)]
                self.interaction(self.population[person],self.population[person2])

        self._kill_infected()
        self._infect_newly_infected()
        self.logger.log_time_step(time_step_counter,False)


        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.


    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert person.is_alive == True
        assert random_person.is_alive == True
        if(random_person.infection==None):
            if(not random_person.is_vaccinated):
                if(random.random()<=self.basic_repro_num):
                    self.newly_infected.append(random_person._id)
                    self.logger.log_interaction(person,random_person,did_infect=True)
                else:
                    self.logger.log_interaction(person,random_person,did_infect=False)
            else:
                self.logger.log_interaction(person,random_person,False,True)

        else:
            self.logger.log_interaction(person,random_person,False,random_person.is_vaccinated,random_person.infection.name)




    def _kill_infected(self):
        for person in self.all_infected:
            # print(self.population[person]._id)
            self.all_infected.remove(person)
            survival = self.population[person].did_survive_infection()
            # print(person," ",survival)
            if not(survival):
                self.all_alive.remove(person)
                # print(person, " removed")
                self.dead+=1
                self.logger.log_infection_survival(person,False)
            else:
                self.logger.log_infection_survival(person,True)
        # print(self.dead)


    def _infect_newly_infected(self):
        self.newly_infected = list(set(self.newly_infected))
        self.logger.log_new_infected(self.newly_infected)
        for i in self.newly_infected:
            person = self.population[i]
            if(person.infection == None):
                person.infection = self.virus
                self.all_infected.append(i)
        self.newly_infected = []


        # TODO: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!

if __name__ == "__main__":
    for v in range(len(viruses)):
        viruses[v].display(v)
    my_virus = viruses[int(input("which virus would you like to use? "))]
    per_vacc = float(input("what percentage of the population is vaccinated? "))
    simulation = Simulation(1000, .5, my_virus)
    simulation.run()
