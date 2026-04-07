import java.util.ArrayList;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;


public class BookSuggestionSystemTest{
    @Test
    public void testThatRangeOfThePageNumberIsBetween1And100 (){
    BookSuggestionSystem testing = new BookSuggestionSystem();
    int page = testing.generateRandomPage();
    assertTrue(page >= 1 && page <= 100);
    }
    
    @Test
    public void testThatBooksAreAddedToTheList(){
    BookSuggestionSystem testing = new BookSuggestionSystem();
    ArrayList <String> expected = new ArrayList
    }

    




    }
