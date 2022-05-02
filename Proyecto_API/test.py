import unittest
from unittest import mock
from unittest.mock import patch
from DB import *
from API import *
class Tests(unittest.TestCase):
    
    #Se realizaron pruebas unitarias de mock para probar que las llamadas a la base de datos sean correctas
    @patch('DB.ConexionBD.eliminar_equipo', return_value = True)
    def test_eliminar_equipo(self, mock):
        bd = ConexionBD()
        expected = True
        actual = bd.eliminar_equipo(1)
        assert expected == actual
    
    
    @patch('DB.ConexionBD.eliminar_equipo', return_value = False)
    def test_eliminar_equipo_dos(self,mock):
        bd = ConexionBD()
        resultado_esperado = False
        resultado_actual = bd.eliminar_equipo(2)
        assert resultado_esperado == resultado_actual 
    
    
    @patch('DB.ConexionBD .eliminar_pokemon', return_value = True)
    def test_eliminar_pokemon(self,mock):
        bd = ConexionBD()
        resultado_esperado = True
        resultado_actual = bd.eliminar_pokemon(5)
        assert resultado_esperado == resultado_actual
    
    
    @patch('DB.ConexionBD.eliminar_pokemon', return_value = False)
    def test_eliminar_pokemon_dos(self,mock):
        bd = ConexionBD()
        resultado_esperado = False
        resultado_actual = bd.eliminar_pokemon(5)
        assert resultado_esperado == resultado_actual
    
    
    @patch('DB.ConexionBD.guardar_equipo', return_value = True)
    def test_guardar_equipo(self,mock):
        bd = ConexionBD()
        expected = True
        actual = bd.guardar_equipo("mock")
        assert expected == actual
        
        
    @patch('DB.ConexionBD.guardar_equipo', return_value = False)
    def test_guardar_equipo_dos(self,mock):
        bd = ConexionBD()
        expected = False
        actual = bd.guardar_equipo("mock")
        assert expected == actual
    

    @patch('DB.ConexionBD.guardar_pokemon', return_value = True)
    def test_guardar_pokemon(self,mock):
        bd = ConexionBD()
        expected = True
        actual = bd.guardar_pokemon("mock",12)
        assert expected == actual
        
    @patch('DB.ConexionBD.guardar_pokemon', return_value = False)
    def test_guardar_pokemon_dos(self,mock):
        bd = ConexionBD()
        expected = False
        actual = bd.guardar_pokemon("mock",12)
        assert expected == actual
    
if __name__ == '__main__':
    unittest.main()