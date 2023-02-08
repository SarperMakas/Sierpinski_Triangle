"""
Siepinski triangle visualization
"""
import pygame, math, random

class Main:
    def __init__(self):
        pygame.init()

        # define screen and other informations related to
        self.width: int = 650
        self.height: int = 650
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sierpinski Triangle")


        self.run: bool = True
        self.run_simulation: bool = False
        self.positions = []

        self.clock = pygame.time.Clock()
        self.fps: int = 100

        self.num_edges = 3
        self.distance = 350
        self.color = (255, 255, 255)
        self.radius = 1
        self.current_pos = (0, 0)
        self._add_circle = self.add_circle()
        self.iter_num = 1
    
    def event(self):
        """Main event loop"""
        for event in pygame.event.get():
            # check game quit
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
                if event.key == pygame.K_SPACE:
                    self.run_simulation = not self.run_simulation
                    print("Simualtion:", self.run_simulation)
    
    def main(self):
        """Main game loop"""
        self.draw_circles(self.width//2, self.height//2+50)
        self.current_pos = self.mid_point(self.positions[0], self.positions[1])
        while self.run:
            self.event()
            self.draw()

            self.clock.tick(self.fps)


    def angles(self, edge_num: int = 3):
        """Angles"""
        degre = 360 / edge_num
        max_degre = 0
        
        while max_degre < 360:
            max_degre += degre
            yield (max_degre+30) % 360
    
    def draw_circles(self, x1, y1):
        """draw circles of the triangle"""
        for angle in self.angles(self.num_edges):
            (x2,y2) = (x1 + self.distance*math.cos(math.radians(angle)),y1 + self.distance*math.sin(math.radians(angle)))
            self.positions.append((x2, y2))
            pygame.draw.circle(self.screen, self.color, (x2, y2), self.radius)
    
    def mid_point(self, p1, p2):
        """returns mid point of the two positions"""
        return (p1[0]+p2[0])/2, (p1[1]+p2[1])/2

    def add_circle(self):
        """Add circle to the screen"""

        while True:
            pos = random.choice(self.positions)
            mid = self.mid_point(self.current_pos, pos)
            self.current_pos = mid
            pygame.draw.circle(self.screen, self.color, (mid[0], mid[1]), self.radius)
            yield
            

    
    def draw(self):
        """Main draw method"""

        if self.run_simulation:
            for _ in range(self.iter_num):
                next(self._add_circle)

        pygame.display.flip()


Main().main()