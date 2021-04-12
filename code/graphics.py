
def solarsystem_canvas_setup(solarsystem, integrator_string, length="AU", size="large"):
    """Setting up canvas"""
    global fig
    global ax
    fig, ax = plt.subplots()


    ax.set_facecolor("#17202a")
    if solarsystem.hour_step == 1:
        ax.set_title("Solar system simulation with " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(solarsystem.years)+ " earth-years. Time step = "+ str(solarsystem.hour_step) + " hour", fontsize=30)
    else:
        # ax.set_title("Asteroid with mass of Uranus using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(solarsystem.years)+ " earth-years. Time step = 10 minutes", fontsize=30)
        # ax.set_title("Asteroid with mass of Jupiter using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(solarsystem.years)+ " earth-years. Time step = 10 minutes", fontsize=30)
        # ax.set_title("Asteroid with one tenth of the mass of the sun. Simulated using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(solarsystem.years)+ " earth-years. Time step = 10 minutes", fontsize=30)
        ax.set_title("Asteroid with the mass of the sun. Simulated using " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(solarsystem.years)+ " earth-years. Time step = 10 minutes", fontsize=30)


        # ax.set_title("Asteroid near miss with " + str(integrator_string) + " integration." + "\n" + "Time step = 10 minutes", fontsize=30)
        # ax.set_title("Asteroid near miss with " + str(integrator_string) + " integration." + "\n" + "Simulation time = " + str(solarsystem.years)+ " earth-years. Time step = 10 minutes", fontsize=30)



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

def draw(solarsystem, inner = True):
    """Plot all planets' trajectory"""
    for body in solarsystem.data:

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

if __name__ == "graphics":
    import matplotlib.pyplot as plt
    import math
