#Taller 2 - Cuadrante del punto
X = int(input())
Y = int(input())
if X == 0 and Y == 0:
    print('El punto ({}, {}) se encuentra en el origen'.format(X,Y))
elif X == 0:
    print('El punto ({}, {}) se encuentra sobre el eje y'.format(X,Y))
elif Y == 0:
    print('El punto ({}, {}) se encuentra sobre el eje x'.format(X,Y))
elif X<0 and Y<0:
    print('El punto ({}, {}) se encuentra en el cuadrante III'.format(X,Y))
elif X>0 and Y>0:
    print('El punto ({}, {}) se encuentra en el cuadrante I'.format(X,Y))
elif X<0 and Y>0:
    print('El punto ({}, {}) se encuentra en el cuadrante II'.format(X,Y))
elif X>0 and Y<0:
    print('El punto ({}, {}) se encuentra en el cuadrante IV'.format(X,Y))