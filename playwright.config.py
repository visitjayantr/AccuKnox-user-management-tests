# playwright.config.py

import os
from playwright.sync_api import Playwright, sync_playwright

# Playwright test config dictionary
config = {
    "timeout": 30000,  # 30 seconds max per action
    "test_dir": "tests",  # directory containing your test files
    "reporter": [["list"], ["html", {"outputFolder": "playwright-report"}]],
    "use": {
        "headless": True,  # set to False if you want to see the browser
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        "video": "retain-on-failure",  # record video only on test failures
        "screenshot": "only-on-failure",
        "action_timeout": 10000,
    },
    "projects": [
        {
            "name": "chromium",
            "use": {"browser_name": "chromium"},
        },
        {
            "name": "firefox",
            "use": {"browser_name": "firefox"},
        },
        {
            "name": "webkit",
            "use": {"browser_name": "webkit"},
        },
    ],
    "workers": 2,  # number of parallel test workers
}

def pytest_configure(config_):
    # You can add pytest configuration here if needed
    pass
