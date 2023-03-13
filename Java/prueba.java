import java.util.Scanner;

public class prueba
{

// Algoritmo de cuadrados medios flexible
public static int[] algoritmoCuadradosMedios(String semilla, int cantNumeros) {
    int[] resultado = new int[cantNumeros]; //Se inicializa el vector con la cantidad de números a generar
    int tam1 = semilla.length(); //Determina el tamaño de la semilla
    long numero1 = Long.parseLong(semilla); //Conversor de la semilla a un entero largo
    for (int i = 0; i < cantNumeros; i++) {
        long numero2 = numero1 * numero1; //Se realiza la operación del cuadrado de la semilla
        String snumero2 = String.valueOf(numero2); //Transforma el número generado en una string
        int tam2 = snumero2.length(); //Calcula el tamaño del número generado
        int primerc = (tam2 - tam1) / 2; //Determina a partir de cual número se extrae la cadena de tam1 del calculo generado
        String snumero3 = snumero2.substring(primerc, primerc + tam1); //Se extrae la cadena de tam1 del cálculo generado
       // snumero3="0."+"snumero3";
        resultado[i] = Integer.parseInt(snumero3);
       // System.out.println("Semilla" + numero1);
        numero1 = Long.parseLong(snumero3);

    }
    return resultado;
}

// Función para saber si tiene 3 números iguales
public static boolean tieneTresDigitosIguales(int num) // Determina si se repiten números a lo largo de la semilla
{
    String numStr = Integer.toString(num); //cambia el número a una string para poderlo dividir
    for (int i = 0; i < numStr.length(); i++) //Se recorre en dos for para ir recorriendo en el mismo array un digito y en el otro que pase por todos
    {// me explico, el primer digito es comparador con cada uno de los digitos en el mismo número, permite saber la cantidad con el contador
        int cont = 0;//cada pasada vuelve a 0, si no, no tendría sentido
        for (int j = 0; j < numStr.length(); j++)// este for lo que hace es recorrer la misma array pero con el fin de compararla
        {
            if (numStr.charAt(i) == numStr.charAt(j))//acumula si son iguales
            { //Se recorre la misma cadena con el fin de comparar si existen iguales
                cont++; //Con ello almacenando y si llega a 3, retornar verdadero
            }
            if (cont >= 3)
            {
                return true;// retorna verdadero si el contador llega a 3, desplegando un IF abajo
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
        System.out.print("Ingrese una semilla de 5 a 7 dígitos: ");//ingresa la semilla
        int seed = sc.nextInt();//scanner de la semilla
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
        else// si no entra en ningún if, se sale
        {
            String seedStr = Integer.toString(seed);
            int[] numeros = algoritmoCuadradosMedios(seedStr,36);//El 36 sera el limite aunque el 28 es el indicado
            for (int i = 0; i < numeros.length; i++)//imprime la matriz que retorna el metodo
            {
                System.out.println(i+")  "+ "0."+numeros[i]);
            }
        }
    }
}
}

