import random

class ReflexVacuumAgent:
    def __init__(self):
        pass

    def decide_action(self, location, is_dirty):
        if is_dirty:
            return "Suck"
        else:
            return random.choice(["Left", "Right", "Up", "Down"])

class VacuumCleanerEnvironment:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.tiles = [[False for _ in range(dimensions[1])] for _ in range(dimensions[0])]
        self.agent_location = (0, 0)
        self.performance_measure = 0
        self.obstacles = [[False for _ in range(dimensions[1])] for _ in range(dimensions[0])]

    def is_tile_dirty(self, tile):
        x, y = tile
        return self.tiles[x][y]

    def clean_tile(self, tile):
        x, y = tile
        self.tiles[x][y] = False

    def place_obstacles(self):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                self.obstacles[x][y] = random.choice([True, False]) if (x, y) != self.agent_location and random.random() < 0.125 else False

    def move_left(self):
        x, y = self.agent_location
        if y > 0 and not self.obstacles[x][y - 1]:
            self.agent_location = (x, y - 1)

    def move_right(self):
        x, y = self.agent_location
        if y < self.dimensions[1] - 1 and not self.obstacles[x][y + 1]:
            self.agent_location = (x, y + 1)

    def move_up(self):
        x, y = self.agent_location
        if x > 0 and not self.obstacles[x - 1][y]:
            self.agent_location = (x - 1, y)

    def move_down(self):
        x, y = self.agent_location
        if x < self.dimensions[0] - 1 and not self.obstacles[x + 1][y]:
            self.agent_location = (x + 1, y)

    def suck(self):
        if self.is_tile_dirty(self.agent_location):
            self.clean_tile(self.agent_location)
            self.performance_measure -= 1

    def step(self, action):
        if action == "Left":
            self.move_left()
        elif action == "Right":
            self.move_right()
        elif action == "Up":
            self.move_up()
        elif action == "Down":
            self.move_down()
        elif action == "Suck":  # Include the "Suck" action
            self.suck()
        else:
            raise ValueError("Invalid action.")
        self.performance_measure += 1

        return self.performance_measure

    def get_agent_location(self):
        return self.agent_location

    def initialize_dirt(self, exclude_tile):
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                if (x, y) != exclude_tile:
                    self.tiles[x][y] = random.choice([True, False])

def run_simulation(dimensions, num_simulations):
    agent = ReflexVacuumAgent()
    total_score = 0

    for _ in range(num_simulations):
        environment = VacuumCleanerEnvironment(dimensions)
        current_tile = environment.get_agent_location()

        for time_step in range(1000):
            environment.initialize_dirt(current_tile)
            environment.place_obstacles()
            is_dirty = environment.is_tile_dirty(current_tile)
            action = agent.decide_action(current_tile, is_dirty)
            environment.step(action)
            current_tile = environment.get_agent_location()

        final_score = environment.performance_measure
        total_score += final_score

        print("Obstacle pattern: \n----------------------------")
        for ob in environment.obstacles:
            print(ob)
        print(f" \n--------------------------\nPerformance: {final_score}\n--------------------------\n")

    average_score = total_score / num_simulations
    print(f"\nOverall Average Score: {average_score}")

# Run the simulation with a 4x4 grid and 10 simulations
run_simulation((4, 4), 10)
