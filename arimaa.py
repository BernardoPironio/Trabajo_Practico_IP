from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    ''' 
    Determina si el tablero t esta bien formado.
    Decimos que un tablero t es valido si tiene un ancho y largo de 7 casillas.

    ARGS: 
        t (Tablero): El tablero que se desea verificar.
    Returns: 
        True si el tablero esta bien formado; False de lo contrario.
    '''
    validez: bool = True 
    for fila in t: 
        if len(fila) != ANCHO:
            validez: bool = False
    return validez and len(t) == ALTO

def posicion_en_tablero(pos : Posicion) -> bool:
    ''' 
    Determina si la posicion pos pertenece al tablero. 

    ARGS: 
        pos (Posicion): La posicion que se desea verificar.
    Returns: 
        True si la posicion esta en el tablero; False de lo contrario.
    '''
    return (0 <= pos.fila < ALTO) and (0 <= pos.columna < ANCHO)
    
def movimiento_bien_formado(m : Movimiento) -> bool:
    ''' 
    Determina si el movimiento m esta bien formado.
    Decimos que le movimiento esta bien formado si la cantidad de pasos corresponde al movimiento por hacer.

    ARGS: 
        m (Movimiento): El movimiento que se desea verificar.
    Returns: 
        True si es un movimiento valido; False de lo contrario.
    '''
    if m.accion == MOVER_A_SECAS:
        pasos_correctos: bool = len(m.pasos) == 1 
    elif m.accion in (ARRASTRAR,EMPUJAR):
        pasos_correctos: bool = len(m.pasos) == 2
    else:
        pasos_correctos: bool = False
    return pasos_correctos and posicion_en_tablero(m.origen)

def juego_bien_formado(j : Juego) -> bool:
    ''' 
    Determina si el juego j esta bien formado. 
    Decimos que un juego esta bien formado si el tablero del juego esta bien formado y la cantidad de pasos consumidos es mayor a cero y no supera el maximo.
    
    ARGS: 
        j (Juego): El juego que se desea verificar.
    Returns: 
        True si el juego esta bien formado; False de lo contrario.
    '''
    return tablero_bien_formado(j.tablero) and (0 <= j.pasos_consumidos < MAX_PASOS)

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    Devuelve el valor de la  posición en direccion d con respecto a la posicion.

    ARGS: 
        pos (Posición): La posición original. 
        d (Dirección): La dirección hacia la que se mueve.
    Returns: 
        La posición vecina de la posición original en la dirección elegida.
    """
    res: Posicion = Posicion(pos.fila, pos.columna)
    if d == NORTE:
        res = Posicion(pos.fila + 1,pos.columna)
    elif d == SUR:
        res = Posicion(pos.fila - 1,pos.columna)
    elif d == ESTE:
        res = Posicion(pos.fila,pos.columna + 1)
    elif d == OESTE:
        res = Posicion(pos.fila,pos.columna - 1) 

    return res

def casilla_en_posicion(t: Tablero, p: Posicion) -> Casilla:
    """
    Devuelve la casilla del tablero t que está ubicada en la posición pos.

    PRE: 
        tableroBienFormado (t) ∧ posiciónEnTablero(pos).
    ARGS: 
        t (Tablero): El tablero que se desea verificar.
        p (Posición): La posición original.
    Returns: 
        VACÍA si la casilla en esa posición es un espacio vacío o una pieza si está ocupada.
    """
    res: Casilla = t[p.fila][p.columna]
    return res

def hay_casilla_vacia(t: Tablero, pos: Posicion) -> bool:
    """
    Determina si la casilla que está en la posición pos está vacía.

    PRE: 
        tableroBienFormado (t) ∧ posiciónEnTablero(pos).
    ARGS: 
        t (Tablero): El tablero que se desea verificar.
        pos (Posición): La posición original.
    Returns:
        True si la casilla en esa posición es un espacio vacío; False de lo contrario.
    """
    return casilla_en_posicion(t,pos) == VACIA

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
    Determina si la casilla que está en la posición pos tiene una figura de color col.

    PRE: 
        tableroBienFormado (t) ∧ posiciónEnTablero(pos).
    ARGS: 
        t (Tablero): El tablero que se desea verificar.
        pos (Posición): La posición original.
        col (Color): El color de la figura que está en casilla de esa posición.
    Returns:
        True si la casilla en esa posición tiene una figura del color col y False si está vacía o es de otro color que col.
    """
    casilla: Casilla = casilla_en_posicion(t,pos)
    if casilla == VACIA:
        res: bool = False
    else:
        res: bool = casilla.color == col
    return res

