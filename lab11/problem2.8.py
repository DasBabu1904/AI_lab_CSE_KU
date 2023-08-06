import random
from os import name

###problem 2.8
class ReflexVacuumAgent:
    def __init__(self):
        pass

    def decide_action(self, location, is_dirty):
        if is_dirty:
            return "Suck"
        else:
            if location == 0:
                return "Right"
            elif location == 1:
                return "Left"


class VacuumCleanerEnvironment:
    def __init__(self):
        self.tiles = [False, False]
        self.agent_location = 0
        self.performance_measure = 0

    def is_tile_dirty(self, tile):
        return self.tiles[tile]

    def clean_tile(self, tile):
        self.tiles[tile] = False

    def move_left(self):
        if self.agent_location > 0:
            self.agent_location -= 1

    def move_right(self):
        if self.agent_location < 1:
            self.agent_location += 1

    def suck(self):
        if self.is_tile_dirty(self.agent_location):
            self.clean_tile(self.agent_location)
            self.performance_measure += 1

    def step(self, action):
        if action == "Left":
            self.move_left()
        elif action == "Right":
            self.move_right()
        elif action == "Suck":
            self.suck()
        else:
            raise ValueError("Invalid action.")


        self.performance_measure -= 1

        return self.performance_measure

    def get_agent_location(self):
        return self.agent_location

    def set_tile_dirt_status(self, left_tile_dirty, right_tile_dirty):
        self.tiles = [left_tile_dirty, right_tile_dirty]


def run_simulation():
    agent = ReflexVacuumAgent()
    total_score = 0
    num_simulations = 0


    for left_tile_dirty in [True, False]:
        for right_tile_dirty in [True, False]:
            for agent_location in [0, 1]:
                num_simulations += 1


                environment = VacuumCleanerEnvironment()
                environment.set_tile_dirt_status(left_tile_dirty, right_tile_dirty)
                environment.agent_location = agent_location


                for time_step in range(1000):
                    current_tile = environment.get_agent_location()
                    is_dirty = environment.is_tile_dirty(current_tile)
                    dirt_status = "dirty" if is_dirty else "clean"


                    action = agent.decide_action(current_tile, is_dirty)
                    environment.step(action)
                    environment.set_tile_dirt_status(random.choice([True, False]),random.choice([True, False]) )


                final_score = environment.performance_measure
                total_score += final_score

                print(f"Dirt Location: [Left: {left_tile_dirty}, Right: {right_tile_dirty}] \n"
                      f"Agent Location: {agent_location}  \nPerformance: {final_score}\n--------------------------")

    average_score = total_score / num_simulations
    print(f"\nOverall Average Score: {average_score}")


run_simulation()
