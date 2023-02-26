import java.lang.Math;

public class Discos
{
    public static boolean positive(double a) // Verifica que el resultado de dentro de la Raiz no sea negativo
    {
        if (a > 0)
        {
            return true;
        }
        if (a < 0)
        {
            return false;
        }
        return false;
    }
    public static double disk(double a, double b) //Hace el calculo de los discos
    {
        double x = b * b;
        double z = a * x;
        return z;
    }
    public static void main(String[] args)
    {
        double vt = 12; //volumen total
        double v0 = 1; //volumen perdido
        int i = 0;
        while (true) 
        {
            i++;
            double y = i * i; // Volumen de la matriz
            double a = (vt / y) - v0;
            if (positive(a) == true)//Si lo de dentro de la matriz es positivo hace el calculo
            {
                System.out.println("Hace el calculo del diametro");
                double diametro = 0.3 * Math.sqrt(vt / y - v0);//calcula el diametro 
                System.out.println("Diametro: " + diametro);//Impresión del diametro
                System.out.println("Discos: " + disk(diametro, i));//Impresipon y calculo de los discos
            }
            if (positive(a) == false)
            {
                break;
            }
        }
    }
}