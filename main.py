# Solar system
# Python script created by Daniel Sanaee
# 2021-01.16

import matplotlib.pyplot as plt
import numpy as np
import math

def main():

    class solarsystem_object():
        """The solarsystem"""
        def __init__(self):
            self._size = 0
            self.time = 0

        def add_sun(self):
            """Add sun to solarsystem"""
            self._size += 1
            self.sun = _round_object()
            self.sun.name = "sun"

        def add_mercury(self):
            """Add mercury to solarsystem"""
            self._size += 1
            self.mercury = _round_object()
            self.mercury.name = "mercury"

        def add_venus(self):
            """Add venus to solarsystem"""
            self._size += 1
            self.venus = _round_object()
            self.venus.name = "venus"

        def add_earth(self):
            """Add earth to solarsystem"""
            self._size += 1
            self.earth = _round_object()
            self.earth.name = "earth"

        def add_mars(self):
            """Add mars to solarsystem"""
            self._size += 1
            self.mars = _round_object()
            self.mars.name = "mars"

        def add_jupiter(self):
            """Add jupiter to solarsystem"""
            self._size += 1
            self.jupiter = _round_object()
            self.jupiter.name = "jupiter"

        def add_saturn(self):
            """Add saturn to solarsystem"""
            self._size += 1
            self.saturn = _round_object()
            self.saturn.name = "saturn"

        def add_uranus(self):
            """Add uranus to solarsystem"""
            self._size += 1
            self.uranus = _round_object()
            self.uranus.name = "uranus"

        def add_neptune(self):
            """Add saturn to solarsystem"""
            self._size += 1
            self.neptune = _round_object()
            self.neptune.name = "neptune"

        def add_asteroid(self):
            """Add asteroid to solarsystem"""
            self._size += 1
            self.asteroid = _round_object()
            self.asteroid.name = "asteroid"

        def get_size(self):
            return self._size

        def healthy(self):
            """Unit testing"""
            assert self._size >= 0
            #Assert mass and radius > 0

    class _round_object(solarsystem_object):
        """Create a round object used as planets, stars and asteroids"""
        def __init__(self):

            self.mass = None
            self.radius = None
            self.name = "None"
            self.colour = "None"

            self.xposition = 0
            self.yposition = 0
            self.xspeed = 0
            self.yspeed = 0
            self.xacceleration = 0
            self.yacceleration = 0

            self.xposition_list = []
            self.yposition_list = []
            self.xspeed_list = []
            self.yspeed_list = []
            self.xacceleration_list = []
            self.yacceleration_list = []

            self.total_energy_list = []
            self.potential_energy_list = []
            self.kinetic_energy_list = []


    def create_solarsystem():
        """Create solarsystem object with planets"""

        solarsystem = solarsystem_object()

        # for bodyindex in range(len(solarsystem_dict)):
            # print("Index nummer", bodyindex)
            # solarsystem.add_body(bodyindex)

        for body in solarsystem_dict:
            if body == "sun":
                solarsystem.add_sun()
            elif body == "mercury":
                solarsystem.add_mercury()
            elif body == "venus":
                solarsystem.add_venus()
            elif body == "earth":
                solarsystem.add_earth()
            elif body == "mars":
                solarsystem.add_mars()
            elif body == "jupiter":
                solarsystem.add_jupiter()
            elif body == "saturn":
                solarsystem.add_saturn()
            elif body == "uranus":
                solarsystem.add_uranus()
            elif body == "neptune":
                solarsystem.add_neptune()
            elif body == "asteroid":
                solarsystem.add_asteroid()

            getattr(solarsystem, str(body)).mass = solarsystem_dict[body][0] # --> solarsystem.sun.mass = 333000
            getattr(solarsystem, str(body)).radius = solarsystem_dict[body][1]
            getattr(solarsystem, str(body)).xposition = solarsystem_dict[body][2]
            getattr(solarsystem, str(body)).yposition = solarsystem_dict[body][3]
            getattr(solarsystem, str(body)).xspeed = solarsystem_dict[body][4]
            getattr(solarsystem, str(body)).yspeed = solarsystem_dict[body][5]
            getattr(solarsystem, str(body)).colour = solarsystem_dict[body][6]
            getattr(solarsystem, str(body)).name = body

        return solarsystem

    def simulate(solarsystem, integrator):
        """Simulate solarsystem and return dictionary with visited planet trajectory coordinates and dictionary with past planet velocities"""
        global dt
        global steps
        global years
        global hour_step
        hour_step = 1
        years = 100
        dt = hour_step/(365*24)
        steps = int(years/dt)

        for body in solarsystem_dict:
            getattr(solarsystem, str(body)).xposition_list.append(getattr(solarsystem, str(body)).xposition)
            getattr(solarsystem, str(body)).yposition_list.append(getattr(solarsystem, str(body)).yposition)
            getattr(solarsystem, str(body)).xspeed_list.append(getattr(solarsystem, str(body)).xspeed)
            getattr(solarsystem, str(body)).yspeed_list.append(getattr(solarsystem, str(body)).yspeed)
            getattr(solarsystem, str(body)).xacceleration_list.append(getattr(solarsystem, str(body)).xacceleration)
            getattr(solarsystem, str(body)).yacceleration_list.append(getattr(solarsystem, str(body)).yacceleration)

        for i in range(steps):
            solarsystem.time += dt
            for body in solarsystem_dict:
                update(getattr(solarsystem, str(body)), integrator)
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

    def draw(inner = True):
        """Plot all planets' trajectory"""

        for body in solarsystem_dict:

            # Change axis to million miles
            # getattr(solarsystem, str(body)).yposition_list = [x * 92.955807 for x in getattr(solarsystem, str(body)).yposition_list]
            # getattr(solarsystem, str(body)).yposition_list = [x * 92.955807 for x in getattr(solarsystem, str(body)).yposition_list]

            ax.plot(getattr(solarsystem, str(body)).xposition_list,getattr(solarsystem, str(body)).yposition_list, color=getattr(solarsystem, str(body)).colour, linestyle='solid', markersize = 2)
            ax.plot(getattr(solarsystem, str(body)).xposition_list[-1],getattr(solarsystem, str(body)).yposition_list[-1], color=getattr(solarsystem, str(body)).colour, marker = "o", markersize = 0.08*getattr(solarsystem, str("sun")).radius + 0.9*math.log(getattr(solarsystem, str(body)).radius/getattr(solarsystem, str("sun")).radius))

            # Add tetboxes for objects
            if body == "asteroid":
                ax.text(getattr(solarsystem, str(body)).xposition_list[-1],getattr(solarsystem, str(body)).yposition_list[-1]+0.1, getattr(solarsystem, str(body)).name, color=getattr(solarsystem, str(body)).colour, fontsize = 15, zorder = 2)
            else:
                if inner == True:
                    arc_percent = int(0.8*len(getattr(solarsystem, str(body)).xposition_list))
                    ax.text(getattr(solarsystem, str(body)).xposition_list[-1],getattr(solarsystem, str(body)).yposition_list[-1]+0.1, getattr(solarsystem, str(body)).name, color=getattr(solarsystem, str(body)).colour, fontsize = 15, zorder = 2)

                    # if body == "jupiter":
                    #     ax.text(getattr(solarsystem, str(body)).xposition_list[arc_percent],getattr(solarsystem, str(body)).yposition_list[arc_percent]+0.5, getattr(solarsystem, str(body)).name, color=getattr(solarsystem, str(body)).colour, fontsize = 15, zorder = 2)
                    # elif body == "mercury":
                    #     ax.text(getattr(solarsystem, str(body)).xposition_list[arc_percent],getattr(solarsystem, str(body)).yposition_list[arc_percent]+0.5, getattr(solarsystem, str(body)).name, color=getattr(solarsystem, str(body)).colour, fontsize = 15, zorder = 2)
                    # else:
                    #     ax.text(getattr(solarsystem, str(body)).xposition_list[-1],getattr(solarsystem, str(body)).yposition_list[-1]+0.1, getattr(solarsystem, str(body)).name, color=getattr(solarsystem, str(body)).colour, fontsize = 15, zorder = 2)

                elif inner == False:
                    ax.text(getattr(solarsystem, str(body)).xposition_list[4000],getattr(solarsystem, str(body)).yposition_list[4000]+0.2, getattr(solarsystem, str(body)).name, color=getattr(solarsystem, str(body)).colour, fontsize = 15, zorder = 2)


        plt.show(block=True)

    def animate(x_list, y_list, colour):
        """Continually draw animation"""
        plt.plot(x_list,y_list, color=colour, linestyle='solid', markersize = 2)
        plt.show(block=False)
        plt.pause(0.00000000000000000001)

    def update(obj, integrator):
        """Update position"""

        x_force, y_force = forcefunction(obj)

        if integrator == "Verlet":
            _update_verlet(obj,[x_force,y_force])

        elif integrator == "EC":
            _update_EC(obj,[x_force,y_force])

    def _update_EC(obj, forcevector):
        """Update position with euler cromer integration"""

        obj.xacceleration = forcevector[0] / obj.mass
        obj.yacceleration = forcevector[1] / obj.mass

        obj.xspeed += obj.xacceleration*dt
        obj.yspeed += obj.yacceleration*dt

        obj.xposition += obj.xspeed * dt
        obj.yposition += obj.yspeed * dt

    def _update_verlet(obj, forcevector):
        """Update position with Verlet integration"""

        obj.xacceleration = forcevector[0] / obj.mass
        obj.yacceleration = forcevector[1] / obj.mass

        #Integrator

        obj.xposition = obj.xposition + obj.xspeed * dt + 0.5*obj.xacceleration*dt*dt
        obj.yposition = obj.yposition + obj.yspeed * dt + 0.5*obj.yacceleration*dt*dt

        new_x_force, new_y_force = forcefunction(obj)

        new_obj_x_acceleration = new_x_force/obj.mass
        new_obj_y_acceleration = new_y_force/obj.mass

        obj.xspeed += 0.5*(new_obj_x_acceleration+obj.xacceleration)*dt
        obj.yspeed += 0.5*(new_obj_y_acceleration+obj.yacceleration)*dt

    def forcefunction(obj):
        """Calculate force on object and return force in x and y direction"""
        x_force = 0
        y_force = 0
        for body in solarsystem_dict:
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

    def energy_results():
        """Generate energy result figures"""
        global hour_step
        global hour_list
        global solarsystem
        energy_canvas()
        hour_list = [1,48,96]

        for hour_step in hour_list:
            for integrator in ["EC","Verlet"]:

                if integrator == "EC":
                    continue
                    integrator_string = "Euler-Cromer"
                else:
                    integrator_string = "Verlet"

                solarsystem = create_solarsystem()
                simulate(solarsystem, str(integrator))

                # solarsystem_canvas_setup(integrator_string)
                # asteroid_earth()
                # draw()

                for body in solarsystem_dict:
                    assert len(getattr(solarsystem, str(body)).total_energy_list) == len(getattr(solarsystem, str(body)).potential_energy_list) == len(getattr(solarsystem, str(body)).kinetic_energy_list) == 0

                    if body != "earth":
                        continue

                    energy_lists(getattr(solarsystem, str(body)))

                    #Generate error lists
                    start_energy_total = getattr(solarsystem, str(body)).total_energy_list[0]
                    getattr(solarsystem, str(body)).total_energy_list = [abs((x-start_energy_total)/start_energy_total) for x in getattr(solarsystem, str(body)).total_energy_list]
                    earth_ax.set_title("Earths relative total energy error using Verlet integration." + "\n" + "Different time steps are displayed", fontsize=30)


                    plot_energy_EC_vs_Verlet(getattr(solarsystem, str(body)), "total", integrator)
                    # plot_energy_EC_vs_Verlet(getattr(solarsystem, str(body)), "potential", integrator)
                    # plot_energy_EC_vs_Verlet(getattr(solarsystem, str(body)), "kinetic", integrator)
                    getattr(solarsystem, str(body)).total_energy_list = []
                    getattr(solarsystem, str(body)).potential_energy_list = []
                    getattr(solarsystem, str(body)).kinetic_energy_list = []


        plt.show()

    def plot_energy_EC_vs_Verlet(obj, type, integrator):
        """Plot the graphs"""

        iterations = np.arange(0, years + 0.1*hour_step/(24*365), hour_step/(24*365)) # Years on x-axis
        # obj.potential_energy_list = [x*1000 for x in obj.potential_energy_list]
        if integrator == "EC":
            if hour_step == hour_list[0]:
                if type == "total":
                    earth_ax.plot(iterations,obj.total_energy_list,color = "#f0b27a", linestyle = "solid", label = "dt = " + str(hour_list[0]) + " hour")
                elif type == "potential":
                    earth_ax.plot(iterations,obj.potential_energy_list,color = "#3498db", linestyle = "solid", label = "dt = " + str(hour_list[0]) + " hour")
                elif type == "kinetic":
                    earth_ax.plot(iterations,obj.kinetic_energy_list,color = "Green", linestyle = "solid", label = "dt = " + str(hour_list[0]) + " hour")

            elif hour_step == hour_list[1]:
                if type == "total":
                    earth_ax.plot(iterations,obj.total_energy_list,color = "#3498db", linestyle = "dashdot", label = "dt = " + str(hour_list[1]) + " hours")
                elif type == "potential":
                    earth_ax.plot(iterations,obj.potential_energy_list,color = "#3498db", linestyle = "dashdot", label = "dt = " + str(hour_list[1]) + " hours")
                elif type == "kinetic":
                    earth_ax.plot(iterations,obj.kinetic_energy_list,color = "Green", linestyle = "dashdot", label = "dt = " + str(hour_list[1]) + " hours")

            elif hour_step == hour_list[2]:
                if type == "total":
                    earth_ax.plot(iterations,obj.total_energy_list,color = "Green", linestyle = "dotted", label = "dt = " + str(hour_list[2]) + " hours")
                elif type == "potential":
                    earth_ax.plot(iterations,obj.potential_energy_list,color = "#3498db", linestyle = "dotted", label = "dt = " + str(hour_list[2]) + " hours")
                elif type == "kinetic":
                    earth_ax.plot(iterations,obj.kinetic_energy_list,color = "Green", linestyle = "dotted", label = "dt = " + str(hour_list[2]) + " hours")

        elif integrator == "Verlet":
            if hour_step == hour_list[0]:
                if type == "total":
                    earth_ax.plot(iterations,obj.total_energy_list,color = "#f0b27a", linestyle = "solid", label = "dt = " + str(hour_list[0]) + " hour")
                elif type == "potential":
                    earth_ax.plot(iterations,obj.potential_energy_list,color = "#3498db", linestyle = "solid", label = "dt = " + str(hour_list[0]) + " hour")
                elif type == "kinetic":
                    earth_ax.plot(iterations,obj.kinetic_energy_list,color = "Green", linestyle = "solid", label = "dt = " + str(hour_list[0]) + " hour")

            elif hour_step == hour_list[1]:
                if type == "total":
                    earth_ax.plot(iterations,obj.total_energy_list,color = "#3498db", linestyle = "dashdot", label = "dt = " + str(hour_list[1]) + " hours")
                elif type == "potential":
                    earth_ax.plot(iterations,obj.potential_energy_list,color = "#3498db", linestyle = "dashdot", label = "dt = " + str(hour_list[1]) + " hours")
                elif type == "kinetic":
                    earth_ax.plot(iterations,obj.kinetic_energy_list,color = "Green", linestyle = "dashdot", label = "dt = " + str(hour_list[1]) + " hours")

            elif hour_step == hour_list[2]:
                if type == "total":
                    earth_ax.plot(iterations,obj.total_energy_list,color = "Green", linestyle = "dotted", label = "dt = " + str(hour_list[2]) + " hours")
                elif type == "potential":
                    earth_ax.plot(iterations,obj.potential_energy_list,color = "#3498db", linestyle = "dotted", label = "dt = " + str(hour_list[2]) + " hours")
                elif type == "kinetic":
                    earth_ax.plot(iterations,obj.kinetic_energy_list,color = "Green", linestyle = "dotted", label = "dt = " + str(hour_list[2]) + " hours")
        earth_ax.legend(prop={'size': 20})

    def energy_lists(obj):
        """Fill all lists of total, potential and kinetic energy"""

        assert len(obj.xposition_list) == len(obj.yposition_list) == len(obj.xspeed_list) == len(obj.yspeed_list)
        for i in range(len(obj.xposition_list)):
            x_position = obj.xposition_list[i]
            y_position = obj.yposition_list[i]
            x_speed = obj.xspeed_list[i]
            y_speed = obj.yspeed_list[i]

            kinetic_energy = 0.5*obj.mass*(x_speed**2+y_speed**2)
            # Calculating potential energy
            potential_energy = 0
            for M in solarsystem_dict:
                if obj.name == M: #Do not want energy from itself
                    continue
                r = [x_position - getattr(solarsystem, str(M)).xposition_list[i], y_position - getattr(solarsystem, str(M)).yposition_list[i]] #Unit vector from body to M
                distance = (r[0]**2+r[1]**2)**0.5
                potential_energy += -1*G*getattr(solarsystem,str(M)).mass*obj.mass / distance

            total_energy = potential_energy + kinetic_energy

            obj.total_energy_list.append(total_energy)
            obj.potential_energy_list.append(potential_energy)
            obj.kinetic_energy_list.append(kinetic_energy)
        return

    def energy_canvas(type="earth"):
        """Setup energy canvas"""
        if type == "earth":
            global earth_fig, earth_ax
            earth_fig, earth_ax = plt.subplots()
            earth_ax.set_facecolor("#17202a")
            earth_ax.tick_params(axis='x', labelsize=20)
            earth_ax.tick_params(axis='y', labelsize=20)
            earth_ax.set_xlabel('Time [Earth-years]', fontsize=28)
            unitstr = r'$Earthmass \times \frac{{AU}^2}{{Earthyear}^2}}^2}$'
            # earth_ax.set_ylabel('Energy ['+unitstr+']', fontsize=28)
            earth_ax.set_ylabel('Relative total energy error', fontsize=28)

            earth_ax.set(ylim=(-80, 80))

            # Set title
            earth_ax.set_title("Total energy using Verlet integration." + "\n" + "Different time steps are displayed", fontsize=30)
            earth_ax.set_title("Total energy using Euler-Cromer integration." + "\n" + "Different time steps are displayed", fontsize=30)


        elif type == "solarsystem":
            global system_fig, system_ax
            system_fig, system_ax = plt.subplots()
            system_ax.set_facecolor("#17202a")

    def asteroid_results():
        """Plotting the results"""
        asteroid_canvas()
        distance_list, acceleration_list, earth_displacement = asteroid_earth()
        iterations = np.arange(0, years*24*365+0.3*hour_step, hour_step)
        iterations = np.arange(0, years + 0.1*hour_step/(24*365), hour_step/(24*365))

        ast_ax.plot(iterations, distance_list, color = "#5D6D7E")
        ast2_ax.plot(iterations, earth_displacement, color = "blue")
        plt.show()

    def asteroid_canvas():
        "Setup canvas"
        global ast_fig, ast_ax, ast2_ax

        ast_fig, ast_ax = plt.subplots()
        ast_ax.set_facecolor("#17202a")
        ast_ax.tick_params(axis='x', labelsize=20)
        ast_ax.tick_params(axis='y', labelsize=20)
        ast_ax.set_xlabel('Time [Hours]', fontsize=28)
        ast_ax.set_ylabel("Asteroid distance to earth [AU]", fontsize=28)
        ast_ax.tick_params(axis='y', labelcolor="#5D6D7E")


        ast2_ax = ast_ax.twinx()
        ast2_ax.tick_params(axis='x', labelsize=20)
        ast2_ax.tick_params(axis='y', labelsize=20, color=solarsystem.earth.colour)
        # ast2_ax.set_ylabel('Acceleration on earth ['+ r'$\frac{AU}{{Earthyear}^2}$' +"]", fontsize=28)
        ast2_ax.set_ylabel('Earths relative displacement', fontsize=28)

        ast2_ax.tick_params(axis='y', labelcolor= "blue")

        # Set title
        ast_ax.set_title("Near miss for Earth and Asteroid with mass "+str(solarsystem.asteroid.mass) + " times that of Earths \n" + "Time step = 10 minutes", fontsize=30)
        ast_ax.set_title("Near miss for Earth and Asteroid with mass "+str(solarsystem.asteroid.mass) + " times that of Earths \n" + "Time step = "+ str(hour_step) + " hour", fontsize=30)

    def asteroid_earth():

        distance_list = []
        acceleration_list = [] #Acceleration on asteroid
        earth_displacement = [] #Earth displacement because of asteroid

        biggest_acceleration = 0
        time_of_biggest_acceleration = None

        shortest_distance = 10**100 # Random big number
        time_of_shortest_distance = None

        assert len(solarsystem.asteroid.xposition_list) == len(solarsystem.asteroid.yposition_list) == len(solarsystem.earth.xposition_list) == len(solarsystem.earth.yposition_list)
        for i in range(len(getattr(solarsystem, str(solarsystem.asteroid.name)).xposition_list)):

            #Distance
            r = np.sqrt((solarsystem.asteroid.xposition_list[i] - solarsystem.earth.xposition_list[i])**2 + (solarsystem.asteroid.yposition_list[i] - solarsystem.earth.yposition_list[i])**2)
            distance_list.append(r)

            #Acceleration
            acceleration = np.sqrt(solarsystem.earth.xacceleration_list[i]**2 + solarsystem.earth.xacceleration_list[i]**2)
            acceleration_list.append(acceleration)

            #Earth's deviation
            expected_r = [np.cos(2*math.pi*i*dt),np.sin(2*math.pi*i*dt)]
            actual_r = [solarsystem.earth.xposition_list[i], solarsystem.earth.yposition_list[i]]
            displacement = np.sqrt((expected_r[0]-actual_r[0])**2 +(expected_r[1]-actual_r[1])**2)
            earth_displacement.append(displacement/np.sqrt(expected_r[0]**2 + expected_r[1]**2))

            if r < shortest_distance:
                shortest_distance = r
                time_of_shortest_distance = (i+1)*dt
            if acceleration > biggest_acceleration:
                biggest_acceleration = acceleration
                time_of_biggest_acceleration = (i+1)*dt

        print("Shortest distance is", shortest_distance, "at time", time_of_shortest_distance)
        print("Biggest acceleration is", biggest_acceleration, "at time", time_of_biggest_acceleration)
        return distance_list, acceleration_list, earth_displacement

    def solarsystem_canvas_setup(integrator_string, length="AU", size="large"):
        """Setting up canvas"""
        global fig
        global ax
        fig, ax = plt.subplots()


        ax.set_facecolor("#17202a")
        if hour_step == 1:
            ax.set_title("Solar system simulation with " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(years)+ " earth-years. Time step = "+ str(hour_step) + " hour", fontsize=30)
        else:
            # ax.set_title("Asteroid with mass of Uranus using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(years)+ " earth-years. Time step = 10 minutes", fontsize=30)
            # ax.set_title("Asteroid with mass of Jupiter using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(years)+ " earth-years. Time step = 10 minutes", fontsize=30)
            # ax.set_title("Asteroid with one tenth of the mass of the sun. Simulated using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(years)+ " earth-years. Time step = 10 minutes", fontsize=30)
            ax.set_title("Asteroid with the mass of the sun. Simulated using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(years)+ " earth-years. Time step = 10 minutes", fontsize=30)


            # ax.set_title("Asteroid near miss with " + str(integrator_string) + " integration." + "\n" + "Time step = 10 minutes", fontsize=30)
            # ax.set_title("Asteroid near miss with " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(years)+ " earth-years. Time step = 10 minutes", fontsize=30)



        ax.tick_params(axis='x', labelsize=20)
        ax.tick_params(axis='y', labelsize=20)

        if length == "miles":
            ax.set_xlabel('Distance [Million Miles]', fontsize=28)
            ax.set_ylabel('Distance [Million Miles]', fontsize=28)
        else:
            ax.set_xlabel('Distance [AU]', fontsize=28)
            ax.set_ylabel('Distance [AU]', fontsize=28)

        if size == "small":
            ax.set(xlim=(0.66, 0.68), ylim=(-0.76, -0.74))
        else:
            ax.set(xlim=(-32, 32), ylim=(-32, 32))



    #[mass (eathmasses), radius (eathradiuses), x-position (Astronomical units), y-position (Astronomical units), x-speed (AU per earth-year), y-speed (AU per earth-year), colour]
    global solarsystem_dict
    solarsystem_dict = {
    "sun": [333000, 109, 0, 0, 0, 0, "#f7dc6f"],
    "mercury": [0.055, 0.3829, 0.387, 0, 0, (47.362/29.78)*(2*math.pi), "#b2babb"],
    "venus": [0.815, 0.95, 0.72, 0, 0, (35.02/29.78)*(2*math.pi), "#f9e79f"],
    "earth": [1, 1, 1, 0, 0, 2*math.pi, "#3498db"],
    "mars": [0.107, 0.53, 1.52, 0, 0, (24.097/29.78)*(2*math.pi), "red"],
    "jupiter": [318, 10.97, 5.2, 0, 0, (13.07/29.78)*(2*math.pi), "#f0b27a"],
    "saturn": [95.159, 58232/6371, 9.58, 0, 0, (9.68/29.78)*(2*math.pi), "#af601a"],
    "uranus": [14.536, 4, 19.21, 0, 0, (6.8/29.78)*(2*math.pi), "#85c1e9"],
    "neptune": [17.147, 24622/6371, 30.07, 0, 0, (5.43/29.78)*(2*math.pi), "#1f618d"],
    "asteroid": [0.01, 1, 0.74854, -12.004, 0, 4*math.pi, "#b2babb"] #Near earth
    }

    integrator = "EC"
    integrator_string = "Euler-Cromer"
    integrator = "Verlet"
    integrator_string = "Verlet"

    solarsystem = create_solarsystem()
    simulate(solarsystem, str(integrator))
    solarsystem_canvas_setup(integrator_string)
    draw()
    asteroid_results()
    # energy_results()

if __name__ == "__main__": main()




# TODO

# IDEAS
