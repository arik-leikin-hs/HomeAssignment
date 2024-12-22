# Candidate Data Processing Script

This Python script is designed to fetch, process, and display candidate data from a given URL. It consists of three main steps: data extraction, data transformation, and output generation.

## Overview

The script performs the following operations:

1. **Data Extraction**: Fetches raw candidate data from a given URL using the `DataExtractor` class.
2. **Data Transformation**: Processes the raw data to extract and structure the relevant information using the `DataTransformer` class.
3. **Output Generation**: Displays the processed data on the console using the `OutputGenerator` class.

### Design Decisions

The implementation was divided into three core components to ensure clarity, maintainability, and scalability:

- **Data Extraction**:  
  The `DataExtractor` class fetches raw data from a given source, such as a URL, text file, or JSON file. This modular design allows for easy extension to support different data sources without affecting other parts of the application.

- **Data Transformation**:  
  The `DataTransformer` class processes and structures the data. Isolating this logic makes it easier to maintain and adapt if the data format changes.

- **Output Generation**:  
  The `OutputGenerator` class handles displaying the processed data. This separation allows for easy adjustments to how data is presented (e.g., in a GUI or file export) without impacting data extraction or transformation.

This separation of concerns follows the principles of modular design, allowing each class to focus on a specific task and making it easier to maintain and extend the application in the future.


## Requirements

No external libraries or dependencies are required to run this script. It uses only standard Python libraries.


## Usage

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```html
git clone "https://github.com/arik-leikin-hs/HomeAssignment.git"
```

### Step 2: Modify the URL

If you would like to fetch data from a different URL, open the main.py file and locate the following line:
```html
CANDIDATES_URL = "<URL-SAMPLE>"
```


### Step 3: Run the Script
```bash
python main.py
```


