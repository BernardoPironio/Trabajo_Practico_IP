import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])

#### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        ''' Tablero bien formado con todas las figuras colocadas.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

    def test_tablero_8x7_invalido(self):
        ''' Tablero mal formado, menos columnas que las requeridas.'''
        t = leer_tablero([
            'hcdmedc', #7
            'rrrrrrr', #6
            '-------', #5
            '-------', #4
            '-------', #3
            '-------', #2
            'RRRRRRR', #1
            'HCDMEDC', #0
            #01234567
            ])
        self.assertFalse(tablero_bien_formado(t))

    def test_tablero_7x8_invalido(self):
        ''' Tablero mal formado, menos filas que las requeridas.'''
        t = leer_tablero([
            'rrrrrrrr', #6
            '--------', #5
            '--------', #4
            '--------', #3
            '--------', #2
            'RRRRRRRR', #1
            'HCDMEDCH', #0
            #01234567 
        ])
        self.assertFalse(tablero_bien_formado(t))

    def test_tablero_8x8_vacio(self):
        ''' Tablero bien formado, pero sin ninguna pieza colocada.'''
        t = tablero_8x8_vacio()
        self.assertTrue(tablero_bien_formado(t))

    def test_tablero_9x10_invalido(self):
        ''' Tablero mal formado, mas filas y columas que las requeridas.'''
        t = leer_tablero([
            'rrrrrrrr', #6
            '--------', #5
            '--------', #4
            '--------', #3
            '--------', #2
            'RRRRRRRR', #1
            'HCDMEDCH', #0
            #01234567 
        ])
        self.assertFalse(tablero_bien_formado(t))

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        ''' Posicion en el tablero.'''
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))

    def test_posicion_fila_mal(self):
        ''' Posicion fuera del tablero (debido a la fila).'''
        self.assertFalse(posicion_en_tablero(Posicion(8,2)))

    def test_posicion_columna_mal(self):
        ''' Posicion fuera del tablero (debido a la columna).'''
        self.assertFalse(posicion_en_tablero(Posicion(5,8)))

    def test_posicion_esquina_superior_derecha(self):
        ''' Posicion dentro del tablero en el limite superior derecho.'''
        self.assertTrue(posicion_en_tablero(Posicion(7,7)))

    def test_posicion_esquina_inferior_izquierda(self):
        ''' Posicion dentro del tablero en el limite inferior izquierdo.'''
        self.assertTrue(posicion_en_tablero(Posicion(0,0)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        ''' Mover a secas bien formado'''
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))

    def test_movimiento_invalido_mover_a_secas(self):
        ''' Mover a secas mal formado (cantidad de pasos incorrecta).'''
        self.assertFalse(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0,1), [NORTE,SUR])))

    def test_movimiento_invalido_arrastrar(self):
        ''' Arrastrar mal formado (cantidad de pasos incorrecta).'''    
        self.assertFalse(movimiento_bien_formado(Movimiento(ARRASTRAR, Posicion(0,1), [NORTE])))

    def test_movimiento_invalido_empujar(self):
        ''' Empujar mal formado (cantidad de pasos incorrecta).'''    
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(0,1), [NORTE])))

    def test_posicion_invalida(self):
        ''' Movimiento mal formado (posicion no valida).'''
        self.assertFalse(movimiento_bien_formado(Movimiento(EMPUJAR, Posicion(-1,1), [NORTE])))

    def test_movimiento_empujar_ok(self):
        ''' Empujar bien formado.'''
        self.assertTrue(movimiento_bien_formado(Movimiento(EMPUJAR,Posicion(4,4),[NORTE,ESTE])))

    def test_movimiento_arrastrar_ok(self):
            ''' Arrastrar bien formado.'''
            self.assertTrue(movimiento_bien_formado(Movimiento(ARRASTRAR,Posicion(4,4),[NORTE,ESTE])))

class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        ''' Juego bien formado.'''
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

    def test_juego_invalido_tablero_mal_formado(self):
        ''' Juego mal formado debido a que el tablero esta mal formado.'''
        j = Juego(leer_tablero([
            'rrrrrrr', #6
            '-------', #5
            '-------', #4
            '-------', #3
            '-------', #2
            'RRRRRRR', #1
            'HCDMEDC', #0
            #01234567
            ]), DORADO, 0)
        self.assertFalse(juego_bien_formado(j))

    def  test_juego_invalido_pasos_invalidos(self):
        ''' Juego mal formado debido a que la cantidad maxima de pasos se supera.'''
        j = Juego(tablero_8x8_inicial_ejemplo(),PLATEADO,4)
        self.assertFalse(juego_bien_formado(j))

    def test_juego_ok_pasos_justos(self):
        ''' Juego bien formado, cantidad de pasos justa y turno del color dorado.'''
        j = Juego(tablero_8x8_inicial_ejemplo(),DORADO,3)
        self.assertTrue(juego_bien_formado(j))

#### Ejercicio 2

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        ''' Posicion vecina hacia el norte.'''
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))

    def test_vecina_al_sur(self):
        ''' Posicion vecina hacia el sur.'''
        self.assertEqual(posicion_vecina_hacia(Posicion(1, 0), SUR), Posicion(0, 0))

    def test_vecina_al_este(self):
        ''' Posicion vecina hacia el este.'''
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), ESTE), Posicion(0, 1))

    def test_vecina_al_oeste(self):
        ''' Posicion vecina hacia el oeste.'''
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 1), OESTE), Posicion(0, 0))

    def test_vecina_afuera(self):
        ''' Posicion vecina hacia el norte, fuera del tablero (el requiere lo permite).'''
        self.assertEqual(posicion_vecina_hacia(Posicion(7,7),NORTE),Posicion(8,7))
    
