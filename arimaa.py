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
    Determina si la casilla en la direccion d, respecto de la posicion pos esta vacia.

    PRE: 
        tablero_bien_formado(t) ∧ posición_en_tablero(pos).
    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): Posicion a verificar si existen casillas vacias en alguna direccion.
        d (Dirección): La direccion a verificar.
    Returns:
        True si la casilla en la direccion d, respecto de la posicion pos, esta vacia; False de lo contrario.
    """
    res: bool = False
    pos_prima: Posicion = posicion_vecina_hacia(pos, d)
    if posicion_en_tablero(pos_prima):
        res: bool = hay_casilla_vacia(t, pos_prima)
    return res

# Esta funcion aux la vamos a dejar porque se puede utilizar en muchos ejericios.
def hay_pieza(t: Tablero, pos: Posicion) -> bool:
    """
    Vamos a determinar si en la posicion pos del tablero t hay una figura, sea esta DORADA o PLATEADA.

    PRE: 
        tablero_bien_formado(t) ∧ posición_en_tablero(pos).

    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): Posicion a verificar si hay pieza.

    Returns:
        True si es que hay una figura dorada o plateada.
        False de lo contrario.
    """
    res: bool = True
    if hay_casilla_vacia(t,pos):
        res: bool = False

    return res

def hay_pieza_amiga_vecina(t: Tablero, pos: Posicion) -> bool:
    """
    Determina si la pieza ubicada en la posicion pos tiene al menos una pieza de su mismo color
    en alguna casilla adyacente ortogonal (norte, sur, este u oeste).

    PRE: 
        tablero_bien_formado(t) ∧ posición_en_tablero(pos) ∧ hay_pieza(t, pos).
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
            res: bool = True

    return res

