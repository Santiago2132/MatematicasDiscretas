import java.util.Scanner;

public class paratu
{    
    public void heart()
    {
        System.out.println("────(♥)(♥)(♥)────(♥)(♥)(♥) __ para ti        \n──(♥)██████(♥)(♥)██████(♥) Mi consentida        \n─(♥)████████(♥)████████(♥) bonita        \n─(♥)██████████████████(♥) espero te vaya bonito        \n──(♥)████████████████(♥) que no tengas tanto dolor        \n────(♥)████████████(♥) Estas super guapa :)         \n──────(♥)████████(♥) que es la niña dueña de mi         \n────────(♥)████(♥) mayor amor        \n─────────(♥)██(♥) y        \n───────────(♥) __ mayor deseo se cumplio contigo"
        );
    }
    public void mensajito()
    {
        System.out.println("Te amor mi niña lindaaaaaaaaaaaaaaaa :)");
    }
    public static void main(String[] args)
    {
        paratu Santi = new paratu();
        Scanner sc = new Scanner(System.in);
        while (true)
        {
            System.out.println("Ingresa 1 o 2: ");
            int opcion = sc.nextInt();
            if (opcion == 1)
            {
                Santi.heart();
            }
            if (opcion == 2)
            {
                Santi.mensajito();
            }
        }
        
    }
}