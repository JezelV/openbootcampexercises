public class Main {


    public static void main(String[] args) {

        int numeroIf = 0;
        int numeroWhile = 0;
        int numeroDoWhile = 5;
        String estacion = "verano";

        // Primera parte del ejercicio
        System.out.println("\nPrimera parte del ejercicio");
        if (numeroIf == 0) {
            System.out.println("numeroIf es igual a 0");
        } else if (numeroIf > 0) {
            System.out.println("numeroIf es mayor a 0");
        } else {
            System.out.println("numeroIf es menor a 0");
        } // Fin del if

        // Segunda parte del ejercicio
        System.out.println("\nSegunda parte del ejercicio");
        while (numeroWhile < 3) {
            System.out.println("numeroWhile vale: " + numeroWhile);
            numeroWhile++;
        } // Fin del while

        // Tercera parte del ejercicio
        System.out.println("\nTercera parte del ejercicio");
        do {
            System.out.println("numeroDoWhile vale: " + numeroDoWhile);
            numeroDoWhile++;
        } while (numeroDoWhile < 3); // Fin del do while

        // Cuarta parte del ejercicio
        System.out.println("\nCuarta parte del ejercicio");
        for (int i = 0; i < 3; i++) {
            System.out.println("la variable local del for vale: " + i);
        } // Fin del for

        // Quinta parte del ejercicio
        System.out.println("\nQuinta parte del ejercicio");
        switch (estacion) {
            case "verano":
                System.out.println("Estamos en verano");
                break;
            case "invierno":
                System.out.println("Estamos en invierno");
                break;
            case "primavera":
                System.out.println("Estamos en primavera");
                break;
            case "otonio":
                System.out.println("Estamos en otonio");
                break;
            default:
                System.out.println("No es una estacion");
                break;
        } // Fin del switch
    }
}
