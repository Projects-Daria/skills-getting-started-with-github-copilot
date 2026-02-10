import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for intramural and regional play",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Learn tennis skills and participate in friendly matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
            "max_participants": 10,
            "participants": ["lucas@mergington.edu", "grace@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and visual arts techniques",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["isabella@mergington.edu"]
        },
        "Music Ensemble": {
            "description": "Join our orchestra and perform classical and modern pieces",
            "schedule": "Mondays and Fridays, 4:00 PM - 5:30 PM",
            "max_participants": 25,
            "participants": ["noah@mergington.edu", "ava@mergington.edu", "mason@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and critical thinking through competitive debate",
            "schedule": "Tuesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["liam@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore STEM topics through hands-on projects",
            "schedule": "Thursdays, 3:30 PM - 4:45 PM",
            "max_participants": 22,
            "participants": ["chloe@mergington.edu", "ethan@mergington.edu"]
        }
    }
    yield original_activities
    # Cleanup - restore original activities after test
    activities.clear()
    activities.update(original_activities)
