import time

class TrafficLight:
    def __init__(self, state="red", timer=3, name="Traffic Light"):
        self.state = state
        self.timer = timer
        self.name = name
        self.states = ["red", "green", "yellow"]  # cycle order
        self.index = 0  # track which state we’re in

    def get_reaction(self):
        if self.state == "red":
            return "Stop the Car"
        elif self.state == "yellow":
            return "Ready to Move"
        elif self.state == "green":
            return "Move the Car"
        else:
            return "Invalid State"

    def run_cycle(self, car, cycles=3):
        """Automatically run traffic light cycles"""
        for _ in range(cycles):
            # Current state reaction
            print(f"{self.name} is {self.state.upper()}")
            car.react_to_light(self)

            # Wait
            time.sleep(self.timer)

            # Move to next state
            self.index = (self.index + 1) % len(self.states)
            self.state = self.states[self.index]


class Car:
    def __init__(self, position=0, speed=0, name="Car"):
        self.position = position
        self.speed = speed
        self.name = name

    def react_to_light(self, traffic_light):
        reaction = traffic_light.get_reaction()
        print(f"{self.name}: {reaction}")


# --- Demo ---
light = TrafficLight(timer=2)  # each state lasts 2 seconds
car1 = Car(name="Toyota")

light.run_cycle(car1, cycles=6)  # run 6 automatic cycles
