import numpy
import pygame
import math, time, sys
import geometry
import objreader

xres = 500
yres = 500

pygame.init()
win = pygame.display.set_mode((xres, yres), pygame.SRCALPHA)

def drawPixel(x, y, color):
#	pygame.gfxdraw.pixel(win, x, y, color)
		pygame.draw.line(win, color, (x+1, y), (x, y))

class light:
	def __init__(self, pos, intensity):
		self.pos = pos
		self.intensity = intensity

def event(e):
	if e.type == pygame.QUIT:
		sys.exit(0)

triangles = objreader.readobj("finger.obj")
camera = geometry.point3d(0, 0, -4)
l = light(geometry.point3d(5, 5, 5), 10)

def isIntersect(ray, t):
	p = t.plane.intersect(ray)
	''' we want to find the barycentric coordinates of all the points '''
	
	ab = [t.p1.x-t.p2.x,t.p1.y-t.p2.y,t.p1.z-t.p2.z]
	ac = [t.p1.x-t.p3.x,t.p1.y-t.p3.y,t.p1.z-t.p3.z]
	A = geometry.getLength(numpy.cross(ab, ac))
	pa = [p.x-t.p1.x,p.y-t.p1.y,p.z-t.p1.z]
	pb = [p.x-t.p2.x,p.y-t.p2.y,p.z-t.p2.z]
	pc = [p.x-t.p3.x,p.y-t.p3.y,p.z-t.p3.z]
	alpha = geometry.getLength(numpy.cross(pb, pc))
	beta = geometry.getLength(numpy.cross(pa, pc))
	gamma = geometry.getLength(numpy.cross(pa, pb))
	if (alpha + beta + gamma <= A):
		return p
	return 0

def draw():
	global triangles
	'''for all points on the screen'''
	for x in range(-1*xres/2, xres/2):
		print x
		for y in range(-1*yres/2, yres/2):
			'''find all the intersections on the triangles'''
			screen = geometry.point3d(x/5., y/5., -3)
			ray = geometry.vector3d(camera, screen)
			for t in triangles:
				p = isIntersect(ray, t)
				if (p):
					'''find the surface normal and use it to calculate angle with light'''
					normalvector = geometry.vector3d(p, t.plane.normal)
					normalvector.normalize()
					lightvector = geometry.vector3d(p, l.pos)
					lightvector.normalize()
					'''we want to find the intersections of the light ray onto the geometry.triangle to check for shadows'''
					'''	for lightt in triangles:
					   	if (lightt != t):	
							if (isIntersect(ray, lightt)):
								break'''
					angle = (normalvector.dx*lightvector.dx + normalvector.dy*lightvector.dy + normalvector.dz*lightvector.dz)
					shade = l.intensity*angle
#	drawPixel(x, y, (0, 0, 0)) 
					pygame.draw.line(win, (max(0,shade*25),max(0, shade*25),max(0, shade*25)), (x+xres/2, y+yres/2), (x+xres/2, y+yres/2))
						
			

	pygame.display.update()
	pygame.display.flip()

while True:

	
	win.fill((255, 255, 255))

	for e in pygame.event.get():
		event(e)

	draw()
		
	
	l.pos.x += 10
