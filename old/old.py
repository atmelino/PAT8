

    #dxdt[0] = vx;
    #dxdt[1] = vy;
    #dxdt[2] = vz;
    #dxdt[3] = muorc * x
    #dxdt[4] = muorc * y
    #dxdt[5] = muorc * z
    #dsq = x * x + y * y  # distance squared
    # print dsq
    # dr = math.sqrt(dsq)  # distance
    # print dr
    # force = GM if dsq > 1e-10 else 0.
    # force = GM
    # xdotdot = -force * x / dr
    # ydotdot = -force * y / dr
    # drdt = [xdot, ydot, xdotdot, ydotdot]
    # return drdt

