
# iOSUICatalogAutomation

Automation Framework for iOS app of [UICatalog](https://github.com/appium/ios-uicatalog), where It has covered almost all important features of DatePicker, Sliders, TextFields and Search Fields. 


Note: since iOS app, so it can be automated in Mac OSX only.





## Tech Stack

**Client:** Python3

**Server:** Appium


## Features

- Automation of iOS app using pytest framework
- Generate Logs in ```Logs``` folder
- Generate Allure Reports



## Installation and Execution

Install my-project with npm

```bash
  git clone https://github.com/taimoorpashanbs17/iOSUICatalogAutomation.git
```
Navigate to Folder

```bash
  cd iOSUICatalogAutomation
```

Install Virtual Environment
```bash
  python3 -m pip install --user virtualenv

```

Create Virtual Environment
```bash
  python3 -m venv env

```

Install all dependencies
```bash
  pip install -r requirements.txt

```


## Running Tests

After Installation, Ran any test suit within ```TestCases```folder, by using 

```bash
  pytest test_text_fields.py -s -v

```

or Run all test cases within ```TestCases```folder, by:
```bash
  pytest -s -v

```

## Generating Allure Report

In Order to generate Allure Reports, run following command:
```bash
  pytest -s -v --alluredir="../allure-reports"

```


## Report 

### Allure Report

![Allure Report](/Users/tp/Desktop/Screenshot 2023-02-20 at 11.10.34 PM.png?raw=true "Title")


### Jenkins View
![Jenkins Report](/Users/tp/Desktop/Screenshot 2023-02-20 at 11.20.25 PM.png?raw=true "Title")

### Loom Link
https://www.loom.com/share/acf5787803c640e19086d43ba0ee3a06

## 🔗 Get In Touch with me
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/taimoor-pasha-a2294878/)





## Acknowledgements
I have created this framework, with [Rahul Shetty's Course of - Appium - Mobile App Automation in Python (Basics + Advance)
](https://www.udemy.com/course/appium-with-python-tutorial/)


