# `pytest-performancetotal` Demo Project

This repository demonstrates the [pytest-performancetotal](https://pypi.org/project/pytest-performancetotal/) plugin, which enhances pytest with performance testing capabilities. It's compatible with UI and API tests, offering a simple way to measure and analyze response times.

Explore the example provided to see how the plugin can be integrated into your tests. For background on the plugin's development, you can refer to the Node.js version's [documentation](https://www.linkedin.com/pulse/elevating-your-playwright-tests-plugin-tzur-paldi-phd/).

Enjoy exploring the demo!

## Installation

Clone the project from GitHub:

```bash
git clone https://github.com/tzurp/pytest_performancetotal_demo.git
```

To set up the test environment and install all dependencies, run:

```bash
pip install -r requirements.txt
```

Then install Playwright browsers:

```
playwright install
```

## Running the test

To start the test, run:

```bash
pytest -s
```
