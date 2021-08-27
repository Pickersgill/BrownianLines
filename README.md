# Jack's Desktop Background 2.0

I finally updated Ubuntu and decided to use the oppurtunity to make a new wallaper.

# What is this?
This simple tool let you generate images made up of many lines. Each line traces the path of a single 
"particle" moving through space. You can change the particle sizes, colours, speeds, masses and some other
stuff in order to change the nature of the generated images.

# What is Brownian Motion?

Brownian Motion is a way of describing random movements of a particle through a 2d plain. I think it was
created to help simulate molecules moving in liquids but I'm not really sure. Check out [the Wikipedia
article](https://en.wikipedia.org/wiki/Brownian_motion) for a deep dive.

# How does it work?

There are lots of particles being simulated in the space but only some of them are being traced, these are 
the "heroes". The other particles collide with the heroes and make them bounce around randomly to generate 
nice twisty lines. After a certain amount of time the simulation stops and the paths the heroes took are used
to draw the lines.

# How do you use it?

To change the parameters of the simulation you can mess around with the style.py file. Most of the variables
are pretty eponymous. The initial positions, speeds and directions of all particles are generated randomly
based on the seed given, or a random seed if none is provided.


