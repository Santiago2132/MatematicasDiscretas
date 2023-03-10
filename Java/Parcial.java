import java.util.Scanner;

public class Parcial {
    // Algoritmo de cuadrados medios flexible 
    public static int[] algoritmoCuadradosMedios(String semilla, int cantNumeros)
    {
        int[] resultado = new int[cantNumeros];
        int tam1 = semilla.length(); //Determina el tamaño de la semilla
        int numero1 = Integer.parseInt(semilla); //Conversor de la semilla a un entero
        for (int i = 0; i < cantNumeros; i++)
        {
            int numero2 = numero1 * numero1; //Se realiza la operación del cuadrado de la semilla
            String snumero2 = Integer.toString(numero2); //Transforma el número generado en una string
            int tam2 = snumero2.length(); //Calcula el tamaño del número generado
            int primerc = (tam2 - tam1) / 2;//Determina a partir de cual número se extrae la cadena de tam1 del calculo generado
            String snumero3 = snumero2.substring(primerc, primerc + tam1); //Se arma la cadena a partir del primer digito
            resultado[i] = Integer.parseInt(snumero3);
            numero1 = Integer.parseInt(snumero3);
        }
        return resultado;
    } 
    // Función para saber si tiene 3 números iguales
    public static boolean tieneTresDigitosIguales(int num)
    {
        String numStr = Integer.toString(num);
        for (int i = 0; i < numStr.length(); i++) 
        {
            int cont = 0;
            for (int j = 0; j < numStr.length(); j++)
            {
                if (numStr.charAt(i) == numStr.charAt(j))
                { //Se recorre la misma cadena con el fin de comparar si existen iguales
                    cont++; //Con ello almacenando y si llega a 3, retornar verdadero
                }
                if (cont >= 3)
                {
                    return true;
                }
            }
        }
        return false;
    }
    // Programa principal
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        while (true)
        {
                System.out.print("Ingrese una semilla de 5 a 7 dígitos: ");
                int seed = sc.nextInt();
                if (seed < 10000 || seed > 9999999) { //Verifica la cantidad de digitos que tiene el número 
                    System.out.println("Error: la semilla debe tener entre 5 y 7 dígitos");
                    continue;
                } else if (Integer.toString(seed).matches("(\\d)\\1+")) { //Verifica que no tenga todos los digitos iguales
                    System.out.println("Error: la semilla no puede tener todos los dígitos iguales");
                    continue;
                } else if (Integer.toString(seed).matches(".*(012|123|234|345|456|567|678|789).*")) { // verifica la secuencia no sea igual
                    System.out.println("Error: la semilla no puede tener números consecutivos");
                    continue;
                } else if (tieneTresDigitosIguales(seed)) { // Que no tenga 3 digitos repetidos
                    System.out.println("Error: la semilla no puede tener tres dígitos iguales");
                    continue;
                }
                else
                {
                    String seedStr = Integer.toString(seed);
                    int[] numeros = algoritmoCuadradosMedios(seedStr,36);
                    for (int i = 0; i < numeros.length; i++)
                    {
                        System.out.println(numeros[i]);
                    }
                    
                }
        }
    }
}

