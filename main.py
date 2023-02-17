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
        self.fps: int = 10

        self.num_edges = 6
        self.n = 1/2
        self.radius = 1
        self.iter_num = 1
        self.distance = 300

        self.color = (255, 255, 255)
        self.current_pos = (0, 0)
        self._add_circle = self.add_circle()
        
    
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
        self.draw_circles(self.width//2, self.height//2)
        self.current_pos = self.choose_point(self.positions[0], self.positions[1], self.n)

        pygame.draw.circle(self.screen, self.color, self.rand_point_from_edges(), self.radius)

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
            yield max_degre-90
    
    def draw_circles(self, x1, y1):
        """draw circles of the triangle"""
        for angle in self.angles(self.num_edges):
            (x2,y2) = (x1 + self.distance*math.cos(math.radians(angle)),y1 + self.distance*math.sin(math.radians(angle)))
            self.positions.append((x2, y2))
            pygame.draw.circle(self.screen, self.color, (x2, y2), self.radius)
    
    def choose_point(self, p1, p2, n):
        """returns mid point of the two positions"""
        return abs(p1[0]-p2[0])*n, abs(p1[1]-p2[1])*n
    
    def rand_point_from_edges(self):
        """Choose random position from edges"""
        points = []
        positions = self.positions[1:]
        positions.append(self.positions[0])

        for i, pos in enumerate(positions):
            point = self.choose_point(pos, self.positions[i], random.random())
            points.append(point)    
            pygame.draw.circle(self.screen, self.color, point, self.radius)

        return random.choice(points)

    def add_circle(self):
        """Add circle to the screen"""

        while True:
            pos = random.choice(self.positions)
            mid = self.choose_point(self.current_pos, pos, self.n)
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