# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.from sentence_transformers import SentenceTransformer
import requests

from services.LlmService import LlmService


def main():
    llm_service = LlmService('http://localhost:5000/api')
    print(llm_service.chat("Print the sum of the first 5 elements of the fibonacci series. Output the ", system_prompt="The user will give you a request for a problem. Implement the problem in python and output the code. Do not output a code block, other messages, quotes, backticks or similar. Output purely the content of the python script like you would write it in a file."))
    print(llm_service.generate("Generate a random number.", system_prompt="Output what the user tells you to in a format like {\"output\": <output>}"))

if __name__ == '__main__':
    main()