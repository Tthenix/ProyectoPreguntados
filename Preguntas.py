import random

class Matematica(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = Matematica ('Pregunta1')
print(a.preguntas)

       
class Programacion(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = Programacion ('')
print(a.preguntas)
         

class Fisica(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = Fisica ('')
print(a.preguntas)


class teleinformatica(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = teleinformatica ('')
print(a.preguntas)



class laboratorioDeHardware(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = laboratorioDeHardware ('')
print(a.preguntas)
    

class sistemaOperativo(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = sistemaOperativo ('')
print(a.preguntas)


class educacionFisica(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = educacionFisica ('')
print(a.preguntas)


class ingles(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = ingles ('')
print(a.preguntas)



class politicaYCiudadania(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = politicaYCiudadania ('')
print(a.preguntas)


class investigacionOperativa(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = investigacionOperativa ('')
print(a.preguntas)


class mantenimientoDeHardware(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = mantenimientoDeHardware ('')
print(a.preguntas)


class lenguaYLiteratura(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = lenguaYLiteratura ('')
print(a.preguntas)


class arquitecturasDeComputadoras(object):
    def __init__(self, pregunta):
        self.pregunta = pregunta

    @property
    def preguntas(self):
        try:
            return self._preguntas
        except AttributeError:
            self._preguntas = random.choice(['a', 'b', 'c', 'd'])
            return self._preguntas

a = arquitecturasDeComputadoras ('')
print(a.preguntas)
