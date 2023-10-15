from sense_hat import SenseHat
import time

class TrafficLight:
    def __init__(self):
        self.sense = SenseHat()
        self.state = 0
        self.paused = False
        self.colors = {
            'r': (255, 0, 0),
            'g': (0, 255, 0),
            'y': (255, 255, 0),
            'n': (0, 0, 0)
        }
        self.patterns = {
            'red': [self.colors['r']] * 8 + [self.colors['n']] * 56,
            'red_yellow': [self.colors['r']] * 8 + [self.colors['y']] * 8 + [self.colors['n']] * 48,
            'yellow': [self.colors['n']] * 8 + [self.colors['y']] * 8 + [self.colors['n']] * 48,
            'green': [self.colors['n']] * 16 + [self.colors['g']] * 8 + [self.colors['n']] * 40
        }
        self.sense.stick.direction_middle = self.button_event
        self.sense.stick.direction_up = self.pause_event
    
    def state_function(self, pattern, duration):
        if not self.paused:
            self.sense.set_pixels(pattern)
            time.sleep(duration)
            self.sense.clear()

    def set_state(self):
        if self.state < 3:
            self.state += 1
        elif self.state == 3:
            self.state = 0

    def button_event(self, event):
        if event.action == 'released':
            self.state = 4 if self.state != 4 else 0

    def pause_event(self, event):
        if event.action == 'pressed':
            self.paused = not self.paused
    
    def run(self):
        while True:
            if self.state == 4:
                self.state_function(self.patterns['yellow'], 0.5)
            elif not self.paused:
                states = [
                    {'pattern': self.patterns['red'], 'duration': 3},
                    {'pattern': self.patterns['red_yellow'], 'duration': 1},
                    {'pattern': self.patterns['green'], 'duration': 2},
                    {'pattern': self.patterns['yellow'], 'duration': 1}
                ]
                
                current = states[self.state]
                self.state_function(current['pattern'], current['duration'])
                self.set_state()


# Create an instance of the TrafficLight class and run the traffic light simulation
traffic_light = TrafficLight()
traffic_light.run()