#### Ejercicio 3

def hay_casilla_vacia_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """
    Vamos a determinar si la casilla en la direccion d, respecto de la posicion pos es vacia o no.

    PRE: tablero_bien_formado(t) ∧ posición_en_tablero(pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): Posicion a verificar si existen casillas vacias en alguna direccion.
        d (Dirección): La direccion a verificar.

    Returns:
        True si la casilla en la direccion d, respecto de la posicion pos, esta vacia.
        False de lo contrario.
    """
    res: bool = False
    pos_prima: Posicion = posicion_vecina_hacia(pos, d)
    if posicion_en_tablero(pos_prima):
        res = hay_casilla_vacia(t, pos_prima)
    return res

def hay_pieza(t: Tablero, pos: Posicion) -> bool:
    """
    Vamos a determinar si en la posicion pos del tablero t hay una figura, sea esta DORADA o PLATEADA.

    PRE: tablero_bien_formado(t) ∧ posición_en_tablero(pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): Posicion a verificar si hay pieza.

    Returns:
        True si es que hay una figura dorada o plateada.
        False de lo contrario.
    """
    casilla: Casilla = casilla_en_posicion(t,pos)
    if hay_casilla_vacia(t,pos):
        return False
    return hay_figura_de_color(t, pos, casilla.figura, DORADO) or hay_figura_de_color(t, pos, casilla.figura,PLATEADO)


def hay_pieza_amiga_vecina(t: Tablero, pos: Posicion) -> bool:
    """
    Vamos a determinar si la pieza ubicada en la posicion pos tiene al menos una pieza de su mismo color
    en alguna casilla adyacente ortogonal (norte, sur, este u oeste).

    PRE: tablero_bien_formado(t) ∧ posición_en_tablero(pos) ∧ hay_pieza(t, pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): La posición de la pieza a evaluar.

    Returns:
        True si hay al menos una pieza amiga adyacente, False en caso contrario.
    """
    res: bool = False
    color_amigo: Color = casilla_en_posicion(t, pos).color

    for d in [NORTE, SUR, ESTE, OESTE]:
        pos_vecina: Posicion = posicion_vecina_hacia(pos, d)

        if posicion_en_tablero(pos_vecina) and hay_pieza_de_color(t, pos_vecina, color_amigo):
            res = True

    return res

def hay_pieza_enemiga_mas_debil_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """
    Vamos a determinar si en la direccion d adyacente a la posicion pos se encuentra una pieza enemiga
    cuya fuerza sea estrictamente menor que la de la pieza en pos.

    PRE: tablero_bien_formado(t) ∧ posición_en_tablero(pos) ∧ hay_pieza(t, pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): La posición de la pieza atacante/origen.
        d (Dirección): La dirección a verificar.

    Returns:
        True si hay una pieza enemiga adyacente mas debil en la direccion d;
        False en caso contrario.
    """
    res: bool = False
    pos_vecina: Posicion = posicion_vecina_hacia(pos, d)

    if posicion_en_tablero(pos_vecina) and not hay_casilla_vacia(t, pos_vecina):
        pieza_actual: Casilla = casilla_en_posicion(t, pos)
        pieza_vecina: Casilla = casilla_en_posicion(t, pos_vecina)

        es_enemigo: bool = pieza_vecina.color == oponente(pieza_actual.color)
        es_mas_debil: bool = fuerza(pieza_vecina.figura) < fuerza(pieza_actual.figura)

        res = es_enemigo and es_mas_debil

    return res

