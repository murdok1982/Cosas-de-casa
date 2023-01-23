import requests
import json

def scan_file(file_path, api_key):
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    params = {"apikey": api_key}
    files = {"file": (file_path, open(file_path, "rb"))}
    response = requests.post(url, files=files, params=params)
    json_response = json.loads(response.text)
    return json_response

def get_scan_report(file_hash, api_key):
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    params = {"apikey": api_key, "resource": file_hash}
    response = requests.get(url, params=params)
    json_response = json.loads(response.text)
    return json_response

api_key = "your_api_key"
file_path = "path/to/file.exe"

scan_response = scan_file(file_path, api_key)
if "resource" in scan_response:
    file_hash = scan_response["resource"]
    report_response = get_scan_report(file_hash, api_key)
    if "scans" in report_response:
        scan_results = report_response["scans"]
        for scanner, result in scan_results.items():
            if result["detected"] and result["result"] != None:
                print(f"{file_path} is detected as {result['result']} by {scanner}")
            else:
                print(f"{file_path} is not detected as malware by {scanner}")

