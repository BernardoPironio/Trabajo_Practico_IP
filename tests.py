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
        ''' Hay casilla vacia hacia el norte.'''
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

    def test_hay_casilla_vacia_hacia_sur(self):
        ''' Hay casilla vacia hacia el sur.'''
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(7, 7), SUR))

    def test_hay_casilla_vacia_hacia_este(self):
        ''' Hay casilla vacia hacia el este.'''
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(7, 1), ESTE))

    def test_hay_casilla_vacia_hacia_oeste(self):
        ''' Hay casilla vacia hacia el oeste.'''
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
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(7, 1), OESTE))

    def test_no_hay_casilla_vacia_hacia(self):
        ''' No hay casilla vacia hacia el norte.'''
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

    def test_casilla_vacia_hacia_fuera_del_tablero(self):
        ''' No hay casilla vacia hacia cierta direccion porque sale del tablero (permitido por el requiere).'''
        
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
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(7, 7), NORTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina(self):
        ''' Hay pieza amiga vecina.'''
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

    def test_no_hay_pieza_amiga_vecina(self):
        ''' Hay pieza vecina pero es enemiga.'''
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
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(4, 0)))

    def test_hay_pieza_amiga_y_enemiga_vecinas(self):
        ''' Hay pieza amiga vecina y tambien pieza enemiga vecina.'''
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
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(7, 3)))

    def test_hay_pieza_vecina(self):
        ''' No hay piezas vecinas.'''
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-R-c-', #1
              're---r--', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_amiga_vecina(t, Posicion(0, 5)))

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        ''' Hay pieza enemiga mas debil hacia el oeste.'''
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

    def test_hay_pieza_enemiga_misma_fuerza(self):
        ''' Hay pieza enemiga con la misma fuerza hacia el este.'''
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhCc-', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(6, 5), ESTE))

    def test_hay_pieza_amiga_mas_debil_norte(self):
        ''' Hay pieza amiga mas debil hacia el norte.'''
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---r-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(4, 4), NORTE))

    def test_hacia_apunta_fuera_tablero(self):
        ''' No hay pieza ni amiga ni enemiga porque apunta fuera del tablero.'''
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
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(7, 7), NORTE))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        ''' Hay pieza enemiga mas fuerte vecina.'''
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

    def test_no_hay_pieza_enemiga_mas_fuerte_vecina(self):
        ''' Hay pieza enemiga mas fuerte vecina.'''
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
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(6, 6)))

    def test_hay_pieza_enemiga_mas_debil_vecina(self):
        ''' Hay pieza enemiga pero es mas debil.'''
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
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(4, 3)))

    def test_hay_pieza_amiga_mas_fuerte_vecina(self):
        ''' Hay pieza mas fuerte, pero es amiga.'''
        t = leer_tablero([
              'R-e--mRr', #7
              '-------E', #6
              'h--Rr-RE', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(5, 6)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        ''' La pieza esta congelada.'''
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

    def test_no_hay_pieza_congelada_amiga_vecina(self):
        ''' La pieza esta no esta congelada, porque tiene una pieza amiga vecina.'''
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              'h-------', #1
              'rE------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(0, 0)))

    def test_no_hay_pieza_congelada_enemigo_debil(self):
        ''' La pieza no esta congelada porque la eneimga vecina es mas debil.'''
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              'eH------', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(0, 0)))

    def test_no_hay_pieza_congelada_sin_vecinas(self):
        ''' La pieza esta congelada.'''
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '------r-', #0
              #01234567
            ])
        self.assertFalse(hay_pieza_congelada(t, Posicion(0, 6)))

