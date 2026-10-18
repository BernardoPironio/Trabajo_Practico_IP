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
    ''' Verifica que el tablero t sea válido. 
    PRE: True.
    ARGS: t (Tablero): El tablero que se desea verificar.
    Returns: True si el tablero es valido, False si no lo es.
    '''
    validez: bool = True 
    for fila in t: 
        if len(fila) != ANCHO:
            return False
    return validez and len(t) == ALTO

def posicion_en_tablero(pos : Posicion) -> bool:
    ''' Verifica que la posicion sea efectivamente una del tablero. 
        PRE: True.
        ARGS: pos (Posicion): La posicion que se desea verificar.
        Returns: True si es una posicion valida, False si no lo es.
        '''
    return (0 <= pos.fila <= ALTO) and (0 <= pos.columna <= ANCHO)
    
def movimiento_bien_formado(m : Movimiento) -> bool:
    ''' Verifica que el movimiento a realizar este bien formado. 
    PRE: True.
    ARGS: m (Movimiento): El movimiento que se desea verificar.
    Returns: True si es un movimiento valido, False si no lo es.
    '''
    if m.accion == MOVER_A_SECAS:
        pasos_correctos: bool = len(m.pasos) == 1 
    elif m.accion in (ARRASTRAR,EMPUJAR):
        pasos_correctos = len(m.pasos) == 2
    else:
        pasos_correctos = False
    return pasos_correctos and posicion_en_tablero(m.origen)

def juego_bien_formado(j : Juego) -> bool:
    ''' Verifica que juego este bien formado. 
    PRE: True.
    ARGS: j (Juego): El juego que se desea verificar.
    Returns: True si es un juego valido, False si no lo es.
    '''
    return tablero_bien_formado(j.tablero) and (0 <= j.pasos_consumidos <= MAX_PASOS)

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    Devuelve el valor de la nueva posición a partir de la dirección en la que se mueve la figura.
    PRE: True.
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
    PRE: tableroBienFormado (t) ∧ posiciónEnTablero(pos).
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
    Verifica si la casilla que está en la posición pos está vacía.
    PRE: tableroBienFormado (t) ∧ posiciónEnTablero(pos).
    ARGS: 
        t (Tablero): El tablero que se desea verificar.
        pos (Posición): La posición original.
    Returns:
        True si la casilla en esa posición es un espacio vacío y False si no lo es.
    """
    return casilla_en_posicion(t,pos) == VACIA

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
    Verifica si la casilla que está en la posición pos tiene una figura de color col.
    PRE: tableroBienFormado (t) ∧ posiciónEnTablero(pos).
    ARGS: 
        t (Tablero): El tablero que se desea verificar.
        pos (Posición): La posición original.
        col (Color): El color de la figura que está en casilla de esa posición.
    Returns:
            True si la casilla en esa posición tiene una figura del color col y False si está vacía o es de otro color que col.
        """
    casilla: Casilla = casilla_en_posicion (t,pos)
    return casilla != VACIA and casilla.color == col

#### Ejercicio 3

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    raise Exception("No implementado")

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    raise Exception("No implementado")

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    raise Exception("No implementado")

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

