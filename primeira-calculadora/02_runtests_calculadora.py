#baixe tb o arquivo 02_calculadora.py

# instruções: 
# SETUP: vc vai precisar de 2 terminais do VSCode
# um pro flask, outro pro teste.
# sugiro quebrar o terminal embaixo em 2, assim, vc pode ver erros no flask
# a ideia é rodar o 02_calculadora e usar o 02_runtests_calculadora pra testar

# Você deve implementar as 4 operações 
# assim, quando o usuário mandar a=2, b=3, ope=soma,
# você deverá responder algo como "a soma deu 5"

#o arquivo de testes verifica elas, passo a passo

# se vc terminar, tente fazer com que a URL resultado exiba um form:
#   * se o usuário mandou os dados, ela exibe o resultado
#   * se o usuário ainda nao mandou nada, ela exibe o form
#   * se o usuário cometeu algum erro, ela exibe o erro e o form

# se vc terminar, olhe o 03_templates.zip. Entendeu ele? Fez o exercicio?
# Volte aqui
# e reescreva sua calculadora usando templates (ou seja, com arquivo
# .html separado)

import unittest
import requests

class TestStringMethods(unittest.TestCase):



     def test_00_soma(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"soma"})
         #acessa "http://localhost:5000/resultado?a=10&b=20&ope=soma"
         # se quiser, olhe no navegador
         if "30" not in r1.text:
             self.fail("a soma de 10 com 20 deveria ter dado trinta")

     def test_01_divisao(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"div"})
         #acessa "http://localhost:5000/resultado?a=10&b=20&ope=div"
         if "0.5" not in r1.text:
             self.fail("10/20 deveria ter dado 0.5")

     def test_02_mult(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":20, "ope":"mult"})
         #acessa "http://localhost:5000/resultado?a=10&b=20&ope=mult"
         if "20" not in r1.text:
             self.fail("o produto de 10 com 20 deveria ter dado 200")

     def test_03_sub(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':30,"b":20, "ope":"sub"})
         #acessa "http://localhost:5000/resultado?a=10&b=20&ope=sub"
         if "10" not in r1.text:
             self.fail("subtrair 20 de 30 deveria ter dado 10")

     def test_04_divisao_por_zero(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':10,"b":0, "ope":"div"})
         #acessa "http://localhost:5000/resultado?a=10&b=0&ope=div"
         if "ERRO" not in r1.text:
             self.fail("10/0 deveria ter dado um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")

     def test_05_a_inteiro(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'a':'banana',"b":20, "ope":"soma"})
         if "ERRO" not in r1.text:
             self.fail("Enviei um a inválido, esperava um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     def test_05_b_inteiro(self):
         r1 = requests.get("http://localhost:5000/resultado",params={'b':'banana',"a":20, "ope":"soma"})
         if "ERRO" not in r1.text:
             self.fail("Enviei um b inválido, esperava um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     def test_06_incompleto(self):
         r1 = requests.get("http://localhost:5000/resultado",params={"b":20, "ope":"sub"})
         if "ERRO" not in r1.text:
             self.fail("Enviei dados incompletos (faltava a) e esperava um ERRO; a string 'ERRO' deve aparecer na pagina")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     
     def test_07_b_incompleto(self):
         r1 = requests.get("http://localhost:5000/resultado",params={"a":20, "ope":"sub"})
         if "ERRO" not in r1.text:
             self.fail("Enviei dados incompletos (faltava b) e esperava que a resposta tivesse a string 'ERRO'")
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")

     def test_08_ope_incompleto(self):
         r1 = requests.get("http://localhost:5000/resultado",params={"a":20, "b":10})
         if "ERRO" not in r1.text:
             self.fail("Enviei dados incompletos (faltava ope) e esperava que a resposta tivesse a string 'ERRO'")     
         if "Traceback" in r1.text:
             self.fail("recebi a tela de debug do flask")
     
     
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()