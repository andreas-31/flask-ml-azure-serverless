# https://www.tutorialspoint.com/pytest/pytest_parameterizing_tests.htm
# https://stanford-code-the-change-guides.readthedocs.io/en/latest/guide_flask_unit_testing.html

import pytest
import os, sys
# extend system path with directory containing the Flask app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.fixture
def client():
    """Configures the app for testing
    Sets app config variable ``TESTING`` to ``True``
    :return: App for testing
    """
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

@pytest.fixture
def my_html():
    return '<h3>Sklearn Prediction Home</h3>'

@pytest.fixture
def my_prediction():
    return {"prediction":[20.35373177134412]}
