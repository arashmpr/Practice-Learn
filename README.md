# Practice-Learn

Goal of this branch is to have a directory sturcture like this:

app/
├── __init__.py
├── config.py
├── extensions.py
├── db.py
│
├── models/
│   ├── __init__.py
│   ├── User.py
│   ├── Word.py
│   ├── Question.py
│   ├── Practice.py
│   ├── PracticeSession.py          # New model
│   └── PracticeResult.py           # New model
│
├── services/
│   ├── __init__.py
│   ├── practice_service.py         # Main practice business logic
│   ├── question_service.py         # Question generation & management
│   ├── user_service.py             # User-related operations
│   ├── analytics_service.py        # Analytics & reporting
│   └── notification_service.py     # Notifications (optional)
│
├── repositories/
│   ├── __init__.py
│   ├── practice_repository.py      # Database operations for practice
│   ├── question_repository.py      # Database operations for questions
│   └── user_repository.py          # Database operations for users
│
├── blueprints/                     # Renamed from individual blueprint folders
│   ├── __init__.py
│   │
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   ├── practice/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── utils.py
│   │
│   ├── user/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── forms.py
│   │
│   └── main/
│       ├── __init__.py
│       └── routes.py
│
├── schemas/                        # For API validation (optional)
│   ├── __init__.py
│   ├── practice_schemas.py
│   └── user_schemas.py
│
├── utils/
│   ├── __init__.py
│   ├── decorators.py              # Custom decorators
│   ├── validators.py              # Custom validators
│   ├── helpers.py                 # Utility functions
│   └── exceptions.py              # Custom exceptions
│
├── templates/
│   ├── base.html
│   ├── errors/
│   │   ├── 404.html
│   │   └── 500.html
│   │
│   ├── auth/
│   │   ├── login.html
│   │   └── register.html
│   │
│   ├── practice/
│   │   ├── list.html
│   │   ├── history.html
│   │   ├── article-single-choice.html
│   │   ├── article-text-input.html
│   │   ├── plural-text-input.html
│   │   ├── definition-text-input.html
│   │   └── results.html
│   │
│   └── user/
│       └── profile.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── migrations/                     # Database migrations
│   └── versions/
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_models/
│   ├── test_services/
│   ├── test_repositories/
│   └── test_routes/
│
└── cli/                           # Custom CLI commands
    ├── __init__.py
    └── commands.py

# Root directory structure:
project_root/
├── app/                           # Main application package
├── migrations/                    # Database migrations (if using Flask-Migrate)
├── tests/                         # Test files
├── data/                          # Data files (CSV, JSON, etc.)
├── logs/                          # Log files
├── instance/                      # Instance-specific config
├── requirements.txt               # Python dependencies
├── .env                          # Environment variables
├── .env.example                  # Example environment file
├── .gitignore
├── config.py                     # Application configuration
├── run.py                        # Application entry point
├── wsgi.py                       # WSGI entry point for production
└── README.md