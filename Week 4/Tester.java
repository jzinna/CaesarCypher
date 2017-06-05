
/**
 * Write a description of Tester here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
import java.lang.*;
import java.util.*;
import edu.duke.*;
public class Tester {

    public void testSliceString(){
        VigenereBreaker vb = new VigenereBreaker ();
        String result = vb.sliceString("abcdefghijklm", 2, 5);
        System.out.println(result);
    }
    
    public void testKeyLength(){
        VigenereBreaker vb = new VigenereBreaker();
        FileResource file = new FileResource("secretmessage1.txt");
        int [] result = vb.tryKeyLength(file.asString(),4,'e');
        for (int k=0; k<result.length;k++){
            System.out.println(result[k]);
        }
    }
    
    public void testReadDict(){
        VigenereBreaker vb = new VigenereBreaker();
        FileResource fr = new FileResource();
        vb.readDictionary(fr);
    }
    
    public void testBreaker(){
        VigenereBreaker vb = new VigenereBreaker();
        FileResource fr = new FileResource();
        HashSet<String> hshst = vb.readDictionary(fr);
        FileResource file = new FileResource("athens_keyflute.txt");
        String message=file.asString();
        System.out.println(vb.countWords(message,hshst));
        //System.out.println(vb.breakForLanguage(message,hshst));
    }
    
    public void testSplit(){
        String message = ("This is the message to split!");
        String[] splitMsg= message.split("//W+");
        for (int k=0; k<splitMsg.length;k++){
            System.out.println(splitMsg[k]);
        }
        /*/String[] splitMsg = message.split(" ");
            for (int k=0; k<splitMsg.length;k++){
                System.out.println(splitMsg[k]);
            }*/
    }
    
    public void testCommonChar(){
        VigenereBreaker vb = new VigenereBreaker();
        FileResource fr = new FileResource();
        HashSet<String> dictionary = vb.readDictionary(fr);        
        System.out.println(vb.mostCommonCharIn(dictionary));
    }
}
