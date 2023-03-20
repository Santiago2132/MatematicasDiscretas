import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import javax.swing.*;

public class RestauranteGUI extends JFrame
{
    
    public RestauranteGUI()
    {
        initComponents();
    }
    
    private void initComponents()
    {
        // Configurar el JFrame
        this.setTitle("Restaurante");
        this.setSize(new Dimension(1280, 720)); 
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Crear un panel para la sección de búsqueda
        JPanel busquedaPanel = new JPanel();
        JLabel busquedaLabel = new JLabel("Buscar comida:");
        JTextField busquedaTextField = new JTextField(20);
        JButton buscarButton = new JButton("Buscar");
        buscarButton.setBackground(Color.GREEN); // color azul
        buscarButton.setForeground(Color.WHITE); // texto blanco
        buscarButton.setPreferredSize(new Dimension(120, 40)); // tamaño grande
        busquedaPanel.add(busquedaLabel);
        busquedaPanel.add(busquedaTextField);
        busquedaPanel.add(buscarButton);
        
        // Crear un panel para la sección de comida reciente
        JPanel comidaRecientePanel = new JPanel();
        JLabel comidaRecienteLabel = new JLabel("Comida reciente:");
        JList<String> comidaRecienteList = new JList<>(new String[] {"Comida 1", "Comida 2", "Comida 3"});
        comidaRecientePanel.add(comidaRecienteLabel);
        comidaRecientePanel.add(comidaRecienteList);
        
        // Crear un panel para la sección de menú
        JPanel menuPanel = new JPanel();
        JLabel menuLabel = new JLabel("Menú:");
        JTable menuTable = new JTable(new Object[][]{{"Comida 1", "$10"}, {"Comida 2", "$15"}, {"Comida 3", "$20"}}, new Object[]{"Comida", "Precio"});
        menuTable.setPreferredScrollableViewportSize(new Dimension(500, 70));
        JScrollPane menuScrollPane = new JScrollPane(menuTable);
        menuPanel.add(menuLabel);
        menuPanel.add(menuScrollPane);
        
        // Agregar los paneles al JFrame
        this.getContentPane().setLayout(new BorderLayout());
        this.getContentPane().add(busquedaPanel, BorderLayout.NORTH);
        this.getContentPane().add(comidaRecientePanel, BorderLayout.WEST);
        this.getContentPane().add(menuPanel, BorderLayout.CENTER);
    }
    
    public static void main(String[] args) {
        RestauranteGUI gui = new RestauranteGUI();
        gui.setVisible(true);
    }
}