def hay_pieza_enemiga_mas_debil_hacia(t: Tablero, pos: Posicion, d: Direccion) -> bool:
    """
    Determina si en la direccion d adyacente a la posicion pos se encuentra una pieza enemiga 
    cuya fuerza sea estrictamente menor que la de la pieza en pos.

    PRE: 
        tablero_bien_formado(t) ∧ posición_en_tablero(pos) ∧ hay_pieza(t, pos).
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

        res: bool = es_enemigo and es_mas_debil

    return res

def hay_pieza_enemiga_mas_fuerte_vecina(t: Tablero, pos: Posicion) -> bool:
    """
    Determina si la pieza en pos tiene alguna pieza enemiga adyacente con fuerza estrictamente mayor.

    PRE: 
        tablero_bien_formado(t) ∧ posición_en_tablero(pos) ∧ hay_pieza(t, pos).
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
    Determina si la pieza en pos se encuentra congelada.
    Decimos que una pieza esta congelada si existe una pieza en pos, tiene al menos una pieza enemiga
    mas fuerte vecina y no tiene ninguna pieza amiga vecina.

    PRE:
        tablero_bien_formado(t) ∧ posición_en_tablero(pos).
    ARGS:
        t (Tablero): El tablero actual.
        pos (Posición): La posición a verificar.
    Returns:
        True si la pieza esta congelada; False de lo contrario.
    """
    res: bool = False

    if hay_pieza(t, pos) and hay_pieza_enemiga_mas_fuerte_vecina(t, pos) and not hay_pieza_amiga_vecina(t, pos):
        res: bool = True

    return res

#### Ejercicio 4

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    """
    Determina si se puede realizar un movimiento.
    Decimos que se puede realizar un movimiento si el color de pieza a mover coincide con el turno del juego,
    la pieza a mover no esta congelada, la direccion de movimiento esta habilitada y la cantidad de pasos consumidos
    sumada a los pasos que se quieren dar no supera el maximo de pasos. Por ultimo se pide que la accion especifica 
    se pueda realizar       

    PRE: 
        juego_bien_formado(j) ∧ movimeinto_bien_formado(m).
    ARGS:
        j (Juego): El juego actual.
        m (Movimiento): El movimiento a realizar.
    Returns:
        True si el movimiento se puede realizar; False de lo contrario.
    """
    res: bool = True
    if (hay_casilla_vacia(j.tablero,m.origen)                           # No hay vacia
        or (casilla_en_posicion(j.tablero, m.origen).color != j.turno)  # Color pieza == turno 
        or hay_pieza_congelada(j.tablero,m.origen)                      # No esta congelada
        or len(m.pasos) + j.pasos_consumidos > 4):                      # Pasos <= MAX_PASOS
        return False                                                    # Porque no interesa que evalúe lo que sigue y no funciona si es vacía

    if casilla_en_posicion(j.tablero,m.origen).figura == CONEJO:       # Si es conejo que se mueva solo para adelante
        if (casilla_en_posicion(j.tablero,m.origen).color == DORADO      # Conejo dorado no al sur
            and m.pasos[0] == SUR):
            res: bool = False                           
        if (casilla_en_posicion(j.tablero,m.origen).color == PLATEADO    # Conejo plateado no al norte
            and m.pasos[0] == NORTE):
            res: bool = False

    # Condiciones sobre las distintas acciones
    if m.accion == MOVER_A_SECAS:
        res: bool = res and hay_casilla_vacia_hacia(j.tablero,m.origen,m.pasos[0])

    if m.accion == ARRASTRAR:
        res: bool = res and (hay_casilla_vacia_hacia(j.tablero,m.origen,m.pasos[0])
                    and hay_pieza_enemiga_mas_debil_hacia(j.tablero, m.origen, opuesta(m.pasos[1])))
        
    if m.accion == EMPUJAR:
        res:bool = res and (hay_pieza_enemiga_mas_debil_hacia(j.tablero,m.origen,m.pasos[0])
                    and hay_casilla_vacia_hacia(j.tablero,posicion_vecina_hacia(m.origen,m.pasos[0]),m.pasos[1]))

    return res 

#### Ejercicio 5

def copiar_tablero (t: Tablero) -> Tablero:
    copia: Tablero = []
    for elemento in t:
        copia.append(elemento.copy())
    return copia

def sacarPieza (t: Tablero, pos: Posicion) -> Tablero:
    t1: Tablero = copiar_tablero(t)
    t1[pos.fila][pos.columna] = VACIA
    return t1

def activar_una_trampa (t: Tablero, pos: Posicion) -> Tablero:
    t1: Tablero = copiar_tablero(t)
    if casilla_en_posicion(t1,pos) == VACIA:
        pass
    elif hay_pieza_amiga_vecina (t1,pos):
        pass
    elif not hay_pieza_amiga_vecina (t1,pos):
        t1 = sacarPieza (t1,pos)
    return t1

def activar_trampas(t : Tablero) -> Tablero:
    """
    Activa todas las trampas del tablero t y devuelve un tablero con todas las trampas activadas.
    Las posiciones trampa son: [(2, 2), (2, 5), (5, 2), (5, 5)]
    Si al terminar un movimiento una pieza está en una de las casillas trampa y no tiene piezas amigas vecinas, esa pieza se saca del tablero.

    PRE: 
        tablero_bien_formado(t).
    ARGS:
        t (tablero): Es el tablero al que le voy a activar las trampas.
    Returns:
        Un nuevo tablero con todas las trampas activadas.
    """
    t1: Tablero = copiar_tablero(t)
    for trampa in POSICIONES_TRAMPA:
        t1= activar_una_trampa (t1,trampa)
    return t1

#### Ejercicio 6

def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    """
    Realiza el movimiento m sobre el juego j.
    Decimos que ejecuta un movimiento si esque aplica los desplazamientos de las piezas según la acción del movimiento, elimina las piezas caídas en trampas y gestiona los pasos consumidos junto con el cambio de turno.
    PRE: juego_bien_formado(j) ∧ movimiento_bien_formado(m) ∧ puede_realizar_movimiento(j, m)
    ARGS:
        j (Juego): El juego actual.
        m (Movimiento): El movimiento a realizar.
    Returns:
        Juego: El juego actualizado después del movimiento.
    """
    # copio tablero
    tablero_nuevo: Tablero = copiar_tablero(j.tablero)
    origen: Posicion = m.origen

   
    # muevo a secas
    if m.accion == MOVER_A_SECAS:
        destino: Posicion = posicion_vecina_hacia(origen, m.pasos[0])
        pieza: Casilla = casilla_en_posicion(tablero_nuevo, origen)
        tablero_nuevo[origen.fila][origen.columna] = VACIA
        tablero_nuevo[destino.fila][destino.columna] = pieza

    # arrastro
    elif m.accion == ARRASTRAR:
        # moves a la casilla libre
        destino_propio: Posicion = posicion_vecina_hacia(origen, m.pasos[0])
        pieza_propia: Casilla = casilla_en_posicion(tablero_nuevo, origen)
        tablero_nuevo[origen.fila][origen.columna] = VACIA
        tablero_nuevo[destino_propio.fila][destino_propio.columna] = pieza_propia

        # muevo la pieza contraria a la pos q libero
        pos_enemigo: Posicion = posicion_vecina_hacia(origen, opuesta(m.pasos[1]))
        pieza_enemiga: Casilla = casilla_en_posicion(tablero_nuevo, pos_enemigo)
        tablero_nuevo[pos_enemigo.fila][pos_enemigo.columna] = VACIA
        tablero_nuevo[origen.fila][origen.columna] = pieza_enemiga

    # empujo
    elif m.accion == EMPUJAR:
        # pieza contraria a casilla vacia
        pos_enemigo: Posicion = posicion_vecina_hacia(origen, m.pasos[0])
        destino_enemigo: Posicion = posicion_vecina_hacia(pos_enemigo, m.pasos[1])
        pieza_enemiga: Casilla = casilla_en_posicion(tablero_nuevo, pos_enemigo)
        tablero_nuevo[pos_enemigo.fila][pos_enemigo.columna] = VACIA
        tablero_nuevo[destino_enemigo.fila][destino_enemigo.columna] = pieza_enemiga

        # muevo mi pieza a donde estaba la otra contraria 
        pieza_propia: Casilla = casilla_en_posicion(tablero_nuevo, origen)
        tablero_nuevo[origen.fila][origen.columna] = VACIA
        tablero_nuevo[pos_enemigo.fila][pos_enemigo.columna] = pieza_propia

    # activo trampas
    tablero_final: Tablero = activar_trampas(tablero_nuevo)

    # pasos + turno
    pasos_totales: int = j.pasos_consumidos + len(m.pasos)

    if pasos_totales == MAX_PASOS:
        nuevo_turno: Color = oponente(j.turno)
        nuevos_pasos: int = 0
    else:
        nuevo_turno: Color = j.turno
        nuevos_pasos: int = pasos_totales

    return Juego(tablero_final, nuevo_turno, nuevos_pasos)

#### Ejercicio 7

# Función auxiliar para determinar si hay conejos en el tablero del color col
def hayConejoEnTablero (j: Juego, col: Color) -> bool:
    for fila in j.tablero:
        for casilla in fila:
            if casilla != VACIA and casilla.figura == CONEJO and casilla.color == col:
                return True
    return False

# Función auxiliar para determinar si hay conejos de color col en la fila inicial del oponente

def hayConejoEnFilaInicialOponente (j: Juego, col: Color) -> bool:
    res: bool = False
    if col == DORADO:
        for casilla in j.tablero[7]:
            if casilla != VACIA and casilla.figura == CONEJO and casilla.color == col:
                res = True
        
    elif col == PLATEADO:
        for casilla in j.tablero[0]:
            if casilla != VACIA and casilla.figura == CONEJO and casilla.color == col:
                res = True
    return res

# Función auxiliar que determina si tiene las condiciones de ganar
def reuneCondicionesDeGanar (j: Juego, col: Color) -> bool:
    return hayConejoEnFilaInicialOponente (j, col) or not hayConejoEnTablero (j, oponente(col))

def hay_ganador_determinado(j : Juego) -> bool:
    """
    Determina si hay un ganador del juego.
    
    Decimos que tiene condiciones de ganar si cumple alguna de estas dos condiciones:
        - Hay un conejo de su color en la fila inicial del oponente.
        - No hay conejos en el tablero del color del oponente
    
    Un jugador gana en alguno de estos dos casos:
        - Si es el turno de su oponente: gana si tiene las condiciones de ganar.
        - Si es su turno: gana si tiene las condiciones de ganar y su oponente no las tiene.

    PRE: 
        juegoBienFormado (j)
    ARGS:
        j (Juego): El juego a partir del cual se va a determinar si hay un ganador.
    Returns:
        True si hay un ganador del juego.
        False en caso contrario.
    """
    res: bool = False
    if j.pasos_consumidos == 0 and reuneCondicionesDeGanar(j, oponente(j.turno)):
        res = True
    elif j.pasos_consumidos == 0 and reuneCondicionesDeGanar (j, j.turno) and not reuneCondicionesDeGanar(j,oponente(j.turno)):
        res = True
    return res

def ganador_del_juego(j : Juego) -> Color:
    """
    Devuelve el color del ganador del juego.

    PRE: 
        juegoBienFormado (j) ∧ hayGanadorDeterminado (j) 
    ARGS:
        j (Juego): El juego a partir del cual ganó un jugador.
    Returns:
        El color del ganador del juego.
    """

    res: Color = oponente(j.turno)
    if not reuneCondicionesDeGanar(j, oponente(j.turno)):
        res = j.turno
    return res