#### Ejercicio 4

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_mover_a_secas_ok(self):
        ''' Caso base que funciona.'''
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

    # TESTS SOBRE LAS CONDICIONES DEL JUEGO/TABELRO.
    def test_no_puede_realizar_movimiento_casilla_vacia(self):
        ''' No se puede realizar el movimiento porque la casilla del origen del movimiento es vacia.'''
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
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 0), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))    

    def test_no_pude_realziar_movimiento_color_incorrecto(self):
        ''' No puede realizar el movimiento porque la posicion del origen a mover corresponde con 
        una pieza de color distinto al color del turno del juego.'''
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
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 2), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_no_pude_realziar_movimiento_pieza_congelada(self):
        ''' No puede realizar el movimiento porque la pieza a mover esta congelada.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mE--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))    
    
    def test_no_puede_realizar_movimiento_max_pasos_superado(self):
        ''' No puede realizar movimiento porque supera la cantidad maxima de pasos.'''
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
        j = Juego(t, PLATEADO, 2)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE,NORTE,NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m)) 

    def test_mover_a_secas_invalido_fuera_del_tablero(self):
        ''' No puede moverse debido a que la nueva posicion queda fuera del tablero.'''
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

    # TESTS SOBRE CONEJOS 
    def test_no_puede_realizar_movimiento_conejo_plateado(self):
        ''' No puede realizar movimiento porque el conejo plateado no puede volver atras (NORTE)'''
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
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_no_puede_realizar_movimiento_conejo_dorado(self):
        ''' No puede realizar movimiento porque el conejo dorado no puede volver atras (SUR)'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----R-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [SUR])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_puede_realizar_movimiento_conejo_plateado(self):
        ''' Puede realizar movimiento porque el conejo plateado puede ir hacia adelante (SUR)'''
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
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [SUR])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_puede_realizar_movimiento_conejo_dorado(self):
        ''' Puede realizar movimiento porque el conejo dorado puede ir hacia adelante (NORTE)'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----R-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(5, 6), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
    # TEST SOBRE LAS CONDICIONES DE LAS ACCIONES
    # MOVER A SECAS
    def test_mover_a_secas_invalido_pos_ocupada_enemiga(self):
        ''' No puede moverse hacia la nueva posicion porque hay una pieza enemiga ocupando el espacio.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '-R------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_mover_a_secas_invalido_pos_ocupada_amiga(self):
        ''' No puede moverse hacia la nueva posicion porque hay una pieza amiga ocupando el espacio.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '-r------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    # ARRASTRAR
    def test_arrastrar_plateado_ok(self):
        ''' Caso base que funciona con arrastrar con pieza plateada.'''
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
        m = Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_arrastrar_dorado_ok(self):
        ''' Caso base que funciona con arrastrar con pieza dorada.'''
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
        j = Juego(t, DORADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE,OESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_arrastrar_invalido_pieza_mayor_fuerza(self):
        ''' No puede arrastrar porque la pieza a arrastrar es de mayor fuerza (o igual).'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mM--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_arrastrar_invalido_sin_pieza_a_arrastrar(self):
        ''' No puede arrastrar porque no hay pieza a arrastrar.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-m---mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_arrastrar_invalido_pieza_a_arrastrar_amiga(self):
        ''' No puede arrastrar porque la pieza a arrastrar es amiga.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mr--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(0, 1), [NORTE,OESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    # EMPUJAR
    def test_empujar_platead_ok(self):
        ''' Caso base que funciona con empujar con pieza plateada.'''
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
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,ESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

    def test_empujar_dorada_ok(self):
        ''' Caso base que funciona con empujar con pieza dorada.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mE--mDR', #0
              #01234567
            ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 2), [OESTE,OESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
        
    def test_empujar_invalido_pieza_mas_fuerte(self):
        ''' No puede empujar porque la pieza es mas fuerte(o misma fuerza).'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mM--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_empujar_invalido_lugar_ocupado(self):
        ''' No puede empujar porque el lugar al que empuja a la otra pieza esta ocupado.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mDr-mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_empujar_invaido_no_hay_que_empujar(self):
        ''' No puede empujar porque no hay pieza para empujar.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-m---mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_empujar_invaido_pieza_amiga(self):
        ''' No puede empujar porque la pieza a empujar es amiga.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mr--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 1), [ESTE,ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_empujar_invaido_empuja_fuera_tablero(self):
        ''' No puede empujar porque el empujado se sale del tablero.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-m---meR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(0, 6), [ESTE,ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))
    
    def test_empujar_invaido_empuja_fuera_tablero_conejo(self):
        ''' La figura es un conejo y no puede empujar porque el empujado se sale del tablero.'''
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----rR', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-m---me-', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(EMPUJAR, Posicion(5, 6), [ESTE,ESTE])
        self.assertFalse(puede_realizar_movimiento(j, m))