def hay_pieza_enemiga_mas_fuerte_vecina(t: Tablero, pos: Posicion) -> bool:
    """
    Vamos a determinar si la pieza en pos tiene alguna pieza enemiga adyacente con fuerza estrictamente mayor.

    PRE: tablero_bien_formado(t) ∧ posición_en_tablero(pos) ∧ hay_pieza(t, pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): La posición de la pieza a evaluar.

    Returns:
        True si hay al menos una pieza enemiga vecina mas fuerte;
        False en caso contrario.
    """
    res: bool = False
    pieza_actual: Casilla = casilla_en_posicion(t, pos)

    for d in [NORTE, SUR, ESTE, OESTE]:
        pos_vecina: Posicion = posicion_vecina_hacia(pos, d)

        if posicion_en_tablero(pos_vecina) and not hay_casilla_vacia(t, pos_vecina):
            pieza_vecina: Casilla = casilla_en_posicion(t, pos_vecina)

            es_enemigo: bool = pieza_vecina.color == oponente(pieza_actual.color)
            es_mas_fuerte: bool = fuerza(pieza_vecina.figura) > fuerza(pieza_actual.figura)

            if es_enemigo and es_mas_fuerte:
                res = True

    return res

def hay_pieza_congelada(t: Tablero, pos: Posicion) -> bool:
    """
    Vamos a determinar si la pieza en pos se encuentra congelada.

    Decimos que una pieza esta congelada si existe una pieza en pos, tiene al menos una pieza enemiga
    mas fuerte vecina y no tiene ninguna pieza amiga vecina.

    PRE: tablero_bien_formado(t) ∧ posición_en_tablero(pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): La posición a verificar.

    Returns:
        True si la pieza esta congelada; False de lo contrario.
    """
    res: bool = False

    if hay_pieza(t, pos) and hay_pieza_enemiga_mas_fuerte_vecina(t, pos) and not hay_pieza_amiga_vecina(t, pos):
        res = True

    return res

#### Ejercicio 4
def hay_figura_de_color(t: Tablero, pos: Posicion, f: Figura, col: Color):
    """
    Determina que si dado el tablero t, la posicion pos es una posicion en el tablero, no hay casilla vacia en la posicion pos, 
    la figura f coincide con la figura de esa posicion en el tablero y  el color col coincide con el color de esa posicio en ele tablero.

    PRE: tablero_bien_formado(t).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posicion): La posicion a cheaquar si hay una figura de cierto color.
        f (Figura): Tipo de figura a chequear si esta en la casilla.
        col (Color): Color a chequear si esta en la casilla.

    Returns:
        True si hay una figura f de color col en la casilla de la posicion pos(valida en el tablero); False de lo contrario.
    """    
    return(
        posicion_en_tablero(pos)
        and not hay_casilla_vacia(t,pos)
        and t[pos.fila][pos.columna].figura == f
        and t[pos.fila][pos.columna].color == col
    )

def direccion_de_movimiento_habilitada(t: Tablero, pos: Posicion, d: Direccion):
    """
    Vamos a determinar si la direccion esta habilitada.
    Decimos que la direccion esta habilitada si existe una figura f y un color col tales que hay una figura f de color col en la posicion pos y si es que esta figura es un conejo(dorado o plateado) entonces la direccion d sea distinta de NORTE o SUR.

    PRE: tablero_bien_formado(t).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posicion): Posicion de origen de la cual queremos ver si un movimiento es posible.

    Returns:
        True si la direccion de movimiento esta habilitada; False de lo contrario.
    """    
    res: bool = False
    for f in [ELEFANTE, CAMELLO, CABALLO, PERRO, GATO, CONEJO]:
        for col in [DORADO,PLATEADO]:
            if (
                hay_figura_de_color(t,pos,f,col)
                and not (f == CONEJO and col == DORADO and d == SUR)
                and not (f == CONEJO and col == PLATEADO and d == NORTE)
            ):
                res: bool = True
    return res

def puede_mover_a_secas(t: Tablero, pos: Posicion, d: Direccion):
    """
    Determina si puede moverse a secas en direccion d desde la posicion pos en el tablero t. Decimos que se puede mover a secas si la posicion a la que se quiere mover es una casilla vacia.
    PRE: tablero_bien_formado(t).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posicion): Posicion de origen de la cual queremos ver si un movimiento a secas es posible en la direccion d.
        d (Direccion): Direccion en la que nos queremos fijar si es posible hacer un movimiento a secas.

    Returns:
        True si el movimiento a secas se puede realizar; False de lo contrario.
    """    
    return hay_casilla_vacia_hacia(t,pos,d)

