import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    app = Application(browser="chrome", base_url="http://45.150.8.53/")
    app.initialize()

    def finalize():
        app.destroy()

    request.addfinalizer(finalize)
    return app
