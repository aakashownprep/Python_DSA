import java.util.Scanner;
class Node{
    int info;
    Node link;
}
public class LinkedList{
   static Node start=null;
   static  Scanner s1=new Scanner(System.in); 
   public static Node creatNode()
   {
    return new Node();
   }
   public static void insertNode()
   {
        Node temp=creatNode();
System.out.println("Enter any number");
temp.info=s1.nextInt();
temp.link=null; 
if(start==null)
{start=temp;}
else{
    Node t1=start;
    while(t1.link!=null)
    {t1=t1.link;}

}

   }
   public static void deleteNode()
   { if(start==null)
   {System.out.println("List is empty");}
   else{start=start.link;}
     
   }

   public static void printList()
   {
        if(start==null)
        {System.out.println("List is empty");}
        else{
            Node t2=start;
            while(t2!=null)
            {
                System.out.println(t2.info+" ");
                t2=t2.link;
            }
            System.out.println();
        }
    
   }
   public staic int menu1()
   {
    System.out.println("1.Add element\n2.Delete element\n3.Print\n4.Exit.\n");
    System.out.println("Enter yopur choice:");
    return s1.nextInt();
   }
   public static void main(String[] args) {
       while(1)
       {
        switch(menu1())
        {
            case 1:insertNode();break;
                case 2:deleteNode();break;
                    case 3:printList();break;
                        case 4:System.exit(0);
                            default:
                                System.out.println("invalid choice:");
        }
       }
   }
}