

def simulate(solarsystem, integrator):

    integrator = "EC"
    integrator_string = "Euler-Cromer"
    integrator = "Verlet"
    integrator_string = "Verlet"


    """Simulate solarsystem and return dictionary with visited planet trajectory coordinates and dictionary with past planet velocities"""
    solarsystem.hour_step = 10
    solarsystem.years = 1
    solarsystem.dt = solarsystem.hour_step/(365*24)
    solarsystem.steps = int(solarsystem.years/solarsystem.dt)

    for body in solarsystem.data:
        getattr(solarsystem, str(body)).xposition_list.append(getattr(solarsystem, str(body)).xposition)
        getattr(solarsystem, str(body)).yposition_list.append(getattr(solarsystem, str(body)).yposition)
        getattr(solarsystem, str(body)).xspeed_list.append(getattr(solarsystem, str(body)).xspeed)
        getattr(solarsystem, str(body)).yspeed_list.append(getattr(solarsystem, str(body)).yspeed)
        getattr(solarsystem, str(body)).xacceleration_list.append(getattr(solarsystem, str(body)).xacceleration)
        getattr(solarsystem, str(body)).yacceleration_list.append(getattr(solarsystem, str(body)).yacceleration)

    for i in range(solarsystem.steps):
        solarsystem.time += solarsystem.dt
        for body in solarsystem.data:
            update(getattr(solarsystem, str(body)), solarsystem, integrator)
            getattr(solarsystem, str(body)).xposition_list.append(getattr(solarsystem, str(body)).xposition)
            getattr(solarsystem, str(body)).yposition_list.append(getattr(solarsystem, str(body)).yposition)
            getattr(solarsystem, str(body)).xspeed_list.append(getattr(solarsystem, str(body)).xspeed)
            getattr(solarsystem, str(body)).yspeed_list.append(getattr(solarsystem, str(body)).yspeed)
            getattr(solarsystem, str(body)).xacceleration_list.append(getattr(solarsystem, str(body)).xacceleration)
            getattr(solarsystem, str(body)).yacceleration_list.append(getattr(solarsystem, str(body)).yacceleration)


            ### REMOVE LATER ###
            # if i == steps/2 and body == "earth":
            #     print(body, "xposition is", solarsystem.earth.xposition)
            #     print(body, "yposition is", solarsystem.earth.yposition)
            #     print("asteroid xposition is", solarsystem.asteroid.xposition)
            #     print("asteroid yposition is", solarsystem.asteroid.yposition)
            #     return position_dict, velocity_dict

            ## ###
    return None

def update(obj, solarsystem, integrator):
    """Update position"""

    x_force, y_force = forcefunction(obj, solarsystem)

    if integrator == "Verlet":
        _update_verlet(obj, solarsystem, [x_force,y_force])

    elif integrator == "EC":
        _update_EC(obj, solarsystem, [x_force,y_force])

def _update_EC(obj, solarsystem, forcevector):
    """Update position with euler cromer integration"""

    obj.xacceleration = forcevector[0] / obj.mass
    obj.yacceleration = forcevector[1] / obj.mass

    obj.xspeed += obj.xacceleration*solarsystem.dt
    obj.yspeed += obj.yacceleration*solarsystem.dt

    obj.xposition += obj.xspeed * solarsystem.dt
    obj.yposition += obj.yspeed * solarsystem.dt

def _update_verlet(obj, solarsystem, forcevector):
    """Update position with Verlet integration"""

    obj.xacceleration = forcevector[0] / obj.mass
    obj.yacceleration = forcevector[1] / obj.mass

    #Integrator

    obj.xposition = obj.xposition + obj.xspeed * solarsystem.dt + 0.5*obj.xacceleration*solarsystem.dt*solarsystem.dt
    obj.yposition = obj.yposition + obj.yspeed * solarsystem.dt + 0.5*obj.yacceleration*solarsystem.dt*solarsystem.dt

    new_x_force, new_y_force = forcefunction(obj, solarsystem)

    new_obj_x_acceleration = new_x_force/obj.mass
    new_obj_y_acceleration = new_y_force/obj.mass

    obj.xspeed += 0.5*(new_obj_x_acceleration+obj.xacceleration)*solarsystem.dt
    obj.yspeed += 0.5*(new_obj_y_acceleration+obj.yacceleration)*solarsystem.dt

def forcefunction(obj, solarsystem):
    """Calculate force on object and return force in x and y direction"""
    x_force = 0
    y_force = 0
    for body in solarsystem.data:
        if body == obj.name: #Do not want force on itself
            continue

        # if body != "sun": #Only sun exerts force
        #     continue

        forcevector = _forcefunction(obj, getattr(solarsystem, str(body)))
        x_force += forcevector[0]
        y_force += forcevector[1]

    return x_force, y_force

def _forcefunction(obj1, obj2):
    """Calculate and return the mutual attracting force between object 1 and object 2 in list [F1, F2] where F1 is x-force and y-force in direction from obj1 to obj2 and F2 is in direction from obj2 to obj1"""
    global G
    G = 39.478 / (333000) # Unit: (astronomisk enhet kub) per (år kvadrat) per (jordens massa)
    r = [obj2.xposition - obj1.xposition, obj2.yposition- obj1.yposition] #Unit vector from obj1 to obj2
    distance_squared = r[0]**2+r[1]**2
    r_hat = [r[0]/(distance_squared**0.5), r[1]/(distance_squared**0.5)]
    force = G*obj1.mass*obj2.mass/distance_squared
    return [r_hat[0]*force,r_hat[1]*force]



if __name__ == "simulate": pass
