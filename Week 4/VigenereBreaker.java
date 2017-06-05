import java.util.*;
import edu.duke.*;
import java.lang.*;
import java.io.*;

public class VigenereBreaker {
    public String sliceString(String message, int whichSlice, int totalSlices) {
        StringBuilder SBresult = new StringBuilder();
        int m = whichSlice;
        while (m < message.length()){
            char c = message.charAt(m);
            SBresult.append(c);
            m = m + totalSlices;
        }
        String result = SBresult.toString();
        return result;

    }

    public int[] tryKeyLength(String encrypted, int klength, char mostCommon) {
        int[] key = new int[klength];
        CaesarCracker cc = new CaesarCracker(mostCommon);
        //use getKey from caaesarcracker
        //use slicestring
        for (int k = 0; k< klength; k++){
            String current = sliceString(encrypted, k, klength);
            int currKey = cc.getKey(current);
            key[k]= currKey;
        }
        return key;
    }

    public void breakVigenere () {
        FileResource frEncrypted = new FileResource();
        String flAsStrng = frEncrypted.asString();
        DirectoryResource dr= new DirectoryResource();   
        HashMap<String,HashSet<String>> languages = new HashMap<String,HashSet<String>> ();
        for(File f : dr.selectedFiles()){
            String lang = f.getName();
            FileResource frDict = new FileResource (f);
            HashSet<String> hs = readDictionary(frDict);
            languages.put(lang,hs);
        }
        breakForAllLangs(flAsStrng,languages);
    }


    public HashSet<String> readDictionary(FileResource fr){
        //  make Hashset of strings
        HashSet<String> hs = new HashSet<String>();
        //  read each line in fr (one word per line)
        for (String line : fr.lines()){
            //  convert line to lower case
            line.toLowerCase();
            //  put line into hashset
            hs.add(line);
        }
        //  return the hashset representing the words in a dictionary
        return hs;
    }
    
    public int countWords(String message, HashSet<String> dictionary){
        //  split the message into words (with .split("\\W+"), which returns a String array)
        String[] msgAsWds = message.split("\\W+");
        int count=0;
        //  iterate, see how many are real words by looking for them in the dictionary (convert to lowercase first)
        for (int k=0; k<msgAsWds.length; k++){
            String word = msgAsWds[k];
            word=word.toLowerCase();
            if (dictionary.contains(word)){
                count=count+1;
            }
        }
        //  returns the integer representing how many valid words it found
        return count;
    }
    
    public String breakForLanguage(String encrypted, HashSet<String> dictionary){
        int maxCount=0;
        String decryption=null;
        char c=mostCommonCharIn(dictionary);
        for (int k=1;k<101;k++){
            int[] currKey = tryKeyLength(encrypted, k, c);
            VigenereCipher vc= new VigenereCipher(currKey);
            String currDecrypt=vc.decrypt(encrypted);
            int count = countWords(currDecrypt,dictionary);
            if (count>maxCount){
                maxCount=count;
                decryption=currDecrypt;
            }
        }
        return decryption;
    }
    
    public char mostCommonCharIn(HashSet<String> dictionary){
        //  find out which character is the most common in the dictionary
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        for (String word : dictionary){
            for (int k=0;k<word.length();k++){
                char currChar = word.charAt(k);
                if(hm.containsKey(currChar)){
                    int count = hm.get(currChar);
                    count = count+1;
                    hm.put(currChar,count);
                }
                else{
                    hm.put(currChar,1);
                }
            }
        }
        int max=0;
        char result=' ';
        for(char c : hm.keySet()){
            int currCount = hm.get(c);
            if(currCount>max){
                max=currCount;
                result = c;
            }
        }
        return result;
    }
    
    public void breakForAllLangs(String encrypted,HashMap<String,HashSet<String>> languages){
        //  the hashmap provided maps the name of a language to the hashset containing the words of that language (the dictionary)
        //  break the encryption for each language, and determine which has the best results
        //  iterate over the languages keySet to get the name of the language and use .get to use the corresponding dictionary
        int maxCount = 0;
        String bestLang = null;
        String bestDecryption=null;
        for (String lang : languages.keySet()){
            HashSet<String> currDict = languages.get(lang);
            String message = breakForLanguage(encrypted, currDict);
            int currCount = countWords(message, currDict);
            if(currCount>maxCount){
                maxCount=currCount;
                bestLang=lang;
                bestDecryption=message;
            }
        }
        //  print decrypted message and language
        System.out.println("The decrypted message is: "+bestDecryption+" and it's written in "+bestLang);
    }
}
