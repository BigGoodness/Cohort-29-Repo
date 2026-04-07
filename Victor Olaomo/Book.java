public class Book {

    private String title;
    private String authorFirstName;
    private String authorLastName;
    private String nickName;
    private String numberOfPages;

    public Book(String title, String authorFirstName, String authorLastName, String numberOfPages) {
        this.title = title;
        this.authorFirstName = authorFirstName;
        this.authorLastName = authorLastName;
        this.numberOfPages = numberOfPages;
        this.nickName = nickName;
    }

    public String getTitle()           { return title; }
    public String getAuthorFirstName() { return authorFirstName; }
    public String getAuthorLastName()  { return authorLastName; }
    public String nickName()           { return nickName; }
    public String getNumberOfPages()   { return numberOfPages; }
    
    
}
