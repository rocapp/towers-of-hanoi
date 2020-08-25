# coding: utf-8
from toh import *
if __name__=='__main__':
    a = 2; b = 5; n = 10000
    t0 = time.time()
    zrng = ZigguratRNG(a=a,b=b,k=128,mu=0,std=1)
    niters, samples = zrng.nsamples(n=n)
    print('time=', '{:.2f}'.format(time.time()-t0),
          ': ziggurat:', 'niters=', niters,
          'mean=', np.mean(samples),
          'std=', np.std(samples))
    t0 = time.time()
    iters, samps = naive_sample(a=a,b=b,n=n)
    print('time=', '{:.2f}'.format(time.time()-t0),
          ':   naive:', 'niters=', iters,
          'mean=', np.mean(samps),
          'std=', np.std(samps))
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(nrows=2)
    axs[0].plot(samples, 'k.')
    axs[1].plot(samps, 'b.')
    plt.show()
