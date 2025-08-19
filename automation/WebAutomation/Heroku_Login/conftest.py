import os
import shutil
import pytest
import allure
from selenium import webdriver

'''# Clean allure-results before test run
@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    results_dir = os.path.join(os.getcwd(), "allure-results")
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir, exist_ok=True)'''


@pytest.fixture(scope="function")
def invoke_browser(request):
    """
    Initializes and yields a Chrome driver instance for a test function.
    Attaches the driver to the test node so it can be accessed in hooks.
    Quits the driver after the test is complete.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Attach the driver instance to the test item (node) for access in the hook
    request.node.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to create a test report.
    This implementation attaches a screenshot to the Allure report for
    any test that fails or is broken during its 'setup' or 'call' phase.
    """
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Check if the test is broken and in the 'call' phase
    if report.when == "call" and report.outcome == "broken":
        # Change the outcome to 'failed'
        report.outcome = "failed"
        # Optional: Add a prefix to the failure message for clarity
        if report.longrepr:
            report.longrepr = f"Test was BROKEN, now marked as FAILED.\n\n{report.longrepr}"

    # The 'when' attribute tells us if the failure occurred during setup, call, or teardown
    # We only want screenshots for failures during the main test execution or setup.
    if report.when in ("setup", "call"):
        # The 'failed' attribute is True for both failed and broken tests
        if report.failed:
            # Attempt to retrieve the driver from the test item
            driver = getattr(item, "driver", None)
            if driver:
                try:
                    allure.attach(
                        driver.get_screenshot_as_png(),
                        name=f"screenshot_on_{report.when}_failure",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception as e:
                    print(f"Error taking screenshot: {e}")

    # Save the report to the item for potential access in other hooks
    setattr(item, "rep_" + report.when, report)
