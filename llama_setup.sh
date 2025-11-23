# This file is licensed under the GNU General Public License v3.0 (GPLv3).
# See the LICENSE file or https://www.gnu.org/licenses/ for details.apt-update
apt install lshw curl

curl -sSL https://ollama.com/download/linux | sudo sh

ollama pull llama3.1D

ollama serve &
python3 /workspace/proxy.py