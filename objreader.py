import geometry, math

def readobj(filename):
		f = open(filename, "r")

		vertexList = []
		faces = []

		lines = f.readlines()

		for l in lines:
			thisline = l.split(' ')
			command = thisline[0]
			if command == 'v':
				x = float(thisline[1])
				y = float(thisline[2])
				z = float(thisline[3])
				print x, y, z
				vertexList.append(geometry.point3d(x, y, z))
			if command == 'f':
				i1 = int(thisline[1])
				i2 = int(thisline[2])
				i3 = int(thisline[3])
				print len(vertexList), i1, i2, i3
				faces.append(geometry.triangle(vertexList[i1-1], vertexList[i2-1], vertexList[i3-1]))

		f.close()
		return faces
