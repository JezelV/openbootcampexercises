
abstract class Persona {
    // Properties
    final private int edad;
    final private String nombre;
    final private String telefono;

    // Constructor
    public Persona(int edad, String nombre, String telefono) {
        this.edad = edad;
        this.nombre = nombre;
        this.telefono = telefono;
    }

    // Getters
    public int getEdad() {
        return edad;
    }
    public String getNombre() {
        return nombre;
    }
    public String getTelefono() {
        return telefono;
    }
}

final class Client extends Persona {
    // Properties
    final private long credito;

    // Constructor
    public Client(int edad, String telefono, String nombre, long credito) {
        super(edad, nombre, telefono);
        this.credito = credito;
    }

    // Methods
    public String showInformation() {
        return "Nombre: " + super.getNombre() + "\nEdad: " + super.getEdad() + "\nTelefono: " + super.getTelefono() + "\nCredito: " + credito;
    }
}

final class Worker extends Persona {
    // Properties
    final private int salario;

    // Constructor
    public Worker(int edad, String telefono, String nombre, int salary) {
        super(edad, nombre, telefono);
        this.salario = salary;
    }

    // Methods
    public String showInformation() {
        return "Nombre: " + super.getNombre() + "\nEdad: " + super.getEdad() + "\nTelefono: " + super.getTelefono() + "\nSalario: " + salario;
    }
}

public class Main {
    public static void main(String[] args) {

        // Primera parte del ejercicio
        Client client1 = new Client(20, "+00 (000) 000 00 00", "Juan", 100);
        System.out.println(client1.showInformation());
        System.out.println();

        // Segunda parte del ejercicio
        Worker worker1 = new Worker(30, "+00 (000) 000 00 00", "Pedro", 1000);
        System.out.println(worker1.showInformation());
    }
}
