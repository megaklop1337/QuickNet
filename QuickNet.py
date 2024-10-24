import os
import requests
import zipfile
import subprocess

# Конфигурация
REPO_URL = "https://github.com/megaklop1337/Files/raw/refs/heads/main/git.zip"  # Замените на URL вашего репозитория
VERSION_URL = "https://raw.githubusercontent.com/megaklop1337/Files/refs/heads/main/version.txt"  # URL для версии
LOCAL_VERSION_FILE = "version.txt"
LOCAL_REPO_DIR = "repository"
BATCH_SCRIPT = "123.bat"  # Убедитесь, что имя .bat файла правильное

def download_version():
    response = requests.get(VERSION_URL)
    with open(LOCAL_VERSION_FILE, 'w') as version_file:
        version_file.write(response.text.strip())

def get_local_version():
    if os.path.exists(LOCAL_VERSION_FILE):
        with open(LOCAL_VERSION_FILE, 'r') as version_file:
            return version_file.read().strip()
    return None

def download_repository():
    zip_file_path = "repo.zip"
    response = requests.get(REPO_URL)

    if response.status_code == 200:
        with open(zip_file_path, 'wb') as zip_file:
            zip_file.write(response.content)
    else:
        print("Site Error:", response.status_code)
        return

    # Разархивирование
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(".")

    # Переименуйте извлеченную папку
    extracted_folder_name = os.path.basename(REPO_URL).replace('.zip', '')
    if os.path.exists(extracted_folder_name):
        os.rename(extracted_folder_name, LOCAL_REPO_DIR)

def run_batch_script():
    # Полный путь к .bat файлу
    bat_file_path = os.path.join(BATCH_SCRIPT)
    
    # Проверка, существует ли файл
    if not os.path.exists(bat_file_path):
        print(f"Error #2")
        return False

    # Запуск .bat файла и ожидание его завершения
    process = subprocess.run(bat_file_path, shell=True)
    return process.returncode == 0  # Успех, если код возврата 0

def main():
    download_version()
    local_version = get_local_version()

    download_repository()

    if run_batch_script():
        print("Success")
    else:
        print("Error #1")


if __name__ == "__main__":
    main()