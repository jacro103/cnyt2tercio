import unittest
import libreriados as lc
import cap4a as lc
import cap4b as lc


class Prueba_cap4b(unittest.TestCase):
    def test(self):
        self.assertEqual(lc.ParticulaPosicion( [(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)] , 2 ), 0.05263157894736841)
if __name__ == "__main__":
    unittest.main()
class Prueba_cap4b(unittest.TestCase):
    def test(self):
        self.assertEqual(lc.transitarVectorVector([(1.0, 0.0), (0.0, -1.0)],[(0.0, 1.0), (1.0, 0.0)]),(0.0, -1.414213562373095))

if __name__ == "__main__":
    unittest.main()

class Prueba_cap4b(unittest.TestCase):
    def test_valorEsperado(self):
        self.assertEqual(lc.valorEsperado([[(1.0, 0.0), (0.0, -1.0)], [(0.0, 1.0), (2.0, 0.0)]],
                                                       [(1.0, 0.0), (0.0, 1.0)]), (2.0, 0.0))
if __name__ == "__main__":
    unittest.main()

class Prueba_cap4b(unittest.TestCase):
    def test_varianzaObservable(self):
        self.assertEqual(lc.varianzaObservable([[(1.0, 0.0), (0.0, -1.0)], [(0.0, 1.0), (2.0, 0.0)]],
                                                            [(1.0, 0.0), (0.0, 1.0)]), (1.0, 0.0))
if __name__ == "__main__":
    unittest.main()
class Prueba_cap4b(unittest.TestCase):
    def test_dinamica(self):
        self.assertEqual(lc.dinamica( [[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0)],
                                                    [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)],
                                                    [(1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (1.0, 0.0), (0.0, 0.0)]]
                                                   ,[(1.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)] ,
                                                      3),
                                                 [[(0.0, 0.0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)], [(0, 0)]])
if __name__ == "__main__":
    unittest.main()