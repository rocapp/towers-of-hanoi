# coding: utf-8
import numpy as np
from random import choice
import time

def generate_normalized_vector(a=0,b=1,n=10):
    xv = list(range(n))
    xmin, xmax = min(xv), max(xv)
    return [(b-a)*(x-xmin)/(xmax-xmin)+a for x in xv]
    
def pdf(x,mu=0,std=1): ## x --> prob(x)
    # return (1.0/np.sqrt(2*np.pi*std**2)) * np.exp(-0.5*(x-mu)**2/std**2)
    return np.exp(-0.5*((x-mu)/std)**2)

def qf(p,mu=0,std=1): ## prob(x) --> x
    return np.log(p/(1-p))*np.sqrt(np.pi/8)

def calc_area(x0,x1,y0,y1):
    return (x1-x0)*(y1-y0)


class ZigguratRNG:
    
    def pdf(self, x):
        return pdf(x, mu=self.mu, std=self.std)
    
    def qf(self, p):
        return qf(p,mu=self.mu,std=self.std)
    
    def __init__(self, a=-3, b=3, k=128, mu=0, std=1):
        self.a = a
        self.b = b
        self.k = k
        self.mu = mu
        self.std = std
        self.z = self.generate_ziggurat()
        self._niters = 0

    @property
    def zA(self):
        return calc_area(*self.z[0][1])
    
    def generate_ziggurat(self, **kwargs):
        a = kwargs.get('a',self.a)
        b = kwargs.get('b',self.b)
        k = kwargs.get('k',self.k)
        c = (b-a)/float(k)
        z = []
        for i in range(k-1):
            z.append((i,
                      (self.a+i*c,self.a+(i+1)*c,
                       self.pdf(self.a+i*c),
                       self.pdf(self.a+(i+1)*c))))
        return z

    def single_sample(self, **kwargs):
        zi, zA = choice(self.z)
        x0, x1, y0, y1 = zA
        if zi == 0: ## special case (R0)
            while True:
                w = 1.23*self.zA*np.random.rand()
                if w <= self.zA:
                    xi = w / (y1-y0) ## sampling from within R0
                else:
                    xi = self.qf(w) ## sampling from the tail
                if xi >= x0 and xi <= x1:
                    return xi
                else:
                    return None
        else: ## sample from any other rectangles (Ri)
            xi = x0+self.zA*np.random.rand() / (y1-y0)
            if xi < x1 and xi > x0:
                return xi
            else:
                y = y0+(y1-y0)*np.random.rand()
                if y < self.pdf(xi):
                    xi = self.qf(y)
                    if xi < x1 and xi > x0:
                        return xi
                return None ## reject sample

    def nsamples(self, n=10, iters=True):
        out = []
        i = 0
        while True:
            i = i + 1
            s = self.single_sample()
            if s is not None:
                out.append(s)
                # print('(ziggurat) iter=', i, 'len=', len(out))
            if len(out) == n:
                if not iters:
                    return out
                self._niters = i
                return self._niters, out


def naive_sample(a=4,b=5,n=10):
    out = []
    i = 0
    while True:
        i = i + 1
        s = np.random.normal(0,1)
        if s > a and s < b:
           out.append(s)
           # print('(naive) iter=', i, 'len=',len(out))
        if len(out) == n:
            return i, out


if __name__=='__main__':
    a = 2; b = 5; n = 10000
    t0 = time.time()
    zrng = ZigguratRNG(a=a,b=b,k=128,mu=0,std=1)
    niters, samples = zrng.nsamples(n=n)
    print(time.time()-t0, ': ziggurat:', niters, np.mean(samples), np.std(samples))
    t0 = time.time()
    iters, samps = naive_sample(a=a,b=b,n=n)
    print(time.time()-t0,': naive:', iters, np.mean(samps), np.std(samps))
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(nrows=2)
    axs[0].plot(samples, 'k.')
    axs[1].plot(samps, 'b.')
    plt.show()
