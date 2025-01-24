import pytest
from api_client import YouGileApiClient
import uuid


TOKEN = "bmtbppyXmYxoierwEXdJUgVGe3I1DV2bGTYA-MVWnDMHWcKaQHfgnRVi+HomWYJj"  


@pytest.fixture
def api_client():
    """Фикстура для создания и возврата клиента API."""
    base_url = "https://ru.yougile.com/api-v2"
    client = YouGileApiClient(base_url, TOKEN) 
    return client
    

def generate_unique_name():
    """Генерирует уникальное имя проекта на основе UUID."""
    return f"Test Project {uuid.uuid4()}"

def test_create_project_positive(api_client):
    """Позитивный тест создания проекта."""
    unique_name = generate_unique_name()
    response = api_client.create_project(name=unique_name)
    assert "id" in response
    assert response["name"] == unique_name
    assert response["description"] is None
    assert response["code"] is None


def test_create_project_negative_no_name(api_client):
    """Негативный тест создания проекта без имени."""
    response = api_client.create_project(name=None)
    assert response["code"] == 1000
    assert "name" in response["errors"]

def test_get_projects_positive(api_client):
    """Позитивный тест получения списка проектов."""
    response = api_client.get_projects()
    assert isinstance(response, list)

def test_update_project_positive(api_client):
    """Позитивный тест обновления проекта."""
    unique_name = generate_unique_name()
    create_response = api_client.create_project(name=unique_name)
    project_id = create_response["id"]
    
    updated_name = generate_unique_name()
    update_response = api_client.update_project(project_id, name = updated_name)
    assert update_response["id"] == project_id
    assert update_response["name"] == updated_name


def test_update_project_negative_no_name(api_client):
    """Негативный тест обновления проекта без имени."""
    unique_name = generate_unique_name()
    create_response = api_client.create_project(name=unique_name)
    project_id = create_response["id"]
    
    update_response = api_client.update_project(project_id, name = None)
    assert update_response["code"] == 1000
    assert "name" in update_response["errors"]

def test_get_project_positive(api_client):
    """Позитивный тест получения проекта по id."""
    unique_name = generate_unique_name()
    create_response = api_client.create_project(name=unique_name)
    project_id = create_response["id"]
    
    get_response = api_client.get_project(project_id)
    assert get_response["id"] == project_id
    assert get_response["name"] == unique_name