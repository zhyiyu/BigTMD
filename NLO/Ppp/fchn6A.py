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
    return 0.0208333333333333*(12*Q**4*t + 18*Q**2*s*t - 8*Q**2*s23*t + 14*Q**2*t**2 + 6*s**2*t - 4*s*s23*t + 10*s*t**2 - 4*s23*t**2 + 4*t**3)*np.log((2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2))/(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)))/(np.pi**5*t*(2*Q**2 + s + t)*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) + (0.0625*(Q**2*t + s*t)/np.pi**5 - (-0.03125*np.log(s23)/np.pi**5 + 0.03125*np.log(np.pi)/np.pi**5 + 0.0625*np.log(2)/np.pi**5)*(6*Q**2*t + 6*s*t - 4*s23*t + 4*t**2) - 0.0625*(6*Q**2*t + 6*s*t - 4*s23*t + 4*t**2)*np.log(mu)/np.pi**5 + 0.03125*EulerGamma*(6*Q**2*t + 6*s*t - 4*s23*t + 4*t**2)/np.pi**5)/(t*(3.0*s - 3.0*s23)) + (((-0.03125*np.log(s23)/np.pi**5 + 0.03125*np.log(np.pi)/np.pi**5 + 0.0625*np.log(2)/np.pi**5)*(4*Q**4*t + 6*Q**2*s*t + 2*Q**2*t**2 + 2*s**2*t + 2*s*t**2) + 0.0625*(-2*Q**4*t - 3*Q**2*s*t - Q**2*t**2 - s**2*t - s*t**2)/np.pi**5)*(Q**2*s + s**2 - s*s23 + s*t) + 0.0625*(Q**2*s + s**2 - s*s23 + s*t)*(4*Q**4*t + 6*Q**2*s*t + 2*Q**2*t**2 + 2*s**2*t + 2*s*t**2)*np.log(mu)/np.pi**5 - 0.03125*EulerGamma*(Q**2*s + s**2 - s*s23 + s*t)*(4*Q**4*t + 6*Q**2*s*t + 2*Q**2*t**2 + 2*s**2*t + 2*s*t**2)/np.pi**5 + 0.03125*(2*Q**2*s23 + s**2 - s*s23 + s*t + s23*t)*(4*Q**4*t + 6*Q**2*s*t + 2*Q**2*t**2 + 2*s**2*t + 2*s*t**2)/np.pi**5)/(t*(3.0*Q**2 + 3.0*s)*(s - s23)**2*(2*Q**2 + s + t)) + 0.000868055555555556*(-s + s23)*(-(24*Q**4*s23 + 12*Q**2*(s**2 + s*(2*s23 + t) + 2*s23*(-s23 + t)) + 12*s*(s + t)*(s - s23 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((s - s23)*(4*Q**2*s23 + (s + t)**2)) + (-12*s**2 - 12*s*(-s23 + t) - 12*s23*(2*Q**2 + t))/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(12*Q**4*t + 18*Q**2*s*t + 6*Q**2*t**2 + 6*s**2*t + 6*s*t**2)/(np.pi**5*t*(Q**2 + s)*(2*Q**2 + s + t)*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) + 0.0208333333333333*(-3*Q**4*t**2 - 3*Q**2*s*t**2 - 3*Q**2*t**3 - 3*s*t**3)/(np.pi**5*t**2*(Q**2 + s)*(Q**2 + t)) + 0.0208333333333333*(2*np.log(mu) - np.log(s23) + np.log(Q**2*(s - s23)**2/(s**2*(Q**2 + s - s23 + t))) - EulerGamma + np.log(np.pi) + 2*np.log(2))*(8*Q**6*t + 20*Q**4*s*t - 4*Q**4*s23*t + 8*Q**4*t**2 + 16*Q**2*s**2*t - 6*Q**2*s*s23*t + 14*Q**2*s*t**2 - 2*Q**2*s23*t**2 + 2*Q**2*t**3 + 4*s**3*t - 2*s**2*s23*t + 6*s**2*t**2 - 2*s*s23*t**2 + 2*s*t**3)/(np.pi**5*s*t*(Q**2 + s)*(2*Q**2 + s + t)) + 0.0208333333333333*(Q**2*s23 + s*t)*(s**2 - 2*s*s23 + 2*s23**2)*(-np.log(4*np.pi) + EulerGamma + 1)/(np.pi**5*s**2*(s - s23)**2) - 0.000217013888888889*(-s + s23)*(24 + 12*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(2*Q**2 + s + t)**2*(s**2 + s*(-s23 + t) + s23*(2*Q**2 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/(s - s23) + (48*Q**2 + 24*s + 24*t)*(s**2 + s*(-s23 + t) + s23*(2*Q**2 + t))/((s - s23)*(4*Q**2*s23 + (s + t)**2)) - (12*s**2 + 12*s*(-s23 + t) + 12*s23*(2*Q**2 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(6*Q**2 + 6*s - 4*s23 + 4*t)/(np.pi**5*Q**2*(Q**2 + s - s23 + t)) - 0.00260416666666667*(s - s23)**2*((-1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2))*(1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2))*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(-(4*Q**2*s23 + (s + t)**2)*(2*Q**2 + s + t) + (s**2 + s*(-s23 + t) + s23*(2*Q**2 + t))*(12*Q**4*s23 + 2*Q**2*(s + 2*s23)*(3*s - 2*s23 + 3*t) + (s + t)*(5*s**2 - 5*s*s23 + 5*s*t + s23*t))/(s - s23)**2)*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))) + 4 - 2*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) + (8*Q**2 + 4*s + 4*t)*(s**2 + s*(-s23 + t) + s23*(2*Q**2 + t))/((s - s23)*(4*Q**2*s23 + (s + t)**2)) + 2*(12*Q**4 + 4*Q**2*(3*s - 2*s23 + 3*t) + (s + t)**2)*(s**2 + s*(-s23 + t) + s23*(2*Q**2 + t))**2/((s - s23)**2*(4*Q**2*s23 + (s + t)**2)**2))/(np.pi**5*Q**2*(Q**2 + s - s23 + t)) + 0.0104166666666667*(-8*Q**2 - 8*s + 4*s23 - 4*t)/(np.pi**5*Q**2)
@jit(cache=True)
def delta(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0.111111111111111*(Q**2 + s)*(s - s23)**2*(4*Q**2*s23 + (s + t)**2)*(12*EulerGamma*(0.03125*np.log(mu)/np.pi**5 + 0.015625*np.log(np.pi)/np.pi**5 + 0.03125*np.log(2)/np.pi**5) - 6*EulerGamma*(0.03125*np.log(mu)/np.pi**5 - 0.03125*EulerGamma/np.pi**5 + 0.015625*np.log(np.pi)/np.pi**5 + 0.03125*np.log(2)/np.pi**5) - (-0.1875*np.log(mu)/np.pi**5 - 0.1875*np.log(2)/np.pi**5 - 0.09375*np.log(np.pi)/np.pi**5 + 0.09375*EulerGamma/np.pi**5 + 0.03125*(6*Q**2*s23 + 3*Q**2*(s - s23)*np.log(s**2*(Q**2 + s - s23 + t)/(Q**2*(s - s23)**2)) + 3*s**2 + 3*s*t)/(np.pi**5*Q**2*(s - s23)))*np.log(B) - 0.046875*np.log(B)**2/np.pi**5 - 0.1875*np.log(mu)**2/np.pi**5 - 12*(0.015625*np.log(np.pi)/np.pi**5 + 0.03125*np.log(2)/np.pi**5)*np.log(mu) - 0.1875*np.log(2)*np.log(np.pi)/np.pi**5 - 0.046875*(EulerGamma**2 + 0.166666666666667*np.pi**2)/np.pi**5 - 0.1875*np.log(2)**2/np.pi**5 - 0.046875*np.log(np.pi)**2/np.pi**5 - 0.09375*(-0.333333333333333*np.pi**2 + 2*EulerGamma**2)/np.pi**5 - 0.015625*(4*Q**2*s23 + (s + t)**2)*(2*Q**2*(6*(np.log(-2*s*(Q**2 + s - s23 + t)/(2*Q**2*s23 + s**2 - s*s23 + s*t - s*np.sqrt(4*Q**2*s23 + (s + t)**2) + s23*t + s23*np.sqrt(4*Q**2*s23 + (s + t)**2))) - 2)*np.log(2*s*(Q**2 + s - s23 + t)/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2))) + np.pi**2)*(Q**2 + s - s23 + t)/(4*Q**2*s23 + (s + t)**2) + 12*Q**2*(PolyLOG(2, -(2*Q**2*s23 + s**2 - s*s23 + s*t + s*np.sqrt(4*Q**2*s23 + (s + t)**2) + s23*t - s23*np.sqrt(4*Q**2*s23 + (s + t)**2))/((s - s23)*(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2)))) - PolyLOG(2, 2*s*(Q**2 + s - s23 + t)/((s - s23)*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))))*(Q**2 + s - s23 + t)/(4*Q**2*s23 + (s + t)**2) + 3*Q**2*(Q**2 + s - s23 + t)*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))**3/(4*Q**2*s23 + (s + t)**2)**2)/(4*Q**2*s23 + (s + t)**2) + (-12*Q**2*(Q**2 + s - s23 + t)*np.log(2*s*(Q**2 + s - s23 + t)/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2)))/(4*Q**2*s23 + (s + t)**2) - 3 + 3*(2*Q**2 + s + t)*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))/(4*Q**2*s23 + (s + t)**2) - 3*(-s**2 + s*(s23 - t) - s23*(2*Q**2 + t))/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*np.log(-1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2)) + 3*(4*Q**2*(Q**2 + s - s23 + t)*np.log(1 + (-s**2 + s*(s23 - t) - s23*(2*Q**2 + t))/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2)))/(4*Q**2*s23 + (s + t)**2) - 1 + (2*Q**2 + s + t)*(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(4*Q**2*s23 + (s + t)**2) + (-s**2 + s*(s23 - t) - s23*(2*Q**2 + t))/((s - s23)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*np.log(1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2)))/(np.pi**5*Q**2*(Q**2 + s - s23 + t)) + (0.1875*np.log(mu)/np.pi**5 - 0.09375*EulerGamma/np.pi**5 + 0.09375*np.log(np.pi)/np.pi**5 + 0.1875*np.log(2)/np.pi**5)*(2*Q**2*s23 + Q**2*(s - s23)*np.log(s**2*(Q**2 + s - s23 + t)/(Q**2*(s - s23)**2)) + s**2 + s*t)/(Q**2*(s - s23)))/(s**2*(Q**2 + 0.25*(s + t)**2/s23)*(-s + s23))
@jit(cache=True)
def plus1B(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return -0.0833333333333333*s23*(Q**2 + s)*(s - s23)*np.log(mu)/(np.pi**5*s**2) + 0.0416666666666667*s23*(Q**2 + s)*(s - s23)*np.log(s**2*(Q**2 + s - s23 + t)/(Q**2*(s - s23)**2))/(np.pi**5*s**2) - 0.0833333333333333*s23*(Q**2 + s)*(s - s23)*np.log(2)/(np.pi**5*s**2) - 0.0416666666666667*s23*(Q**2 + s)*(s - s23)*np.log(np.pi)/(np.pi**5*s**2) + 0.0416666666666667*s23*(Q**2 + s)*(2*Q**2*s23 + EulerGamma*Q**2*(s - s23) + s**2 + s*t)/(np.pi**5*Q**2*s**2)
@jit(cache=True)
def plus2B(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0.0416666666666667*s23*(Q**2 + s)*(s - s23)/(np.pi**5*s**2)
