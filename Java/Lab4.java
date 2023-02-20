import java.util.Scanner;
public class Lab4
{    
    //Metodos
    public static boolean inttoboolean(int x)
    {
        if(x == 1)
        {
            return true;
        }
        return false;
    }
    public static String s1(boolean a,boolean c)
    {
        if((a==true)||(c==true))
        {
            return "S1 esta en peligro";
        }

        return "S1 esta a salvo";
    }
    public static String s2(boolean a,boolean b,boolean c,boolean d)
    {
        if(((c == true)&&((a == true)||(b== true)||(d==true)))||((a ==true)&&(b == true)&&(c == true)))
        {
            return "S2 esta en peligro";
        }

        return "S2 esta a salvo";
    }
    public static String s3(boolean a,boolean b,boolean c,boolean d)
    {
        if((d&&((c==true)||(b==true)))||(a==true))
        {
            return "S3 esta en peligro";
        }

        return "S3 esta a salvo";
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);//Para entrar variables
        boolean a = false;
        boolean b = false;
        boolean c = false;
        boolean d = false;
        System.out.println("\nIngrese 1 si esta activa la maquina o ingrese 0 si no\n");
        for (int i = 0; i < 4; i++) {
            System.out.print("Ingrese datos de la maquina [" + (i + 1) + "]: ");
            int numero = scanner.nextInt();
            switch (i) {
                case 0:
                    a = (inttoboolean(numero));
                case 1:
                    b = (inttoboolean(numero));
                case 2:
                    c = (inttoboolean(numero));
                case 3:
                    d = (inttoboolean(numero));
            }
        }
        System.out.println(s1(a, c));
        System.out.println(s2(a,b,c,d));
        System.out.println(s3(a,b,c,d));
    }
}