
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;//Import LinkedList

public class ValidadorHTML
{
    public static void main(String[] args)
    {
        String archivoHTML = "C:\\Users\\santi\\IdeaProjects\\PrimerProyecto\\src\\Ejercicio5\\archivo.html"; // Ruta del archivo a validar
        boolean esValido = validarHTML(archivoHTML);
        System.out.println("Es valido: "+esValido);
        if (esValido)
        {
            System.out.println("Es valido, no contiene errores");
        }
        else
        {
            System.out.println("Error: El archivo HTML contiene errores de etiquetas.");
        }
    }
    public static boolean validarHTML(String archivo) //Valida el HTML
    {
        String contenido = extraerContenidoHTML(archivo);
        try
        {
            BufferedReader br = new BufferedReader(new FileReader(archivo));
            String linea;
            while ((linea = br.readLine()) != null)
            {
                contenido += linea;
            }
            br.close();
        }
        catch (IOException e)
        {
            System.out.println("Error al leer el archivo: " + e.getMessage());
            return false;
        }

        LinkedList<String> pilaEtiquetas = new LinkedList<String>();//Cambiar a LinkedList

        for (int i = 0; i < contenido.length(); i++)
        {
            char c = contenido.charAt(i);
            if (c == '<')
            {
                String etiqueta = "";
                int j = i + 1;
                while (j < contenido.length() && contenido.charAt(j) != '>')
                {
                    etiqueta += contenido.charAt(j);
                    j++;
                }
                if (etiqueta.charAt(0) == '/')// Etiqueta de cierre
                {
                    etiqueta = etiqueta.substring(1);
                    if (pilaEtiquetas.isEmpty())//Cambiado a isEmpty()
                    {
                        System.out.println("Error: " + etiqueta + " no tiene una etiqueta de apertura.");
                        return false;
                    }
                    else
                    {
                        String etiquetaApertura = pilaEtiquetas.removeLast();//Cambiado a removeLast()
                        if (!etiqueta.equals(etiquetaApertura))
                        {
                            System.out.println("Error: " + etiquetaApertura + " no tiene una etiqueta de cierre.");
                            return false;
                        }
                    }
                }
                else
                { // Etiqueta de apertura
                    pilaEtiquetas.addLast(etiqueta);//Cambiado a addLast()
                }
            }
        }
        if (!pilaEtiquetas.isEmpty())//Cambiado a isEmpty()
        {
            System.out.println("Error: Hay etiquetas de apertura que no tienen su correspondiente etiqueta de cierre.");
            return false;
        }
        System.out.println("Termino el proceso");
        return true;
    }
    public static String extraerContenidoHTML(String archivo)// Extrae el contenido
    {
        StringBuilder contenido = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(archivo)))
        {
            String linea;
            while ((linea = br.readLine()) != null)
            {
                contenido.append(linea);
            }
        }
        catch (IOException e)
        {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        }
        return contenido.toString();
    }
}
