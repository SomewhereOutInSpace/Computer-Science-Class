import javax.swing.JOptionPane;
public class Driver {
    public static void main (String[] args){
        String name = JOptionPane.showInputDialog("What is your name?");
        System.out.println("Hello " + name +"!");
    }
}