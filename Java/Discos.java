import java.util.Scanner;

public class Discos
{
    public static void main(String[] args)
    {
        Scanner input = new Scanner(System.in);
        double vt, v0;
        while (true) {
            try {
                System.out.print("\nIngreso de masa total para discos: ");
                vt = Double.parseDouble(input.nextLine());
                System.out.print("Masa perdida en la forja de discos: ");
                v0 = Double.parseDouble(input.nextLine());
                if (vt <= v0)
                {
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
        double diametroAnterior = 0;
        if (Math.pow(2, 16) > v0 && Math.pow(2, 64) > vt) {
            while (true) {
                i++;
                int y = i * i;
                double a = (vt / y) - v0;
                if (a >= 0)
                {
                    System.out.println("Hace el calculo del diamextro");
                    double diametro = 0.3 * Math.sqrt(vt / y - v0);
                    System.out.println("Filas: " + i);
                    System.out.println("Diametro: " + diametro);
                    int discos = (int) (diametro * y);
                    System.out.println("Discos: " + discos);
                    if (discos > (Math.pow(10, 3))) {
                        discos %= Math.pow(10, 3);
                    }
					if (discos < valorAnterior) {
                        System.out.println("Fila: " + (i - 1));
                        System.out.println("Maximo número estirado: " + valorAnterior);
                        System.out.println("Diametro maximo: " + diametroAnterior);
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
        }
    }
}

