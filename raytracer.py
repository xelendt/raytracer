import numpy
import pygame
import math, time, sys

xres = 500
yres = 500

pygame.init()
win = pygame.display.set_mode((xres, yres), pygame.SRCALPHA)

def drawPixel(x, y, color):
#	pygame.gfxdraw.pixel(win, x, y, color)
		pygame.draw.line(win, color, (x+1, y), (x, y))

class point3d:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def draw(self):
		drawPixel(screenx, screeny)
	
	def dump(self):
		print self.x, self.y, self.z

class vector3d:
	def __init__(self, p1, p2):
		self.dx = p1.x-p2.x
		self.dy = p1.y-p2.y
		self.dz = p1.z-p2.z
		self.length = math.sqrt(self.dx*self.dx+ self.dy*self.dy+ self.dz*self.dz);

	def normalize(self):
		self.dx /= self.length
		self.dy /= self.length
		self.dz /= self.length
		self.length = 1
	def dump(self):
		print self.dx, self.dy, self.dz
		
class plane:
	def __init__(self, p1, p2, p3):
		self.p = p1
		self.v1 = vector3d(p1, p2)
		self.v2 = vector3d(p1, p3)
		n = numpy.cross([self.v1.dx, self.v1.dy, self.v1.dz], [self.v2.dx, self.v2.dy, self.v2.dz])
		self.normal = point3d(n[0], n[1], n[2])
	
	def intersect(self, ray):
		a = ([self.v1.dx, self.v2.dx, -1*ray.dx]
			,[self.v1.dy, self.v2.dy, -1*ray.dy]
			,[self.v1.dz, self.v2.dz, -1*ray.dz])
#	print a
		b = ([self.p.x, self.p.y, self.p.z])
		sol = numpy.linalg.solve(a, b)
		p = point3d(sol[0], sol[1], sol[2])
		return p
	def dump():
		self.normal.dump()

class triangle:
	def heron(self, p1, p2, p3):
		a = vector3d(p1, p2).length
		b = vector3d(p1, p3).length
		c = vector3d(p2, p3).length
		s = 0.5*(a+b+c)
		return math.sqrt(abs(s*(s-a)*(s-b)*(s-c)))
	def __init__(self, p1, p2, p3):
		self.p1 = p1;
		self.p2 = p2;
		self.p3 = p3;
		self.plane = plane(p1, p2, p3)
		self.normal = self.plane.normal
		self.area= self.heron(self.p1, self.p2, self.p3)

class light:
	def __init__(self, pos, intensity):
		self.pos = pos
		self.intensity = intensity

def event(e):
	if e.type == pygame.QUIT:
		sys.exit(0)

'''heron's formula
length of sides:a, b, c
s = (a+b+c)/2
area = sqrt( s(s-a)(s-b)(s-c) )
'''
'''testing'''
triangles = []
camera = point3d(0, 0, -1)
screen = point3d(0, 0, 0)
ray = vector3d(camera, screen)
'''===== first triangle ======= '''
p1 = point3d(0, 0, 10)
p2 = point3d(100, -100, 10)
p3 = point3d(100, 0, 10)
p = triangle(p1, p2, p3)
triangles.append(p)
'''=========================== '''
p4 = point3d(5, -100, 10)
ground1 = point3d(-1000, -10, 0)
ground2 = point3d(1000, -100, 1000)
ground3 = point3d(1000, -100, 0)
'''===== second triangle ========'''
t2p1 = point3d(-100, -100, 30)
t2p2 = point3d(200, -100, 30)
t2p3 = point3d(0, 100, 30)
t2 = triangle(t2p1, t2p2, t2p3)
#triangles.append(t2)
'''=====                 ======='''
p = triangle(p1, p2, p3)
t = triangle(p1, p4, p3)
ground = triangle(ground1, ground2, ground3)
p.plane.v1.dump()
p.plane.v2.dump()
ray.dump()
hit = p.plane.intersect(ray)
hit.dump()
l = light(point3d(10, 10, 1), 10)
#triangles.append(p)
#triangles.append(t)
#triangles.append(ground)
'''/testing'''

def draw():
	global triangles
	'''for all points on the screen'''
	for x in range(-1*xres/2, xres/2):
		print x
		for y in range(-1*yres/2, yres/2):
			'''find all the intersections on the triangles'''
			screen = point3d(x, y, 0)
			ray = vector3d(camera, screen)
			for t in triangles:
				p = t.plane.intersect(ray)
				t1 = triangle(t.p1, t.p2, p)
				t2 = triangle(t.p1, t.p3, p)
				t3 = triangle(t.p2, t.p3, p)
				if (t.area +5>= t1.area + t2.area + t3.area):
					'''find the surface normal and use it to calculate angle with light'''
					normalvector = vector3d(p, t.plane.normal)
					normalvector.normalize()
					lightvector = vector3d(p, l.pos)
					lightvector.normalize()
					'''we want to find the intersections of the light ray onto the triangle to check for shadows'''
					for lightt in triangles:
					   	if (lightt != t):	
							lightp = t.plane.intersect(lightvector)
							lightt1 = triangle(lightt.p1, lightt.p2, lightp)
							lightt2 = triangle(lightt.p1, lightt.p3, lightp)
							lightt3 = triangle(lightt.p2, lightt.p3, lightp)
							if (lightt.area +5 >= lightt1.area + lightt2.area + lightt3.area):
								break		
						angle = (normalvector.dx*lightvector.dx + normalvector.dy*lightvector.dy + normalvector.dz*lightvector.dz)
						angle *= -1
						shade = l.intensity*angle
						drawPixel(x, y, (0, 0, 0)) 
						pygame.draw.line(win, (shade*25, shade*25, shade*25), (x+xres/2, y+yres/2), (x+xres/2, y+yres/2))
						
			

	pygame.display.update()
	pygame.display.flip()

while True:

	
	win.fill((255, 255, 255))

	for e in pygame.event.get():
		event(e)

	draw()
		
	
	l.pos.x += 10
