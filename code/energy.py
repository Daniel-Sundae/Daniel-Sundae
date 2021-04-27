
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

            for body in solarsystem.data:
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
        for M in solarsystem.data:
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
