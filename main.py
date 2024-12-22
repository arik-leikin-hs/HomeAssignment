from DataExtractor import DataExtractor
from DataTransformer import DataTransformer
from OutputGenerator import OutputGenerator


def testing():
    jsonFile = "mock_data_with_edge_cases.json"
    extractor = DataExtractor()
    raw_data = extractor.fetch_data_json(jsonFile)

    transformer = DataTransformer(raw_data)
    processed_data = transformer.process_candidates()

    OutputGenerator.print_to_console(processed_data)


def main():
    CANDIDATES_URL = "https://hs-recruiting-test-resume-data.s3.amazonaws.com/allcands-full-api_hub_b1f6-acde48001122.json"

    # Step 1: Extraction
    extractor = DataExtractor()
    raw_data = extractor.fetch_data_url(CANDIDATES_URL)

    # Step 2: Transformation
    transformer = DataTransformer(raw_data)
    processed_data = transformer.process_candidates()

    # Step 3: Print
    OutputGenerator.print_to_console(processed_data)

if __name__ == '__main__':
    main()
