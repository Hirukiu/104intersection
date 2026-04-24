def discriminant_quadratic(a,b,c):
    """
    takes three numbers a, b and c and returns b² + 4ac : the 
    discriminant of the quadratic equation ax² + bx + c = 0
    """

    return ((b * b) + (4 * a *c))

def nb_solutions_quadratic(a, b, c):
    """
    that takes three numbers a, b and c and returns the
    number of solutions to the quadratic equation ax² + bx + c = 0
    """
    

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