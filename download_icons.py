import os
import requests

# Diccionario de categorías con nombre: URL oficial del icono
ICONS = {
    "languages": {
        "javascript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
        "typescript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg",
        "python": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        "php": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg",
        "csharp": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg",
        "kotlin": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg",
    },
    "frontend": {
        "react": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg",
        "nextjs": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg",
        "redux": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg",
        "tailwind": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg",
        "expo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/expo/expo-original.svg",
    },
    "backend": {
        "nodejs": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg",
        "dotnet": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg",
        "fastapi": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg",
    },
    "cloud": {
        "azure": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg",
        "firebase": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg",
    },
    "databases": {
        "mysql": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg",
        "postgresql": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg",
        "mongodb": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg",
        "redis": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg",
    },
    "testing": {
        "jest": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jest/jest-plain.svg",
        "cypress": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cypressio/cypressio-original.svg",
    },
    "tools": {
        "docker": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg",
        "git": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
        # PowerBI no existe en devicon -> podemos incluir luego desde su oficial
    },
}


def download_icons(base_dir="icons"):
    """Descarga íconos SVG organizados por categoría"""
    for category, icons in ICONS.items():
        category_path = os.path.join(base_dir, category)
        os.makedirs(category_path, exist_ok=True)

        for name, url in icons.items():
            file_path = os.path.join(category_path, f"{name}.svg")
            try:
                print(f"⬇️ Descargando {name}...")
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"✅ Guardado en {file_path}")
            except Exception as e:
                print(f"❌ Error al descargar {name}: {e}")


if __name__ == "__main__":
    download_icons()