class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        ''' Son posiciones vecinas y la segunda esta al norte de la primera.'''
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

    def test_vecinas_abajo(self):
        ''' Son posiciones vecinas y la segunda esta al sur de la primera.'''
        self.assertTrue(son_posiciones_vecinas(Posicion(1, 0), Posicion(0, 0)))
    
    def test_vecinas_derecha(self):
        ''' Son posiciones vecinas y la segunda esta al este de la primera.'''
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(0, 1)))
    
    def test_vecinas_izquierda(self):
        ''' Son posiciones vecinas y la segunda esta al oeste de la primera.'''
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 1), Posicion(0, 0)))
        
    def test_vecinas_False(self):
        ''' No son vecinas(separadas por dos casillas.'''
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(2, 0)))

    def test_no_son_vecinas_en_diagonal(self):
        ''' No son vecinas, se tocan pero en la diagonal.'''
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 1)))

    def test_misma_posicion(self):
        ''' No son vecinas, son la misma posicion.'''
        self.assertFalse(son_posiciones_vecinas(Posicion(0, 0), Posicion(0, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        ''' Casilla en posicion con pieza caballo dorado.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

    def test_casilla_en_posicion_plateado(self):
        ''' Casilla con pieza elefante plateado'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(7, 4)), Pieza(ELEFANTE, PLATEADO))

    def test_casilla_en_posicion_vacía(self):
        ''' Casilla sin pieza.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(2, 0)), VACIA)
    
class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        ''' Hay casilla vacia en la posicion.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

    def test_casilla_no_vacia(self):
            ''' No hay casilla vacia.'''
            t = tablero_8x8_inicial_ejemplo()
            self.assertFalse(hay_casilla_vacia(t, Posicion(0, 0)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        ''' Hay pieza y es del color pasado como parametro.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

    def test_hay_pieza_de_color_False(self):
        ''' Hay pieza y pero no es del color pasado como parametro.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(1, 4), PLATEADO))

    def test_hay_pieza_de_color_Vacía(self):
        ''' No hay pieza.'''
        t = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(2, 0), DORADO))


#### Ejercicio 3

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))

    def test_no_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(1, 3), NORTE))

    def test_no_hay_casilla_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(7, 3), NORTE))

class test_hay_pieza(unittest.TestCase):

    def test_hay_pieza_dorada(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza(t,Posicion(0,0)))

    def test_hay_pieza_plateada(self):

        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza(t,Posicion(7,0)))

    def test_no_hay_pieza(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertFalse(hay_pieza(t,Posicion(0,4)))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

    # hay alguna amiga
    # hay alguna enemiga
    # hay alguna amiga y otra enemiga
    # no hay pieza

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))

    # mira hacia afuera del tablero
    # una de la misma fuerza
    # una si es mayor
    # una que es aimga y mas debil


class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

    # hay 
    # no hay
    # hay pero es amiga

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))

        # no hay pieza congelada porque hay amiga vecina
        # no hay piesza congelada porque la enemiga es mas debil
        # no hay pieza congelada porque no tiene vecinas

#### Ejercicio 4

class test_puede_realizar_movimiento(unittest.TestCase):

    # MOVER A SECAS

    def test_mover_a_secas_ok(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
    
    def test_mover_a_secas_conejor_sur_varios_pasos(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(5,6), [SUR,SUR,SUR])
        self.assertTrue(puede_realizar_movimiento(j,m))

    # despu hay que chequar
    def test_mover_a_secas_invalido_por_pieza_con_color_incorrecto(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(0,2), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))
        #st_mover_a_secas_invalido_por
    def test_mover_a_secas_invalido_por_posicion_ocupada_por_enemigo(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(0,1), [ESTE])
        self.assertFalse(puede_realizar_movimiento(j,m))

    def test_mover_a_secas_invalido_no_hay_piez(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(1,1), [ESTE])
        self.assertFalse(puede_realizar_movimiento(j,m))

    def test_mover_a_secas_invalido_pieza_congelada(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMde--', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(4,3), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))

    def test_mover_a_secas_invalido_conejo_plateado_norte(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(6,5), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))

    def test_mover_a_secas_invalido_fuera_del_tablero(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,0)
        m = Movimiento(MOVER_A_SECAS,Posicion(0,1), [SUR])
        self.assertFalse(puede_realizar_movimiento(j,m))

    def test_mover_a_secas_sin_pasos_suficientes(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t,PLATEADO,3)
        m = Movimiento(MOVER_A_SECAS,Posicion(0,1), [NORTE,NORTE])
        self.assertFalse(puede_realizar_movimiento(j,m))

    # ARRASTRAR
         
#### Ejercicio 5

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

#### Ejercicio 6

class test_realizar_movimiento(unittest.TestCase):
 
    def test_mover_a_secas_6(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

#### Ejercicio 7

class test_ganador_del_juego(unittest.TestCase):

    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero([
              'rr----Rr', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '-rrrr---', #2
              '-H---DCC', #1
              'R-----RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

