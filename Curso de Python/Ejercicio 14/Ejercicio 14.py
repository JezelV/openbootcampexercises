class Alumno:
    _nombre = ""
    _nota = 0
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getNota(self):
        return self._nota
    
    def setNota(self, nota):
        self._nota = nota

    def aprobado(self):
        if self._nota >= 70:
            return True
        else:
            return False
    
    def info(self):
        return "Nombre: " + self.getNombre() + "\tNota: " + str(self.getNota()) + "\tAprobado: " + str(self.aprobado())

a = Alumno()
a.setNombre("Juan")
a.setNota(80)
print(a.info())
