import math, numpy

def getLength(vector):
	sum = 0
	for i in vector:
		sum += i*i

	return math.sqrt(sum)

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
	def vequals(self, a, b):
		if a[0] == b[0] and a[1] == b[1] and a[2] == c.z:
			return True
		return False

	def intersect(self, ray):
		a = ([self.v1.dx, self.v2.dx, -1*ray.dx]
			,[self.v1.dy, self.v2.dy, -1*ray.dy]
			,[self.v1.dz, self.v2.dz, -1*ray.dz])
#	print a
		b = ([self.p.x, self.p.y, self.p.z])
		'''tried to remove singular matrix stuff
		if (self.vequals(a[0], a[1]) or self.vequals(a[1], a[2]) or self.vequals(a[0], a[2])):
			return point3d(0, 0, -100000)'''
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


