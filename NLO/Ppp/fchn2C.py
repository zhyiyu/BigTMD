#!/usr/bin/env python
import numpy as np
from mpmath import fp
from numba import jit
import numpy as np
EulerGamma=np.euler_gamma
@jit(cache=True)
def _PolyLOG(s, z):
    tol = 1e-10
    l = 0
    k = 1
    zk = z
    while 1:
        term = zk / k**s
        l += term
        if abs(term) < tol:
            break
        zk *= z
        k += 1
    return l
@jit(cache=True)
def PolyLOG(s, z):
    #return fp.polylog(s,z)
    #if abs(z) > 0.75:
    #  return -PolyLOG(s,1-z) + np.pi**2/6 - np.log(z)*np.log(1-z)
    if abs(z) >1: 
      return -PolyLOG(s, 1/z) - np.pi**2/6 - 0.5*np.log(-z)**2
    return _PolyLOG(s, z)
@jit(cache=True)
def regular(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,nf=None):
    return -0.0416666666666667*(-s23 + t)*(2*Q**2*s23 - Q**2*t + s*s23)*np.log((2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2))/(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)))/(np.pi**5*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) + 0.00694444444444444*(s23 - t)**4*((-3 - 3*(2*Q**2 + s + t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((s23 - t)*(4*Q**2*s23 + (s + t)**2)))*(5 - 3*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 2*(10*Q**4 + 2*Q**2*(5*s - 3*s23 + 5*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)**2) - (8*Q**2 + 4*s + 4*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))) + (36*Q**2 + 18*s + 18*t)/np.sqrt(4*Q**2*s23 + (s + t)**2) + (-4*Q**2*s23 - 2*s*(s23 + t) + 2*t*(s23 - t))*(24 - 4*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) - (54*Q**2 + 27*s + 27*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)) + 3*(-3 + 5*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)))*(Q**2 + 0.5*s + 0.5*t)**2/(s23*(Q**2 + 0.25*(s + t)**2/s23)))/((s23 - t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))/(np.pi**5*(2*Q**2 + s + t)*(-Q**2 - s + s23 - t)**2*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) - 0.000434027777777778*(s23 - t)**4*((-3 + (2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)))*(256*Q**2*s23 + 128*s*(s23 + t) - 128*t*(s23 - t))/((s23 - t)*np.sqrt(4*Q**2*s23 + (s + t)**2)) - 48*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(3 - 30*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) + 35*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/((s23 - t)**4*(4*Q**2*s23 + (s + t)**2)**2))*(Q**2 + 0.5*s + 0.5*t)**3 - (105 - 90*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 9*(2*Q**2 + s + t)**4/(4*Q**2*s23 + (s + t)**2)**2 - 18*(5 - 18*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 5*(2*Q**2 + s + t)**4/(4*Q**2*s23 + (s + t)**2)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) + 3*(64*Q**2 + 32*s + 32*t)*(10*Q**4 + 2*Q**2*(5*s - 3*s23 + 5*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**3/((s23 - t)**3*(4*Q**2*s23 + (s + t)**2)**3) + 3*(3 - 30*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 35*(2*Q**2 + s + t)**4/(4*Q**2*s23 + (s + t)**2)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/((s23 - t)**4*(4*Q**2*s23 + (s + t)**2)**2) - 3*(64*Q**2 + 32*s + 32*t)*(-6*Q**4 - 2*Q**2*(3*s - 5*s23 + 3*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)**2))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))) + (87 - 294*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) + 55*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/((s23 - t)**4*(4*Q**2*s23 + (s + t)**2)**2))*(4*Q**2 + 2.0*s + 2.0*t)/np.sqrt(4*Q**2*s23 + (s + t)**2) + 192*(4*Q**2*s23 + (s + t)**2)**(-2.5)*(2*Q**2 + s + t)**2*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))*(10*Q**4*s23**2 + 2*Q**2*s23*(5*s*(s23 + t) - 3*s23**2 + s23*t + 2*t**2) + s**2*(s23**2 + 8*s23*t + t**2) + 2*s*t*(-4*s23**2 + 3*s23*t + t**2) + t**2*(s23 - t)**2)/(-s23 + t)**3)/(np.pi**5*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) - 0.0416666666666667*(s23 - t)**3/(np.pi**5*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2) + 0.00520833333333333*(s23 - t)**2*(-(6 - 2*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 4*(6*Q**4 + Q**2*(6*s - 2*s23 + 6*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)**2) - 2*(8*Q**2 + 4*s + 4*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))) + (8*Q**2 + 4*s + 4*t)/np.sqrt(4*Q**2*s23 + (s + t)**2) - (4*Q**2*s23 + (s + t)**2)**(-1.5)*(24*Q**2 + 12*s + 12*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/(s23 - t)**2 + (32*Q**2*s23 + 16*s*(s23 + t) + 16*t*(-s23 + t))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(2*Q**4 + 3*Q**2*s - Q**2*s23 + Q**2*t + s**2 - 3*s23**2 + 6*s23*t - 3*t**2)/(np.pi**5*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) - 0.00347222222222222*(s23 - t)*((24*Q**4*s23 + 12*Q**2*(s*(2*s23 + t) + 2*s23**2 - 2*s23*t + t**2) + 12*s*s23*(s + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)) + (24*Q**2*s23 + 12*s*(s23 + t) + 12*t*(-s23 + t))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(2*Q**4 + 3*Q**2*s + 4*Q**2*s23 - 3*Q**2*t + s**2 + 2*s*s23 - s*t + 2*s23**2 - 4*s23*t + 2*t**2)/(np.pi**5*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) - 0.0208333333333333*(s23 - t)**2*(-2*s23*t + 2*t**2)/(np.pi**5*t*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2) - 0.00520833333333333*(s23 - t)*(-4*Q**4*t - 8*Q**2*s*t + 4*Q**2*s23*t - 4*Q**2*t**2 - 4*s**2*t + 4*s*s23*t - 4*s*t**2 + 4*s23**2*t - 8*s23*t**2 + 4*t**3)/(np.pi**5*t*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2) - 0.00694444444444444*(s23 - t)**2*(-6*s23*t**2 + 6*t**3)/(np.pi**5*t**2*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2) + 0.0104166666666667*(s23 - t)*(2*Q**4*t**2 + 4*Q**2*s*t**2 - 2*Q**2*s23*t**2 + 2*Q**2*t**3 + 2*s**2*t**2 - 2*s*s23*t**2 + 2*s*t**3 - 2*s23**2*t**2 + 4*s23*t**3 - 2*t**4)/(np.pi**5*t**2*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)**2) + 0.0208333333333333*(-2*Q**2*s23*t**2 + 2*Q**2*t**3 - 2*s*s23*t**2 + 2*s*t**3)/(np.pi**5*t**2*(2*Q**2 + s + t)*(Q**2 + s - s23 + t)) + 0.000868055555555556*(Q**2 + s)*(s23 - t)*(24 - 12*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(2*Q**2 + s + t)**2*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/(-s23 + t) - (48*Q**2 + 24*s + 24*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)) + (24*Q**2*s23 + 12*s*(s23 + t) + 12*t*(-s23 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(Q**4 + 2*Q**2*s + s**2 + s23**2 - 2*s23*t + t**2)/(np.pi**5*Q**2*(Q**2 + s - s23 + t)**3) - 0.000868055555555556*(s23 - t)**4*(24*Q**2*(4*Q**2*s23 + (s + t)**2)**(-4.5)*(Q**2 + s - s23 + t)*((4*Q**2*s23 + (s + t)**2)**2*(6*Q**2 + 3*s + 3*t)*(Q**4 + Q**2*(s - 5*s23 + t) - (s + t)**2) + (4*Q**2*s23 + (s + t)**2)*(12*Q**2 + 6*s + 6*t)*(-5*Q**4 + Q**2*(-5*s + 9*s23 - 5*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/(s23 - t)**2 + (10*Q**2 + 5*s + 5*t)*(7*Q**4 + Q**2*(7*s - 3*s23 + 7*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/(s23 - t)**4 + 4*(4*Q**2*s23 + (s + t)**2)**2*(9*Q**4 + Q**2*(9*s - 5*s23 + 9*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/(-s23 + t) - (48*Q**2*s23 + 12*(s + t)**2)*(5*Q**4 + Q**2*(5*s - s23 + 5*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**3/(-s23 + t)**3)*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))) + 48 - 96*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) + 16*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/((s23 - t)**4*(4*Q**2*s23 + (s + t)**2)**2) + (48*Q**2 + 24*s + 24*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))*(26*Q**4*s23**2 + 2*Q**2*s23*(13*s*(s23 + t) - 11*s23**2 + 9*s23*t + 2*t**2) + s**2*(s23**2 + 24*s23*t + t**2) + 2*s*t*(-12*s23**2 + 11*s23*t + t**2) + t**2*(s23 - t)**2)/((-s23 + t)**3*(4*Q**2*s23 + (s + t)**2)**2) - 72*(2*Q**2 + s + t)**3*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))*(10*Q**4*s23**2 + 2*Q**2*s23*(5*s*(s23 + t) - 3*s23**2 + s23*t + 2*t**2) + s**2*(s23**2 + 8*s23*t + t**2) + 2*s*t*(-4*s23**2 + 3*s23*t + t**2) + t**2*(s23 - t)**2)/((-s23 + t)**3*(4*Q**2*s23 + (s + t)**2)**3) - (51 - 222*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) + 115*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/((s23 - t)**4*(4*Q**2*s23 + (s + t)**2)**2))*(Q**2 + 0.5*s + 0.5*t)**2/(s23*(Q**2 + 0.25*(s + t)**2/s23)) + 3*(3 - 30*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)) + 35*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**4/((s23 - t)**4*(4*Q**2*s23 + (s + t)**2)**2))*(Q**2 + 0.5*s + 0.5*t)**4/(s23**2*(Q**2 + 0.25*(s + t)**2/s23)**2))/(np.pi**5*Q**2*(Q**2 + s - s23 + t)**3) + 0.00520833333333333*(s23 - t)**3*(2*Q**2 + 2*s + s23 - t)*(6*Q**2*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(Q**2 + s - s23 + t)*(4*Q**2 + 2*s + 2*t + (-2*Q**2*s23 - s*(s23 + t) + t*(s23 - t))*(3 - 3*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 4*(5*Q**4 + Q**2*(5*s - s23 + 5*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)**2) - (12*Q**2 + 6*s + 6*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)))/(s23 - t))*np.log((2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))) + 8 - 6*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + 6*(12*Q**4 + 4*Q**2*(3*s - 2*s23 + 3*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)**2) + (4*Q**2 + 2*s + 2*t)*(30*Q**4 + Q**2*(30*s - 26*s23 + 30*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**3/((s23 - t)**3*(4*Q**2*s23 + (s + t)**2)**3) - (12*Q**2 + 6*s + 6*t)*(-6*Q**4 - 2*Q**2*(3*s - 5*s23 + 3*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)**2))/(np.pi**5*Q**2*(Q**2 + s - s23 + t)**3) - 0.0104166666666667*(s23 - t)**2*(2 - (2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) - (4*Q**2*s23 + (s + t)**2)**(-2.5)*(-4*Q**2 - 2*s - 2*t + 2*np.sqrt(4*Q**2*s23 + (s + t)**2))*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))*(6*Q**6*s23**2 + Q**4*s23*(9*s*s23 + 6*s*t + 2*s23**2 - 3*s23*t + 4*t**2) + Q**2*(s**2*(5*s23**2 + 6*s23*t + t**2) + s*(s23**3 + 3*s23*t**2 + 2*t**3) + t*(-3*s23**3 + 5*s23**2*t - 3*s23*t**2 + t**3)) + s*s23*(s + t)*(s*(s23 + 2*t) + 2*t*(-s23 + t)))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/(s23 - t)**2 + (12*Q**4 + 4*Q**2*(3*s - 2*s23 + 3*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)**2) - (4*Q**2 + 2*s + 2*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)))*(3*Q**4 + 6*Q**2*s + 2*Q**2*s23 - 2*Q**2*t + 3*s**2 + 2*s*s23 - 2*s*t + s23**2 - 2*s23*t + t**2)/(np.pi**5*Q**2*(Q**2 + s - s23 + t)**3)
@jit(cache=True)
def delta(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0
@jit(cache=True)
def plus1B(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0
@jit(cache=True)
def plus2B(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0
