
class Persona {
    String nombre;
    String apellido;
    int edad;
    String sexo;
    String estadoCivil;
    String nacionalidad;

    public Persona(String nombre, String apellido, int edad, String sexo, String estadoCivil, String nacionalidad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
        this.sexo = sexo;
        this.estadoCivil = estadoCivil;
        this.nacionalidad = nacionalidad;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo, soy una App Java");

        // Crear dos instancias de la clase Persona
        Persona juanito = new Persona("Juan", "Perez", 30, "M", "Casado", "Argentina");

        Persona pepito = new Persona("Pepito", "Perez", 30, "M", "Casado", "Mexicano");

        // Imprimir los datos de la persona Juanito
        System.out.println("Nombre: " + juanito.nombre);
        System.out.println("Apellido: " + juanito.apellido);
        System.out.println("Edad: " + juanito.edad);
        System.out.println("Sexo: " + juanito.sexo);
        System.out.println("Estado Civil: " + juanito.estadoCivil);
        System.out.println("Nacionalidad: " + juanito.nacionalidad);
        System.out.println();

        // Imprimir los datos de la persona Pepito
        System.out.println("Nombre: " + pepito.nombre);
        System.out.println("Apellido: " + pepito.apellido);
        System.out.println("Edad: " + pepito.edad);
        System.out.println("Sexo: " + pepito.sexo);
        System.out.println("Estado Civil: " + pepito.estadoCivil);
        System.out.println("Nacionalidad: " + pepito.nacionalidad);

    }
}
