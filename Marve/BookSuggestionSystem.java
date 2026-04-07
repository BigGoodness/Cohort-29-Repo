import java.util.Random;
import java.util.ArrayList;

public class BookSuggestionSystem{

    public ArrayList<String> books = new ArrayList<>();

    public void addBook(String bookName) {
        books.add(bookName);
        
    }

    public ArrayList<String> getBooks(){
        return books;
    }

    public String getRandomBook(){

    Random random = new Random();
    return books.get(random.nextInt(books.size()));

    }
    public int generateRandomPage(){
    Random random = new Random();
    return random.nextInt(100) + 1;



        }   
    }

