import java.util.Scanner;

public class Discos
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingreso de la masa total: ");
        double vt = sc.nextDouble(); // almacenado de masa total
        System.out.print("Ingreso de la masa perdida: ");
        double v0 = sc.nextDouble();// almacenado de la masa perdida
        int i = 0;
        if (Math.pow(2, 16) > v0 && Math.pow(2, 64) > vt)
        {
            while (true)
            {
                i++;
                double y = i * i; // calculo de casillas i = 2, la matriz sera de 4 casillas por que y = 2 * 2 = 4
                double a = (vt / y) - v0; // calculo previo para verfificar que dentro de la raiz no sea negativo
                if (a >= 0)
                {
                    System.out.println("Hace el calculo del diametro");
                    double diametro = 0.3 * Math.sqrt(vt / y - v0);
                    System.out.println("Filas: " + i);
                    System.out.println("Diametro: " + diametro);
                    double discos = diametro * y;
                    if (discos > Math.pow(10, 3))
                    {
                        discos = discos % Math.pow(10, 3);
                    }
                    if (discos < Math.pow(10, 3)) 
                    {
                        System.out.println("Discos: " + discos);
                    }
                }
                else 
                {
                    break;
                }
            }
        }
    }
}
