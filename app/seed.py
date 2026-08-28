from app.extensions import db
from app.models import User, Category, Book
from datetime import datetime

def seed_database():
    """Seed the database with initial data"""
    
    # Create categories
    categories_data = [
        {'name': 'Fiction', 'description': 'Imaginative literary works'},
        {'name': 'Mystery', 'description': 'Detective and mystery novels'},
        {'name': 'Romance', 'description': 'Love and relationship stories'},
        {'name': 'Science', 'description': 'Scientific and educational works'},
        {'name': 'Self Help', 'description': 'Personal development books'},
        {'name': 'Finance', 'description': 'Money and investment guides'},
        {'name': 'Biography', 'description': 'Life stories and memoirs'},
        {'name': 'History', 'description': 'Historical narratives'},
        {'name': 'Technology', 'description': 'Tech and innovation'},
        {'name': 'Education', 'description': 'Learning and academic books'},
    ]
    
    for cat_data in categories_data:
        if not Category.query.filter_by(name=cat_data['name']).first():
            category = Category(**cat_data)
            db.session.add(category)
    
    db.session.commit()
    
    # Create books
    books_data = [
        {
            'title': 'Think Like a Monk',
            'author': 'Jay Shetty',
            'description': 'Train your mind for peace and purpose every day',
            'category_name': 'Self Help',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8386253-M.jpg',
            'rating': 4.6,
            'total_copies': 5,
        },
        {
            'title': 'Rich Dad Poor Dad',
            'author': 'Robert T. Kiyosaki',
            'description': 'What the rich teach their kids about money that the poor and middle class do not',
            'category_name': 'Finance',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/7832656-M.jpg',
            'rating': 4.5,
            'total_copies': 5,
        },
        {
            'title': 'Atomic Habits',
            'author': 'James Clear',
            'description': 'Tiny Changes, Remarkable Results. Build the habits that stick',
            'category_name': 'Self Help',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8367435-M.jpg',
            'rating': 4.7,
            'total_copies': 5,
        },
        {
            'title': 'The Subtle Art of Not Giving a F*ck',
            'author': 'Mark Manson',
            'description': 'A Counterintuitive Approach to Living a Good Life',
            'category_name': 'Self Help',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/7826999-M.jpg',
            'rating': 4.4,
            'total_copies': 5,
        },
        {
            'title': 'The 5 AM Club',
            'author': 'Robin Sharma',
            'description': 'Own Your Morning. Elevate Your Life',
            'category_name': 'Self Help',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/9316903-M.jpg',
            'rating': 4.6,
            'total_copies': 5,
        },
        {
            'title': 'Ikigai',
            'author': 'Héctor García',
            'description': 'The Japanese Secret to a Long and Happy Life',
            'category_name': 'Self Help',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8367435-M.jpg',
            'rating': 4.5,
            'total_copies': 5,
        },
        {
            'title': 'To Kill a Mockingbird',
            'author': 'Harper Lee',
            'description': 'A gripping tale of racial injustice and childhood innocence',
            'category_name': 'Fiction',
            'price': 220.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8206233-M.jpg',
            'rating': 4.8,
            'total_copies': 5,
        },
        {
            'title': 'Sapiens',
            'author': 'Yuval Noah Harari',
            'description': 'A Brief History of Humankind',
            'category_name': 'History',
            'price': 350.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8367435-M.jpg',
            'rating': 4.7,
            'total_copies': 5,
        },
        {
            'title': 'The Alchemist',
            'author': 'Paulo Coelho',
            'description': 'A philosophical fable about following your dreams',
            'category_name': 'Fiction',
            'price': 180.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/7832656-M.jpg',
            'rating': 4.6,
            'total_copies': 5,
        },
        {
            'title': 'The Psychology of Money',
            'author': 'Morgan Housel',
            'description': 'Timeless lessons on wealth, greed, and happiness',
            'category_name': 'Finance',
            'price': 280.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/9316903-M.jpg',
            'rating': 4.6,
            'total_copies': 5,
        },
        {
            'title': 'The Hobbit',
            'author': 'J.R.R. Tolkien',
            'description': 'A fantasy adventure of a reluctant hero',
            'category_name': 'Fiction',
            'price': 250.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8206233-M.jpg',
            'rating': 4.7,
            'total_copies': 5,
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'description': 'A dystopian social science fiction novel',
            'category_name': 'Fiction',
            'price': 200.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/7832656-M.jpg',
            'rating': 4.6,
            'total_copies': 5,
        },
        {
            'title': 'Pride and Prejudice',
            'author': 'Jane Austen',
            'description': 'A timeless romance and social commentary',
            'category_name': 'Romance',
            'price': 180.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/8206233-M.jpg',
            'rating': 4.7,
            'total_copies': 5,
        },
        {
            'title': 'The Book Thief',
            'author': 'Markus Zusak',
            'description': 'A story of a girl who steals books during World War II',
            'category_name': 'Fiction',
            'price': 240.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/7832656-M.jpg',
            'rating': 4.5,
            'total_copies': 5,
        },
        {
            'title': 'Think and Grow Rich',
            'author': 'Napoleon Hill',
            'description': 'The secret to wealth and success',
            'category_name': 'Finance',
            'price': 260.00,
            'cover_url': 'https://covers.openlibrary.org/b/id/9316903-M.jpg',
            'rating': 4.6,
            'total_copies': 5,
        },
    ]
    
    for book_data in books_data:
        category_name = book_data.pop('category_name')
        category = Category.query.filter_by(name=category_name).first()
        
        if not Book.query.filter_by(title=book_data['title']).first():
            book = Book(
                **book_data,
                category_id=category.id,
                available_copies=book_data['total_copies']
            )
            db.session.add(book)
    
    db.session.commit()
    
    # Create test user
    if not User.query.filter_by(username='testuser').first():
        user = User(
            username='testuser',
            email='test@bookparadise.com',
            bio='A passionate reader',
            member_since=datetime.utcnow()
        )
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
