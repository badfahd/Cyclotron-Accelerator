import numpy as np
import vpython as vp

scene = vp.canvas(title="Cyclotron Accelerator with Extended Target", width=1600, height=900, resize=True)


d_container = vp.cylinder(
    pos=vp.vector(0, -0.22, 0),
    axis=vp.vector(0, 0.44, 0),
    radius=5.0,
    color=vp.vector(0.5, 0.5, 0.5),
    opacity=0.1,
)


dee = vp.cylinder(
    pos=vp.vector(0, -0.22, 0),
    axis=vp.vector(0, 0.44, 0),
    radius=4.0,
    color=vp.color.magenta,
)


gap_slit = vp.box(
    pos=vp.vector(0, 0, 0),
    size=vp.vector(0.2, 0.5, 9.0),
    color=vp.vector(0.05, 0.05, 0.05),
)

for x_pos in range(-3, 4, 2):
    for z_pos in range(-3, 4, 2):
        vp.arrow(
            pos=vp.vector(x_pos, 0.25, z_pos),
            axis=vp.vector(0, 0.6, 0),
            color=vp.color.cyan,
            shaftwidth=0.06,
            opacity=0.4,
        )


ac_wire = vp.cylinder(
    pos=vp.vector(0, 0, -5.0),
    axis=vp.vector(0, 0, -1.5),
    radius=0.08,
    color=vp.color.orange,
)

ac_generator = vp.cylinder(
    pos=vp.vector(0, 0, -6.8),
    axis=vp.vector(0, 0.3, 0),
    radius=0.5,
    color=vp.color.orange,
)


beamline = vp.cylinder(
    pos=vp.vector(2.8, 0.4, -2.8),
    axis=vp.vector(6.0, 0, -6.0),
    radius=0.25,
    color=vp.color.green,
    opacity=0.5
)

target = vp.sphere(
    pos=vp.vector(9.5, 0, -9.5),
    radius=0.5,
    color=vp.color.red
)


particle = vp.sphere(
    pos=vp.vector(0.0, 0.4, 0.0),
    radius=0.2,
    color=vp.color.yellow,
    make_trail=True,
    retain=8000,
)


q = 1.0
m = 1.0
B_vector = vp.vector(0, 5.0, 0)
dt = 0.005

vel = vp.vector(0.2, 0.0, 0.5)
E_dir = 1.0
in_gap_last = False
is_ejected = False

while True:
    vp.rate(200)
    
    if not is_ejected:
        
        E_field = vp.vector(0, 0, 0)
        in_gap = abs(particle.pos.x) < 0.2
        
        if in_gap and not in_gap_last:
            E_dir *= -1.0
            
        if in_gap:
            E_field = vp.vector(E_dir * 4.0, 0, 0)
            
        in_gap_last = in_gap

        magnetic_force = q * vp.cross(vel, B_vector)
        electric_force = q * E_field
        total_force = electric_force + magnetic_force
        
        vel += (total_force / m) * dt
        particle.pos += vel * dt
        
        
        if particle.pos.x >= 2.5 and particle.pos.z <= -2.5:
            is_ejected = True
            vel = vp.vector(6.0, 0.0, -6.0) 
            B_vector = vp.vector(0, 0, 0)
            
    else:
        
        particle.pos += vel * dt
        
        
        if vp.mag(particle.pos - target.pos) < 0.6:
            particle.pos = vp.vector(0.0, 0.4, 0.0)
            vel = vp.vector(0.2, 0.0, 0.5)
            B_vector = vp.vector(0, 5.0, 0)
            E_dir = 1.0
            is_ejected = False
            particle.clear_trail()