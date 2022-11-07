import requests
import os.path as osp
try:
    import json

    decode_error = json.decoder.JSONDecodeError or errors.JSONDecodeError

    import orjson as json

    USE_ORJSON = True
except Exception as e:
    import json

    USE_ORJSON = False
    print("orJson not found. Using json.")

INFERENCE_URL = 'http://0.0.0.0:8888'

def get(url: str, data: dict, headers: dict = {}):
    data_str = data
    if data:
        data_str = json.dumps(data)
    response = requests.get(url, headers=headers, data=data_str)
    response_dict = parse_response(response)

    return response_dict

def parse_response(response: requests.models.Response) -> dict:
    try:
        response_dict = response.json()
    except decode_error:
        response_dict = {}
    if response.status_code != 200:
        detail = "No detail"
        if "detail" in response_dict:
            detail = response_dict["detail"]
        raise Exception(f"Error: {response.status_code} - {response.text} - {detail}")

    return response_dict

def sample_inference(input_data, type_='json'):
    url = osp.join(INFERENCE_URL, 'txt2img')
    response = get(url, headers={'content-type': f'application/{type_}'}, data=input_data)

    return response

input_data = {"text":'astronaut rides a horse.'}
response = sample_inference(input_data)

print(response)

