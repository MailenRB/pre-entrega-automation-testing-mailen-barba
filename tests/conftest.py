import os
import sys
import pytest
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_factory import get_chrome_driver

@pytest.fixture(scope="function")
def driver():
    driver_instance = get_chrome_driver()
    yield driver_instance
    driver_instance.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            reports_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports"))
            screenshots_dir = os.path.join(reports_dir, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            
            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_filename = f"{test_name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)
            
            driver_fixture.save_screenshot(screenshot_path)
            
            html = (
                f'<div><img src="screenshots/{screenshot_filename}" alt="screenshot" '
                f'style="width:400px;height:225px;border:1px solid #ccc;border-radius:4px;cursor:pointer;" '
                f'onclick="window.open(this.src)" align="right"/></div>'
            )
            
            extra = getattr(report, "extra", [])
            try:
                import pytest_html
                extra.append(pytest_html.extras.html(html))
                report.extra = extra
            except ImportError:
                pass