#### Ejercicio 5

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        ''' Caso base donde se eliminan correctamente todas las piezas en una trampa (sin amigas vecinas).'''

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

    def test_activar_trampas_sin_figuras_en_trampa(self):
            ''' Se activan todas las trampas pero no habia piezas en las trampas. Entonces,
            el tablero inicial es igual al tablero final.'''
            t0 = leer_tablero([
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
            self.assertEqual(t0, t1)
            self.assertEqual(t2, t1)
    
    def test_activar_trampas_con_pieza_amiga_vecina(self):
            ''' Se activa el tablero y se eliminan todas las piezas en posiciones trampa, menos la
            que tiene amiga vecina (5,2)'''
            t0 = leer_tablero([
                   '--RD--rd', #7
                   '--------', #6
                   'H-re-E--', #5
                   '-H--r-Cr', #4
                   'R-------', #3
                   'R-H--m--', #2
                   'R-------', #1
                   'c-D---R-', #0
                   #01234567
                 ])
            t1 = leer_tablero([
                   '--RD--rd', #7
                   '--------', #6
                   'H-re----', #5
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
    
    def test_activar_trampas_con_pieza_enemiga_vecina(self):
            ''' Se activa el tablero y se eliminan las piezas en las posiciones trampa (enemiga 
            vecina no salva a la pieza).'''
            t0 = leer_tablero([
                   '-eRD--rd', #7
                   '--------', #6
                   '-Hr--E--', #5
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
                   '-H------', #5
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

    def test_mover_a_secas_sin_cambio_de_turno(self):
        '''Mueve un conejo dorado un paso al norte sin llegar a los 4 pasos totales.'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--------',  # 3
            '--------',  # 2
            '-R------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(1, 1), [NORTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[1][1], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[2][1], Pieza(CONEJO, DORADO))
        self.assertEqual(realizar_movimiento(j, m).turno, DORADO)
        self.assertEqual(realizar_movimiento(j, m).pasos_consumidos, 1)

    def test_mover_a_secas_con_cambio_de_turno(self):
        '''Al llegar a 4 pasos consumidos (3 y 1), cambia el turno al oponente y se reinician los pasos.'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--------',  # 3
            '--------',  # 2
            '-R------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 3)
        m = Movimiento(MOVER_A_SECAS, Posicion(1, 1), [NORTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[1][1], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[2][1], Pieza(CONEJO, DORADO))
        self.assertEqual(realizar_movimiento(j, m).turno, PLATEADO)
        self.assertEqual(realizar_movimiento(j, m).pasos_consumidos, 0)

    def test_arrastrar_sin_cambio_de_turno(self):
        '''El Elefante dorado se mueve al norte y arrastra al conejo plateado hacia el este .'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--rE----',  # 3
            '--------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[4][3], Pieza(ELEFANTE, DORADO))
        self.assertEqual(realizar_movimiento(j, m).tablero[3][3], Pieza(CONEJO, PLATEADO))
        self.assertEqual(realizar_movimiento(j, m).tablero[3][2], VACIA)
        self.assertEqual(realizar_movimiento(j, m).turno, DORADO)
        self.assertEqual(realizar_movimiento(j, m).pasos_consumidos, 2)

    def test_arrastrar_con_cambio_de_turno(self):
        '''Arrastrar una pieza teniendo 2 pasos consumidos (2 y 2 = 4) cambia el turno al rival.'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--rE----',  # 3
            '--------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 2)
        m = Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[4][3], Pieza(ELEFANTE, DORADO))
        self.assertEqual(realizar_movimiento(j, m).tablero[3][3], Pieza(CONEJO, PLATEADO))
        self.assertEqual(realizar_movimiento(j, m).turno, PLATEADO)
        self.assertEqual(realizar_movimiento(j, m).pasos_consumidos, 0)

    def test_empujar_sin_cambio_de_turno(self):
        ''' El elefante dorado empuja al conejo plateado al este ocupando su lugar.'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '---Er---',  # 3
            '--------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[3][3], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[3][4], Pieza(ELEFANTE, DORADO))
        self.assertEqual(realizar_movimiento(j, m).tablero[3][5], Pieza(CONEJO, PLATEADO))
        self.assertEqual(realizar_movimiento(j, m).turno, DORADO)
        self.assertEqual(realizar_movimiento(j, m).pasos_consumidos, 2)

    def test_empujar_con_cambio_de_turno(self):
        '''Empujar una pieza teniendo 2 pasos consumidos (2 y 2 = 4) cambia el turno al rival.'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '---Er---',  # 3
            '--------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 2)
        m = Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[3][3], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[3][4], Pieza(ELEFANTE, DORADO))
        self.assertEqual(realizar_movimiento(j, m).turno, PLATEADO)
        self.assertEqual(realizar_movimiento(j, m).tablero[3][5], Pieza(CONEJO, PLATEADO))
        self.assertEqual(realizar_movimiento(j, m).pasos_consumidos, 0)

    def test_caer_en_trampa_sin_aliado_elimina_pieza(self):
        '''Pieza cae en la trampa (2,2) sin aliados adyacentes y la trampa la elimina.'''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--------',  # 3
            '-R------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(2, 1), [ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[2][1], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[2][2], VACIA)

    def test_caer_en_trampa_con_aliado_sobrevive(self):
        ''' Una Pieza cae en trampa (2,2) pero sobrevive por tener un perro aliado en (3,2) posición adyacente. '''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--D-----',  # 3
            '-R------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(2, 1), [ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[2][1], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[2][2], Pieza(CONEJO, DORADO))

    def test_empujar_enemigo_a_trampa_lo_elimina(self):
        '''Empujar a un enemigo a la trampa (2,2) sin aliados lo elimina del tablero. '''
        t = leer_tablero([
            '--------',  # 7
            '--------',  # 6
            '--------',  # 5
            '--------',  # 4
            '--------',  # 3
            'Er------',  # 2
            '--------',  # 1
            '--------',  # 0
            #01234567
        ])
        j = Juego(t, DORADO, 0)
        m = Movimiento(EMPUJAR, Posicion(2, 0), [ESTE, ESTE])

        self.assertEqual(realizar_movimiento(j, m).tablero[2][0], VACIA)
        self.assertEqual(realizar_movimiento(j, m).tablero[2][1], Pieza(ELEFANTE, DORADO))
        self.assertEqual(realizar_movimiento(j, m).tablero[2][2], VACIA)
        
#### Ejercicio 7

class test_ganador_del_juego(unittest.TestCase):
    
    def test_promueve_conejo_dorado_turno_del_oponente(self):
        ''' Gana el jugador dorado en el turno del oponente por tener un conejo en la fila inicial de su oponente'''
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

    def test_promueve_conejo_dorado_su_turno(self):
        ''' Gana el jugador en su turno por tener un conejo en la fila inicial de su oponente
        y el otro jugador no cumple las condiciones para ganar'''
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
        j = Juego(t, DORADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

    def test_sin_conejos_plateados_turno_del_oponente(self):
        ''' Gana el jugador dorado en su turno del oponente porque no hay más conejos plateados'''
        t = leer_tablero([
              '--------', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '--------', #2
              '-H---DCC', #1
              'R-R---RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

    def test_sin_conejos_plateados_su_turno(self):
            ''' Gana el jugador dorado en el turno del oponente porque no hay más conejos plateados
             y el otro jugador no cumple las condiciones para ganar'''
            t = leer_tablero([
                  '--------', #7
                  'c-----me', #6
                  '---Ed-R-', #5
                  '-M---R--', #4
                  '---R----', #3
                  '--------', #2
                  '-H---DCC', #1
                  'R-R---RR', #0
                  #01234567
                ])
            j = Juego(t, DORADO, 0)
            self.assertTrue(hay_ganador_determinado(j))
            self.assertEqual(ganador_del_juego(j), DORADO)

    def test_sin_ganador(self):
            ''' No hay ganador porque ninguno cumple'''
            t = leer_tablero([
                  'rr----rr', #7
                  'c-----me', #6
                  '---Ed-R-', #5
                  '-M---R--', #4
                  '---R----', #3
                  '-rrrr---', #2
                  '-H---DCC', #1
                  'R----RRR', #0
                  #01234567
                ])
            
            j = Juego(t, DORADO, 0)
            self.assertFalse(hay_ganador_determinado(j))
    
    def test_cumplen_los_dos(self):
                ''' Gana el oponente porque cumplen los dos'''
                t = leer_tablero([
                      '-------R', #7
                      'c-----me', #6
                      '---Ed-R-', #5
                      '-M---R--', #4
                      '---R----', #3
                      '--rrr---', #2
                      '-H---DCC', #1
                      'r-------', #0
                      #01234567
                    ])
                
                j = Juego(t, DORADO, 0)
                self.assertTrue(hay_ganador_determinado(j))
                self.assertEqual(ganador_del_juego(j), PLATEADO)


if __name__ == '__main__':
    unittest.main(verbosity=2) 

