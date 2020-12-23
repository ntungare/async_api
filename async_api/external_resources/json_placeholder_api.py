from typing import Dict, Optional, Union

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json_data(endpoint: str, content_id: Optional[Union[str, int]] = None) -> Dict:
    url_segments = [BASE_URL, endpoint]
    if content_id:
        url_segments.append(str(content_id))

    response = requests.get("/".join(url_segments))

    response_data = response.json()

    return response_data
