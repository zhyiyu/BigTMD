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
    return 0.0208333333333333*(2*Q**4*s - 8*Q**4*s23 + 8*Q**4*t + 3*Q**2*s**2 - 16*Q**2*s*s23 + 17*Q**2*s*t + 12*Q**2*s23**2 - 28*Q**2*s23*t + 16*Q**2*t**2 + s**3 - 6*s**2*s23 + 7*s**2*t + 6*s*s23**2 - 18*s*s23*t + 12*s*t**2 + 6*s23**2*t - 12*s23*t**2 + 6*t**3)*np.log((2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2))/(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)))/(np.pi**5*t*(2*Q**2 + s + t)*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) + 0.000868055555555556*(s23 - t)*(-(24*Q**4*s23 + 12*Q**2*(s*(2*s23 + t) - 2*s23**2 + 2*s23*t + t**2) + 12*t*(s + t)*(s - s23 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((-s23 + t)*(4*Q**2*s23 + (s + t)**2)) + (-24*Q**2*s23 - 12*s*(s23 + t) - 12*t*(-s23 + t))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(4*Q**4*s - 8*Q**4*s23 + 8*Q**4*t + 2*Q**2*s**2 - 4*Q**2*s*s23 + 10*Q**2*s*t - 12*Q**2*s23*t + 12*Q**2*t**2 + 2*s**2*t - 4*s*s23*t + 6*s*t**2 - 4*s23*t**2 + 4*t**3)/(np.pi**5*t*(Q**2 + t)*(2*Q**2 + s + t)*np.sqrt(4*Q**2*s23 + s**2 + 2*s*t + t**2)) + 0.0833333333333333*(s23 - t)*(-Q**2 - s + s23 - t)/(np.pi**5*t**2) + 0.0208333333333333*(-2*np.log(mu) + np.log(s23) - 2*np.log(2) - np.log(np.pi) + EulerGamma)*(-2*Q**2*s23 + Q**2*t - 2*s*s23 + s*t + 2*s23**2 - 4*s23*t + 2*t**2)/(np.pi**5*t**2) + 0.0208333333333333*(2*np.log(mu) - np.log(s23) + np.log(Q**2*(s23 - t)**2/(t**2*(Q**2 + s - s23 + t))) - EulerGamma + np.log(np.pi) + 2*np.log(2))*(-4*Q**6*s23 + 6*Q**6*t - 10*Q**4*s*s23 + 13*Q**4*s*t + 16*Q**4*s23**2 - 38*Q**4*s23*t + 25*Q**4*t**2 - 4*Q**2*s**2*s23 + 5*Q**2*s**2*t + 8*Q**2*s*s23**2 - 30*Q**2*s*s23*t + 26*Q**2*s*t**2 + 24*Q**2*s23**2*t - 50*Q**2*s23*t**2 + 27*Q**2*t**3 - 4*s**2*s23*t + 5*s**2*t**2 + 8*s*s23**2*t - 20*s*s23*t**2 + 13*s*t**3 + 8*s23**2*t**2 - 16*s23*t**3 + 8*t**4)/(np.pi**5*t**2*(Q**2 + t)*(2*Q**2 + s + t)) + 0.0208333333333333*(Q**6*s23 + 2*Q**4*s*s23 - Q**4*s23**2 + 3*Q**4*s23*t - Q**4*t**2 + Q**2*s**2*s23 - Q**2*s*s23**2 + 4*Q**2*s*s23*t - Q**2*s*t**2 - Q**2*s23**2*t + 2*Q**2*s23*t**2 - Q**2*t**3 + s**2*s23*t - s*s23**2*t + 2*s*s23*t**2 - s*t**3)/(np.pi**5*t**2*(Q**2 + s)*(Q**2 + t)) + 0.333333333333333*(s23 - t)*(-(0.5*np.log(mu)/np.pi**5 - 0.25*np.log(s23)/np.pi**5 - 0.25*EulerGamma/np.pi**5 + 0.25*np.log(np.pi)/np.pi**5 + 0.5*np.log(2)/np.pi**5)*(2*Q**2*s23**2 - 2*Q**2*s23*t + s*s23*t - s*t**2 + s23*t**2 - t**3) - 0.25*(4*Q**2*s23**2 - 2*Q**2*t**2 + 4*s*s23*t - 2*s*t**2 + 2*s23*t**2 - 2*t**3 + (s23 - t)*(2*Q**2*s23 + t*(s + t))*np.log(Q**2*(s23 - t)**2/(t**2*(Q**2 + s - s23 + t))))/np.pi**5)*(-Q**2 - s + s23 - t)**2/(t**4*(Q**2 + s - s23 + t)**2) - 0.0416666666666667*(Q**2*s23 + s*t)*(-EulerGamma + 1 + np.log(4*np.pi))*(2*s23**2 - 2*s23*t + t**2)/(np.pi**5*t**4) - 0.00260416666666667*(s23 - t)**2*((-1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2))*(1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2))*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(-(4*Q**2*s23 + (s + t)**2)*(2*Q**2 + s + t) + (2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))*(12*Q**4*s23 + 2*Q**2*(2*s23 + t)*(3*s - 2*s23 + 3*t) + (s + t)*(s*(s23 + 5*t) + 5*t*(-s23 + t)))/(s23 - t)**2)*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))) + 4 - 2*(2*Q**2 + s + t)**2/(4*Q**2*s23 + (s + t)**2) - (8*Q**2 + 4*s + 4*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((s23 - t)*(4*Q**2*s23 + (s + t)**2)) + 2*(12*Q**4 + 4*Q**2*(3*s - 2*s23 + 3*t) + (s + t)**2)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))**2/((s23 - t)**2*(4*Q**2*s23 + (s + t)**2)**2))/(np.pi**5*Q**2*(Q**2 + s - s23 + t)) - 0.000217013888888889*(s23 - t)*(24 - (48*Q**2 + 24*s + 24*t)*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))/((s23 - t)*(4*Q**2*s23 + (s + t)**2)) + 12*(4*Q**2*s23 + (s + t)**2)**(-1.5)*(2*Q**2 + s + t)**2*(2*Q**2*s23 + s*(s23 + t) + t*(-s23 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/(-s23 + t) - (24*Q**2*s23 + 12*s*(s23 + t) + 12*t*(-s23 + t))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*(6*Q**2 + 6*s - 8*s23 + 8*t)/(np.pi**5*Q**2*(Q**2 + s - s23 + t)) - 0.0104166666666667*(8*Q**2 + 8*s - 14*s23 + 14*t)/(np.pi**5*Q**2) + 0.333333333333333*(s23 - t)*((-6*Q**4*s23**2 + 4*Q**4*s23*t + 2*Q**2*t*(-2*s*s23 + s*t - s23*t + t**2))*(0.25*np.log(mu)/np.pi**5 - 0.125*np.log(s23)/np.pi**5 - 0.125*EulerGamma/np.pi**5 + 0.125*np.log(np.pi)/np.pi**5 + 0.25*np.log(2)/np.pi**5) + 0.125*(-16*Q**4*s23**2 + 2*Q**4*t**2 + 2*Q**2*t*(-8*s*s23 + s*t - 3*s23*t + t**2) + 2*Q**2*(Q**2*s23*(3*s23 - 2*t) - t*(s*(-2*s23 + t) + t*(-s23 + t)))*np.log(t**2*(Q**2 + s - s23 + t)/(Q**2*(s23 - t)**2)) - t**2*(s + t)**2)/np.pi**5)*(-Q**2 - s + s23 - t)**3/(Q**2*t**4*(Q**2 + s - s23 + t)**3)
@jit(cache=True)
def delta(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0.111111111111111*(s23 - t)*(4*Q**2*s23 + (s + t)**2)*(Q**2 + s - 3*s23 + 3*t)*(12*EulerGamma*(0.03125*np.log(mu)/np.pi**5 + 0.015625*np.log(np.pi)/np.pi**5 + 0.03125*np.log(2)/np.pi**5) - 6*EulerGamma*(0.03125*np.log(mu)/np.pi**5 - 0.03125*EulerGamma/np.pi**5 + 0.015625*np.log(np.pi)/np.pi**5 + 0.03125*np.log(2)/np.pi**5) - (-0.1875*np.log(mu)/np.pi**5 - 0.1875*np.log(2)/np.pi**5 - 0.09375*np.log(np.pi)/np.pi**5 + 0.09375*EulerGamma/np.pi**5 + 0.03125*(-6*Q**2*s23 + 3*Q**2*(s23 - t)*np.log(t**2*(Q**2 + s - s23 + t)/(Q**2*(s23 - t)**2)) - 3*t*(s + t))/(np.pi**5*Q**2*(s23 - t)))*np.log(B) - 0.046875*np.log(B)**2/np.pi**5 - 0.1875*np.log(mu)**2/np.pi**5 - 12*(0.015625*np.log(np.pi)/np.pi**5 + 0.03125*np.log(2)/np.pi**5)*np.log(mu) - 0.1875*np.log(2)*np.log(np.pi)/np.pi**5 - 0.046875*(EulerGamma**2 + 0.166666666666667*np.pi**2)/np.pi**5 - 0.1875*np.log(2)**2/np.pi**5 - 0.046875*np.log(np.pi)**2/np.pi**5 - 0.09375*(-0.333333333333333*np.pi**2 + 2*EulerGamma**2)/np.pi**5 - 0.015625*(4*Q**2*s23 + (s + t)**2)*(2*Q**2*(6*(np.log(-2*t*(Q**2 + s - s23 + t)/(2*Q**2*s23 + s*(s23 + t) - (-s23 + t)*(-t + np.sqrt(4*Q**2*s23 + (s + t)**2)))) - 2)*np.log(2*t*(Q**2 + s - s23 + t)/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2))) + np.pi**2)*(Q**2 + s - s23 + t)/(4*Q**2*s23 + (s + t)**2) + 12*Q**2*(PolyLOG(2, (2*Q**2*s23 + s*(s23 + t) + (-s23 + t)*(t + np.sqrt(4*Q**2*s23 + (s + t)**2)))/((s23 - t)*(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2)))) - PolyLOG(2, 2*t*(Q**2 + s - s23 + t)/((-s23 + t)*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))))*(Q**2 + s - s23 + t)/(4*Q**2*s23 + (s + t)**2) + 3*Q**2*(Q**2 + s - s23 + t)*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2)))*np.log((2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))**3/(4*Q**2*s23 + (s + t)**2)**2)/(4*Q**2*s23 + (s + t)**2) + (-12*Q**2*(Q**2 + s - s23 + t)*np.log(2*t*(Q**2 + s - s23 + t)/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))/(4*Q**2*s23 + (s + t)**2) - 3 + 3*(2*Q**2 + s + t)*(2*Q**2 + s + t + np.sqrt(4*Q**2*s23 + (s + t)**2))/(4*Q**2*s23 + (s + t)**2) - 3*(-2*Q**2*s23 - s*(s23 + t) + t*(s23 - t))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*np.log(-1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2)) + 3*(4*Q**2*(Q**2 + s - s23 + t)*np.log(1 + (-2*Q**2*s23 - s*(s23 + t) + t*(s23 - t))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))/(4*Q**2*s23 + (s + t)**2) - 1 + (2*Q**2 + s + t)*(2*Q**2 + s + t - np.sqrt(4*Q**2*s23 + (s + t)**2))/(4*Q**2*s23 + (s + t)**2) + (-2*Q**2*s23 - s*(s23 + t) + t*(s23 - t))/((-s23 + t)*np.sqrt(4*Q**2*s23 + (s + t)**2)))*np.log(1 + (2*Q**2 + s + t)/np.sqrt(4*Q**2*s23 + (s + t)**2)))/(np.pi**5*Q**2*(Q**2 + s - s23 + t)) + (-2*Q**2*s23 + Q**2*(s23 - t)*np.log(t**2*(Q**2 + s - s23 + t)/(Q**2*(s23 - t)**2)) - t*(s + t))*(0.1875*np.log(mu)/np.pi**5 - 0.09375*EulerGamma/np.pi**5 + 0.09375*np.log(np.pi)/np.pi**5 + 0.1875*np.log(2)/np.pi**5)/(Q**2*(s23 - t)))/(t**2*(Q**2 + 0.25*(s + t)**2/s23))
@jit(cache=True)
def plus1B(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return 0.0833333333333333*s23*(s23 - t)*(Q**2 + s - 3*s23 + 3*t)*np.log(mu)/(np.pi**5*t**2) - 0.0416666666666667*s23*(s23 - t)*(Q**2 + s - 3*s23 + 3*t)*np.log(t**2*(Q**2 + s - s23 + t)/(Q**2*(s23 - t)**2))/(np.pi**5*t**2) + 0.0416666666666667*s23*(s23 - t)*(Q**2 + s - 3*s23 + 3*t)*np.log(np.pi)/(np.pi**5*t**2) + 0.0833333333333333*s23*(s23 - t)*(Q**2 + s - 3*s23 + 3*t)*np.log(2)/(np.pi**5*t**2) - 0.0416666666666667*s23*(Q**2*(s23*(-2 + EulerGamma) - EulerGamma*t) - t*(s + t))*(Q**2 + s - 3*s23 + 3*t)/(np.pi**5*Q**2*t**2)
@jit(cache=True)
def plus2B(g=None,gp=None,s=None,t=None,Q=None,s23=None,mu=None,B=None,nf=None):
    return -0.0416666666666667*s23*(s23 - t)*(Q**2 + s - 3*s23 + 3*t)/(np.pi**5*t**2)
