from database import create_tables, add_user, authenticate_user, add_book, search_books, list_all_books, delete_all_books

def test_database():
    print("=== Database Test ===")

    # Step 1: Create Tables
    print("Creating tables...")
    create_tables()
    print("Tables created successfully.")

    # Step 2: Test User Registration
    print("\nTesting user registration...")
    if add_user("testuser", "password123"):
        print("User 'testuser' added successfully.")
    else:
        print("Failed to add user 'testuser' (duplicate user).")

    # Step 3: Test User Authentication
    print("\nTesting user authentication...")
    if authenticate_user("testuser", "password123"):
        print("User 'testuser' authenticated successfully.")
    else:
        print("Failed to authenticate 'testuser'.")

    # Step 4: Test Adding Books
    print("\nTesting book addition...")
    add_book("1984", "George Orwell", 1949)
    add_book("To Kill a Mockingbird", "Harper Lee", 1960)
    print("Books added successfully.")

    # Step 5: Test Searching Books
    print("\nTesting book search...")
    results = search_books("1984")
    print(f"Search results for '1984': {results}")

    results = search_books("George")
    print(f"Search results for 'George': {results}")

    # Step 6: Test Listing All Books
    print("\nListing all books...")
    all_books = list_all_books()
    print(f"All books: {all_books}")

    # Step 7: Test Deleting All Books
    print("\nDeleting all books...")
    delete_all_books()
    print("All books deleted successfully.")

    # Step 8: Verify Deletion
    print("\nVerifying deletion...")
    all_books = list_all_books()
    print(f"Books after deletion: {all_books}")

if __name__ == "__main__":
    test_database()