def puede_arrastrar(t: Tablero, pos: Posicion, d: Direccion, d_arrastre: Direccion):
    """
    Determina si puede arrastrar en direccion d desde la posicion pos en el tablero t. Decimos que puede arrastrar si en la direccion d hay una casilla vacia y en la direccion opuesta(d_arrastre) hay una pieza mas debil.
    PRE: tablero_bien_formado(t).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posicion): Posicion de origen de la cual queremos ver si es posible arrastrar.
        d (Direccion): Direccion en la que se mueve la pieza.
        d_arrastre (Direccion): Direccion de arrastre

    Returns:
        True si se puede arrastrar; False de lo contrario.
    """        
    return hay_casilla_vacia_hacia(t, pos, d) and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(d_arrastre))

def puede_empujar(t: Tablero, pos: Posicion, d: Direccion, d_empuje: Direccion):
    """
    Determina si se puede empujar desde la posicion pos en direccion d. Decimos que se puede empujar si en la direccion d hay una pieza enemiga de menor fuerza, y la casilla vecina a esa pieza en la direccion d_empuje esta vacia.
    PRE: tablero_bien_formado(t).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posicion): Posicion de origen de la cual queremos ver si es posible empujar.
        d (Direccion): Direccion en la que esta la pieza a empujar.
        d_arrastre (Direccion): Direccion a la que se empuja la pieza enemiga.

    Returns:
        True si se puede empujar; False de lo contrario.
    """ 
    return (
        hay_pieza_enemiga_mas_debil_hacia(t, pos, d)
        and hay_casilla_vacia_hacia(t, posicion_vecina_hacia(pos, d), d_empuje)
    )

def puede_realizar_accion(t: Tablero, m: Movimiento):
    """
    Determina si se puede realizar la accion. Decimos que se puede realizar la accion si la accion del movimiento m se puede realizar.
    ARGS:
        t (Tablero): El tablero actual.
        m (Movimiento): Movimiento al que se quiere ver si la accion se puede realizar.

    Returns:
        True si la accion del movimiento m se puede realziar; False de lo contrario.
    """ 
    res: bool = True
    if m.accion == MOVER_A_SECAS:
        res: bool = puede_mover_a_secas(t,m.origen,m.pasos[0])
    elif m.accion == ARRASTRAR:
        res: bool = puede_arrastrar(t,m.origen,m.pasos[0],m.pasos[1])
    elif m.accion == EMPUJAR:
        res: bool = puede_empujar(t,m.origen,m.pasos[0],m.pasos[1])
    return res

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    """
    Vamos a determinar si se puede realizar un movimiento.

    Decimos que podemos realizar un movimiento si: El color de la pieza del origen coincide con el turno del jugador con ese respectivo color.
                                                   La pieza no esta congelada.
                                                   La direccion de moviemiento esta habilitada.
                                                   La cantidad de pasos consumidos + los pasos a dar <= maximo de pasos.
                                                   Si se puede realizar la accion.
    PRE: juego_bien_formado(j) ∧ movimeinto_bien_formado(m).

    ARGS:
        j (Juego): El juego actual.
        m (Movimiento): El movimiento a realizar.

    Returns:
        True si el movimiento se puede realizar; False de lo contrario.
    """
    return (
        hay_pieza_de_color(j.tablero,m.origen,j.turno)
        and not hay_pieza_congelada(j.tablero,m.origen)
        and direccion_de_movimiento_habilitada(j.tablero,m.origen,m.pasos[0])
        and (j.pasos_consumidos + len(m.pasos) <= MAX_PASOS)
        and puede_realizar_accion(j.tablero,m)
    )
    
#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    raise Exception("No implementado")

#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    raise Exception("No implementado")

#### Ejercicio 7

def hay_ganador_determinado(j : Juego) -> bool:
    raise Exception("No implementado")

def ganador_del_juego(j : Juego) -> Color:
    raise Exception("No implementado")

