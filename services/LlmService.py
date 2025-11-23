# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.import json

import requests


class LlmService:
    __url = None

    def __init__(self, url):
        self.__url = url

    def chat(self, user_prompt, system_prompt=None, attachments=None):
        body = {
            "model": "llama3.1",
            "messages": [],
        }

        if system_prompt is not None:
            body["messages"].append({
                "role": "system",
                "content": system_prompt
            })

        body["messages"].append({
            "role": "user",
            "content": user_prompt
        })

        resp = requests.post(
            self.__url + "/chat",
            json=body,
        )

        response = json.loads(resp.text)
        return response

    def generate(self, user_prompt, system_prompt=None, attachments=None, temperature=None):
        body = {
            "model": "llama3.1",
            "keep_alive": "1m",
            "format": "json",
            "options": {},
            "prompt": user_prompt,
            "template": "{{ .System }}\n{{ .Prompt }}",
        }

        if temperature is not None:
            body["options"]["temperature"] = temperature
        if system_prompt is not None:
            body["system"] = system_prompt

        resp = requests.post(
            self.__url + "/generate",
            json=body,
        )

        response = json.loads(resp.text)
        return response
