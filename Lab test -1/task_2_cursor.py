def recommend_books_by_genre(preferred_genre):
    # Dictionary mapping genres to a list of recommended books
    genre_to_books = {
        'maths': ['RD Sharma', 'NCERT Mathematics', 'RS Aggarwal'],
        'mathematics': ['RD Sharma', 'NCERT Mathematics', 'RS Aggarwal'],
        'physics': ['Physics Wallah', 'HC Verma', 'Resnick Halliday'],
        'chemistry': ['O.P. Tandon', 'Pradeep\'s Chemistry', 'Modern ABC Chemistry'],
        'biology': ['Trueman\'s Biology', 'Pradeep\'s Biology', 'NCERT Biology'],
        'english': ['Wren & Martin', 'Word Power Made Easy', 'High School English Grammar'],
        'computer science': ['Let Us C by Yashavant Kanetkar', 'Introduction to Algorithms', 'Python Crash Course'],
        'history': ['NCERT History', 'India\'s Struggle for Independence', 'History of Modern India'],
        'geography': ['Oxford School Atlas', 'NCERT Geography', 'Certificate Physical and Human Geography'],
        'economics': ['S. Chand Economics', 'NCERT Economics', 'Principles of Economics']
    }
    genre = preferred_genre.strip().lower()
    recommendations = genre_to_books.get(genre)
    if recommendations:
        return f"Recommended books for {preferred_genre}:\n" + "\n".join(recommendations)
    else:
        return "Sorry, we have no recommendations for that genre."

# Example usage:
if __name__ == "__main__":
    user_genre = input("Enter your preferred genre: ")
    print(recommend_books_by_genre(user_genre))
