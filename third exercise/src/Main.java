
class Persona {

    // Properties
    private int edad;
    private String nombre;
    private String apellido;
    private String telefono;

    // Constructor Overloading
    public Persona(){
        this.nombre = "";
        this.apellido = "";
        this.telefono = "+00 (000) 000-0000";
        this.edad = 0;
    }
    public Persona(String nombre, String apellido, String telefono, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.telefono = telefono;
        this.edad = edad;
    }

    // Methods
    void mostrarDatos(Persona persona) {
        System.out.println("Nombre: " + persona.nombre);
        System.out.println("Apellido: " + persona.apellido);
        System.out.println("Telefono: " + persona.telefono);
        System.out.println("Edad: " + persona.edad + "\n");
    }

    // Getters y Setters
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    public String getApellido() {
        return apellido;
    }
    public void setTelefono(String telefono){
        this.telefono = telefono;
    }
    public String getTelefono(){
        return this.telefono;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }
    public int getEdad() {
        return edad;
    }
}

public class Main {
    public static void main(String[] args) {

        Persona juan = new Persona();

        // Proporcionar valores: forma larga
        juan.setEdad(20);
        juan.setNombre("Juan");
        juan.setApellido("Perez");
        juan.setTelefono("+00 (000) 000-0000");
        System.out.println();

        // Proporcionar valores: forma corta
        Persona maria = new Persona("Maria", "Gonzalez", "+00 (000) 000-0000", 20);

        // Mostrar datos: forma larga
        System.out.println("Metodo largo para mostrar los datos (Juan): ");
        System.out.println(juan.getEdad());
        System.out.println(juan.getNombre());
        System.out.println(juan.getApellido());
        System.out.println(juan.getTelefono());
        System.out.println();

        // Mostrar datos: forma corta
        System.out.println("Metodo optimizado para mostrar los datos (Maria): ");
        juan.mostrarDatos(maria);
    }
}