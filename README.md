# raytracer
Building a ray tracer in python using pygame.  Reads obj files and renders them

## Elements

1. File reading

   The ray tracer will need to get its information from somewhere. It will read .obj files and store all of the triangles in a surface object. 
  
2. Ray Tracing

   The ray tracing will be done on an arbitrary set of objects by sending out rays from a camera, through the screen and into the scene. It will then look for all available light sources to determine the intensity of the light on that surface.

3. API
 
   After the ray tracer is completed with all desired features, it will be part of a graphics library that allows for the manipulation and display of 3D objects.
