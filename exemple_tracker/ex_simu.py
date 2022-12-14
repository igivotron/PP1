import numpy as np

def force_frot_fun(v,k):
    f_fr = k*v
    return f_fr

def main(x, v, ligma, k, dt, m,decal):
    v_t = [v]
    x_t = [x]
    t = 0
    loop = True
    while loop:
        x += v*dt
        x_t.append(x)
        f_fr = force_frot_fun(v,k)
        v -= (f_fr/m)*dt
        v_t.append(v)
        if v < ligma:
            loop = False
        t+=1
    t =t*dt
    tt = np.arange(decal,decal+t+dt,dt)
    print(tt)
    return v_t, x_t, tt
