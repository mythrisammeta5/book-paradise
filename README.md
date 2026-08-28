# Book Paradise - Smart Library Management & Book Rental Platform

**Your Reading Paradise Awaits**

A complete full-stack web application for book rental, library management, rewards, and reading games.

## Features

✅ **Book Discovery & Management**
- Browse thousands of books
- Search by title, author, category
- Detailed book information and reviews
- Professional book catalog

✅ **Book Rental System**
- Rent books without purchasing
- 7-day default rental period
- Track rental status and due dates
- Calculate and track fines for overdue books
- Return books with ease

✅ **Personal Library**
- View current rentals
- See rental history
- Manage wishlist
- Track reading progress

✅ **Study in Library**
- Book study seats
- Choose quiet zones or group study areas
- Select date and time slots
- View availability

✅ **Home Delivery**
- Request home delivery
- Cash on delivery payment
- Track delivery status

✅ **Rewards System**
- Earn points from rentals and games
- Collect badges
- Unlock discounts
- View reward history

✅ **Reading Games**
- Quiz Challenge
- Rapid Fire Questions
- Memory Match Game
- Earn points and achievements

✅ **AI Reading Assistant**
- Smart book recommendations
- Answer reading-related queries
- Fallback rule-based suggestions

✅ **User Profiles**
- Personal dashboard
- Track reading statistics
- Manage preferences
- View achievements

✅ **Admin Panel**
- Manage books
- View users and rentals
- Monitor library operations

## Technologies

**Backend**
- Python 3.8+
- Flask
- SQLAlchemy ORM
- Werkzeug (security)

**Frontend**
- HTML5
- CSS3
- JavaScript (ES6+)
- Responsive Design

**Database**
- MySQL 5.7+
- SQLAlchemy ORM

**Other**
- Python-dotenv (environment variables)
- Flask-MySQLdb

## Project Structure

```
book-paradise/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth.py
│   ├── books.py
│   ├── rentals.py
│   ├── library.py
│   ├── rewards.py
│   ├── games.py
│   ├── ai_assistant.py
│   ├── delivery.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── books.html
│   ├── book_detail.html
│   ├── rentals.html
│   ├── library.html
│   ├── rewards.html
│   ├── games.html
│   ├── ai_assistant.html
│   ├── profile.html
│   ├── wishlist.html
│   ├── admin.html
│   └── errors/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── database/
│   └── schema.sql
├── .env.example
├── .gitignore
├── requirements.txt
├── setup.ps1
├── run.py
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- MySQL 5.7 or higher
- Git

### Windows Setup (PowerShell)

1. **Clone the repository**
   ```powershell
   git clone https://github.com/yourusername/book-paradise.git
   cd book-paradise
   ```

2. **Run the setup script**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .\setup.ps1
   ```

The script will automatically:
- Create virtual environment
- Install dependencies
- Configure .env file
- Setup MySQL database
- Seed sample data
- Start the application

### Manual Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate      # Linux/Mac
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure .env**
   ```bash
   copy .env.example .env
   ```
   Edit `.env` with your MySQL credentials:
   ```
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   DATABASE_USER=root
   DATABASE_PASSWORD=your-password
   DATABASE_NAME=book_paradise
   AI_API_KEY=your-openai-key-optional
   ```

4. **Create MySQL database**
   ```bash
   mysql -u root -p < database/schema.sql
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

## Configuration

### Environment Variables (.env)

Required:
- `FLASK_ENV`: development/production
- `SECRET_KEY`: Flask secret key
- `DATABASE_HOST`: MySQL host
- `DATABASE_PORT`: MySQL port (default 3306)
- `DATABASE_USER`: MySQL username
- `DATABASE_PASSWORD`: MySQL password
- `DATABASE_NAME`: Database name

Optional:
- `AI_API_KEY`: OpenAI API key (for AI assistant)

### Database Setup

1. Create database:
   ```sql
   CREATE DATABASE book_paradise CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. Run schema:
   ```bash
   mysql -u root -p book_paradise < database/schema.sql
   ```

3. Seed data:
   The application automatically seeds sample data on first run.

## Running the Application

```bash
python run.py
```

Access at: `http://127.0.0.1:5000`

## Test Credentials

**Default User:**
- Username: `testuser`
- Email: `test@bookparadise.com`
- Password: `password123`

**Admin User:**
- Username: `admin`
- Email: `admin@bookparadise.com`
- Password: `admin123`

## Test Flow

### User Journey
1. **Home** → Browse featured books
2. **Sign Up** → Create account
3. **Login** → Access personalized features
4. **Books** → Search and explore catalog
5. **Book Details** → View detailed information
6. **Rent Book** → Start rental
7. **My Library** → Track active rentals
8. **Return Book** → Return and pay fines
9. **Rewards** → View points and badges
10. **Games** → Play and earn rewards
11. **Profile** → View statistics
12. **Logout** → End session

### Admin Features
1. **Admin Panel** → Access via /admin (login required)
2. **Add Book** → Create new book entries
3. **Manage Books** → Edit/delete existing books
4. **View Users** → Monitor user accounts
5. **View Rentals** → Track rental activity

## Troubleshooting

### MySQL Connection Error
- Verify MySQL is running
- Check credentials in .env
- Ensure database exists: `CREATE DATABASE book_paradise;`

### Port Already in Use
- Change port in run.py
- Or kill process: `netstat -ano | findstr :5000`

### Module Not Found
- Activate virtual environment
- Reinstall requirements: `pip install -r requirements.txt`

### Database Schema Error
- Drop and recreate database
- Rerun schema.sql

## Security

- Passwords hashed with Werkzeug
- Flask sessions for authentication
- Environment variables for secrets
- SQL injection prevention via SQLAlchemy
- CSRF protection on forms
- Admin route protection

## File Sizes

All files are optimized for GitHub:
- No large binary files
- Placeholder images only
- Seed data included
- Clean code structure

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - see LICENSE file

## Support

For issues and questions:
- GitHub Issues
- Email: support@bookparadise.com

---

**Book Paradise** - Your Reading Paradise Awaits ✨📚
