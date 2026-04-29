import math



def discriminant_quadratic(a,b,c):
    """
    takes three numbers a, b and c and returns b² - 4ac : the
    discriminant of the quadratic equation ax² + bx + c = 0
    """

    return ((b * b) - (4 * a * c))

"""
    ax² + bx + c = 0

    x² + bx/a  = - c/a 

    x² + bx/a + (b/2a)² = - c/a + (b/2a)²

    (x + b/2a)² = -c/a + (b/2a)²

    x + b/2a = &(-c/a + (b/2a)²)

    x  = &(-c/a + b²/4a²) - b/2a

    -c/a + b²/4a² = (-4ca + b²)/4a²

    x  = &((-4ca + b²)/4a²) - b/2a

    x  = &(-4ca + b²)/2a - b/2a

    x  = &(-4ca + b²) - b / 2a
"""








def nb_solutions_quadratic(a, b, c):
    """
    that takes three numbers a, b and c and returns the
    number of solutions to the quadratic equation ax² + bx + c = 0
    returns -1 for infinite solutions
    """
    if a == 0 and b == 0 and c == 0:
        return -1
    discriminant = discriminant_quadratic(a,b,c)
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    elif discriminant < 0:
        return 0



def solutions_quadratic(a,b,c):
    """
    takes three numbers a, b and c and returns the
    solutions to the quadratic equation ax² + bx + c = 0
    returns -1 for infinite solutions, None for no solution
    """
    nb = nb_solutions_quadratic(a,b,c)
    discriminant = discriminant_quadratic(a,b,c)
    if nb == -1:
        return -1
    if not nb:
        return None
    elif nb == 1:
        return (-b / (2 * a))
    elif nb == 2:
        return ([ ( -b + math.sqrt(discriminant) ) / (2 * a) , ( -b - math.sqrt(discriminant) ) / ( 2 * a ) ])



def coordinates_Lt(Vx, Vy , Vz, Px, Py, Pz, t):
    """
    takes the definition of a line L (a point P and a vector P) 
    and a coefficient t and returns the coordinates of the point L(t)
    """

    xt = Px + (t * Vx)
    yt = Py + (t * Vy)
    zt = Pz + (t * Vz)

    coordinates = [xt, yt, zt]

    return coordinates


def quadratic_equation_sphere(Vx, Vy , Vz, Px, Py, Pz, R):
    """
    takes the definition of a line (a point P and a vector V )
    and a radius R and returns the coefficients a, b and c of the
    quadratic equation for the intersection of the line and the sphere
    """

    a = Vx ** 2 + Vy ** 2  + Vz ** 2
    b = 2 * (Px * Vx + Py * Vy + Pz * Vz)
    c = Px ** 2 + Py ** 2 + Pz ** 2 - R ** 2

    return solutions_quadratic(a,b,c)

"""

Sphere:

(Px + tVx)² + (Py + tVy)² + (Pz + tVz)² = R²

(Px² + 2(Px * tVx) + tVx²) + (Py² + 2(Py * tVy) + tVy²) + (Pz² + 2(Pz * tVz) + tVz²) = R²

Px² + 2(Px * tVx) + (t² * Vx²) + Py² + 2(Py * t2Vy) + (t² * Vy²) + Pz² + 2(Pz * tVz) + (t² * Vz²)

Px² + Py² + Pz² + 2(Px * tVx) + 2(Py * t2Vy) + 2(Pz * tVz) + (t² * Vz²) + (t² * Vx²) + (t² * Vy²)

(Px² + Py² + Pz²) + 2t((Px * Vx) + (Py * Vy) + (Pz * Vz)) + t²(Vz² + Vx² + Vy²) = R²

-R² + (Px² + Py² + Pz²) + 2t((Px * Vx) + (Py * Vy) + (Pz * Vz)) + t²(Vz² + Vx² + Vy²) = 0

at² + bt + c = 0

avec :
    a = Vx² + Vy² + Vz²
    b = 2(Px*Vx + Py*Vy + Pz*Vz)
    c = Px² + Py² + Pz² - r²
"""



def quadratic_equation_Cylinder(Vx, Vy , Vz, Px, Py, Pz, R):
    """
    takes the definition of a line (a point P and a vector V )
    and a radius R and returns the coefficients a, b and c of the
    quadratic equation for the intersection of the line and the Cylinder
    """

    a = Vx ** 2 + Vy ** 2
    b = 2 * (Px * Vx + Py * Vy)
    c = Px ** 2 + Py ** 2 - R ** 2
    
    return solutions_quadratic(a,b,c)
"""
Cylinder:

(Px + tVx)² + (Py + tVy)² = R²

(Px² + Py²) + 2t(Px * Vx * Py * tVy) + t²(Vy² + Vx²) = R²

= 0

avec :
    a = Vx² + Vy²
    b = 2(Px*Vx + Py*Vy)
    c = Px² + Py² - R²

"""




def quadratic_equation_cone(Vx, Vy , Vz, Px, Py, Pz, A):
    """
    takes the definition of a line (a point P and a vector V )
    and a radius R and returns the coefficients a, b and c of the
    quadratic equation for the intersection of the line and the cone
    """

    a = (Vx ** 2) + (Vy ** 2 )- (math.tan(A) ** 2)  * (Vz ** 2)
    b = 2 * (Px * Vx + Py * Vy - (math.tan(A) ** 2) * Pz * Vz)
    c = (Px ** 2) + (Py ** 2) - (math.tan(A) ** 2) * (Pz ** 2)

    return solutions_quadratic(a,b,c)

"""
Cone:

x² + y² = (tan(O))² * z²

(Px + tVx)² + (Py + tVy)² = (tan(O))² * (Pz + tVz)²

(Px² + Py²) + 2t(Px * Vx * Py * tVy) + t²(Vy² + Vx²)  = (tan(O))² * (Pz + tVz)²

(Px² + Py²) + 2t(Px * Vx * Py * tVy) + t²(Vy² + Vx²)  = tan²(O) * (Pz² + 2t(Pz*Vz) + t²Vz²)

((Px² + Py²) - tan²(O) * Pz²) + (2t(Px * Vx * Py * tVy) - (Pz*Vz) * tan²(O)) + (t²(Vy² + Vx²) - Vz² * tan²(O))

avec :
    a = Vx² + Vy² - tan²(O) * Vz²
    b = 2(Px * Vx + Py * Vy - tan²(O) * Pz * Vz)
    c = Px² + Py² - tan²(O) * Pz²

"""

