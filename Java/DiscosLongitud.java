import java.util.Scanner;

public class DiscosLongitud
{
    public static void main(String[] args)
    {
        Scanner entrada= new Scanner(System.in);
        double v0 = 0, vTotal = 0, diametroAnterior = 0;
        while (true)
        {
            while (true)
            {
                try
                {
                    System.out.print("\nIngreso de masa total para discos: ");
                    vTotal = Double.parseDouble(entrada.nextLine());
                    System.out.print("Masa perdida en la forja de discos: ");
                    v0 = Double.parseDouble(entrada.nextLine());
                    if (vTotal <= v0) {
                        System.out.println("Ingrese cantidades validas");
                        continue;
                    }
                    else
                    {
                        break;
                    }
                }
                catch (NumberFormatException e)
                {
                    System.out.println("¡Ingrese algo valido!");
                }
            }
            int i = 0;
            int valorAnterior = 0;
            if (Math.pow(2, 16) > v0 && Math.pow(2, 64) > vTotal)
            {
                System.out.println("Calculo de la longitud maxima");
                while (true)
                {
                    i++;
                    int y = i * i;
                    double a = (vTotal / y) - v0;
                    if (a >= 0)
                    {
                        double diametro = 0.3 * Math.sqrt(vTotal / y - v0);
                        int discos = (int) (diametro * y);
                        if (discos > Math.pow(10, 3))
                        {
                            discos = discos % (int) Math.pow(10, 3);
                        }
                        if (discos < valorAnterior)
                        {
                            System.out.println("Fila: " + (i - 1) + "\nMaximo número estirado: " + valorAnterior + "\nDiametro maximo: " + diametroAnterior);
                            break;
                        }
                        valorAnterior = discos;
                        diametroAnterior = diametro;
                    }
                    else
                    {
                        break;
                    }
                }
                break;
            }
            if (Math.pow(2, 16) < v0 || Math.pow(2, 64) < vTotal)
            {
                System.out.println("\n Cantidades no validas ");
                continue;
            }
        }
    }
}
