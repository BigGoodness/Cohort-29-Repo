import java.util.ArrayList;
import java.util.List;

public class BookSystem {

    private final List<Book> bookStore;

    public BookSystem() {
        this.bookStore = new ArrayList<>();  
    }

    public boolean addBook(Book book) {
        if (book != null) {         
            bookStore.add(book);
            return true;
        }
        return false;
    }

    public boolean removeBook(Book book) {
        bookStore.remove(book);
    }

    public void updateBook(int index, Book book) {
        bookStore.set(index, book);  
    }

    public Book getABook(int index) {
        return bookStore.get(index); 
    }

    public List<Book> getAllBooks() {
        return bookStore;            
    }
}
