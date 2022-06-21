
public class Main {

    public static int sumOfThreeNumbers(int a, int b, int c) {
        return a + b + c;
    }   

    public static void main(String[] args) {

        System.out.println();
        // Parte uno:
        System.out.println("Suma de 1, 2 y 3: " + sumOfThreeNumbers(1, 2, 3));

        // Parte dos:
        coche miCoche = new coche();
        miCoche.addPuerta();
        System.out.println("El numero de puertas que tiene mi coche son: " + miCoche.getPuertas());

    }


}
