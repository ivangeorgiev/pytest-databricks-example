import pytest
import os

@pytest.fixture(scope="session", autouse=True)
def _conftest(dbr_client):
    dir_results = os.path.join(os.path.dirname(__file__), '..', 'test-results')
    dbr_client.dir_auto_save = dir_results
    dbr_client.auto_save = True
