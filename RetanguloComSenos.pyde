c1, c2 = 100, 150

def setup():
    size(500, 500)
    
def draw():
    strokeWeight(5)
    background(200, 0, 0)
    tam1 = 5 + 130 * sin(radians(frameCount))
    rect (175, 150, c2, 200, tam1)
    rect (175, 50, c2, 50, tam1)
    rect (175, 400, c2, 50, tam1)
    rect (20, 150, c1, 200, tam1)
    rect (20, 50, c1, 50, tam1)
    rect (20, 400, c1, 50, tam1)
    rect (380, 150, c1, 200, tam1)
    rect (380, 50, c1, 50, tam1)
    rect (380, 400, c1, 50, tam1)
