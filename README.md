<div align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&pause=1000&color=F7F7F7&background=0D1117&center=true&vCenter=true&width=600&lines=wiener-API;FastAPI+CRUD+%2B+Auth+Backend;Instagram-like+Image+Uploader" alt="wiener-API" />
</a>

<br/>
<br/>

[![Python](https://img.shields.io/badge/Python-3.13%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.135%2B-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-async-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=flat-square&logo=gunicorn&logoColor=white)](https://www.uvicorn.org/)
[![ImageKit](https://img.shields.io/badge/ImageKit-CDN-FF6C2F?style=flat-square&logo=cloudinary&logoColor=white)](https://imagekit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Educational-blueviolet?style=flat-square)]()

</div>

---

> **Educational Project** — This repository is a learning-focused backend project. It is not intended for production use. The goal is to demonstrate API design, authentication management, and CRUD patterns using modern Python tooling.

---

## About

**wiener-API** is a RESTful CRUD backend inspired by Instagram's core flow: users can register, authenticate, and manage images through a clean API. It focuses on backend fundamentals — authentication, authorization, database persistence, and external media storage — using a minimal and explicit Python stack.

Built as an educational reference for developers learning:

- How to structure a FastAPI project
- JWT-based authentication with fastapi-users
- Async database access with SQLAlchemy + aiosqlite
- Image upload and CDN delivery via ImageKit
- CRUD operations over a REST API

---

## Features

- User registration and login (JWT-based)
- Protected routes with token authentication
- Image upload to ImageKit CDN
- Full CRUD operations on image resources
- Async SQLite persistence via aiosqlite
- Auto-generated interactive docs (`/docs`, `/redoc`)

---

## Tech Stack

| Technology | Role |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Web framework — route definitions, dependency injection |
| [fastapi-users](https://fastapi-users.github.io/fastapi-users/) | Authentication — JWT, registration, login, user management |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM — async database models and queries |
| [aiosqlite](https://aiosqlite.omnilib.dev/) | Async SQLite driver |
| [ImageKit](https://imagekit.io/) | Media storage and CDN delivery |
| [Uvicorn](https://www.uvicorn.org/) | ASGI server |
| [uv](https://docs.astral.sh/uv/) | Package and environment manager |

---

## Project Structure

```
wiener-API/
├── src/
│   └── wiapp.py          # FastAPI app instance and route definitions
├── main.py               # Entry point — runs uvicorn
├── pyproject.toml        # Project metadata and dependencies
├── .env.example          # Required environment variables (template)
└── .gitignore
```

---

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) installed

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation

```bash
# Clone the repository
git clone https://github.com/Faridsz0605/wiener-API.git
cd wiener-API

# Create virtual environment and install dependencies
uv sync
```

### Environment Variables

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `IMAGEKIT_PUBLIC_KEY` | Your ImageKit public API key |
| `IMAGEKIT_PRIVATE_KEY` | Your ImageKit private API key |
| `IMAGEKIT_URL_ENDPOINT` | Your ImageKit URL endpoint |
| `SECRET_KEY` | Secret key for JWT token signing |
| `DATABASE_URL` | SQLite database path (e.g. `sqlite+aiosqlite:///./db.sqlite3`) |

### Run

```bash
python main.py
```

The API will be available at `http://localhost:8000`.

Interactive docs: `http://localhost:8000/docs`

---

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for details.

---

## A Note on Coding Agents

> I am a professional whose intent is to contribute to community, enterprise, and open source. Following that idea, coding agents are used for aesthetical, functional, repetitive tasks, or automation. Although the source code is completely written by humans (me).
>
> The main goal is to ship functional yet easy to maintain code for reliable projects in strong, established companies.

---

<details>
<summary>Documentacion en Espanol</summary>

<br/>

> **Proyecto Educativo** — Este repositorio es un proyecto de aprendizaje enfocado en el backend. No esta pensado para uso en produccion. El objetivo es demostrar diseno de APIs, gestion de autenticacion y patrones CRUD usando herramientas modernas de Python.

---

## Acerca del proyecto

**wiener-API** es un backend REST CRUD inspirado en el flujo principal de Instagram: los usuarios pueden registrarse, autenticarse y gestionar imagenes a traves de una API clara. Se enfoca en los fundamentos del backend — autenticacion, autorizacion, persistencia de datos y almacenamiento externo de medios — usando un stack de Python minimalista y explicito.

Construido como referencia educativa para desarrolladores que aprenden:

- Como estructurar un proyecto con FastAPI
- Autenticacion basada en JWT con fastapi-users
- Acceso asincrono a base de datos con SQLAlchemy + aiosqlite
- Carga de imagenes y entrega por CDN via ImageKit
- Operaciones CRUD sobre una API REST

---

## Funcionalidades

- Registro e inicio de sesion de usuarios (basado en JWT)
- Rutas protegidas con autenticacion por token
- Carga de imagenes a ImageKit CDN
- Operaciones CRUD completas sobre recursos de imagenes
- Persistencia asincrona en SQLite via aiosqlite
- Documentacion interactiva autogenerada (`/docs`, `/redoc`)

---

## Stack tecnologico

| Tecnologia | Rol |
|---|---|
| [FastAPI](https://fastapi.tiangolo.com/) | Framework web — definicion de rutas, inyeccion de dependencias |
| [fastapi-users](https://fastapi-users.github.io/fastapi-users/) | Autenticacion — JWT, registro, login, gestion de usuarios |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM — modelos y consultas asincronas a la base de datos |
| [aiosqlite](https://aiosqlite.omnilib.dev/) | Driver asincrono para SQLite |
| [ImageKit](https://imagekit.io/) | Almacenamiento de medios y entrega por CDN |
| [Uvicorn](https://www.uvicorn.org/) | Servidor ASGI |
| [uv](https://docs.astral.sh/uv/) | Gestor de paquetes y entornos virtuales |

---

## Estructura del proyecto

```
wiener-API/
├── src/
│   └── wiapp.py          # Instancia de la app FastAPI y definicion de rutas
├── main.py               # Punto de entrada — ejecuta uvicorn
├── pyproject.toml        # Metadatos y dependencias del proyecto
├── .env.example          # Variables de entorno requeridas (plantilla)
└── .gitignore
```

---

## Primeros pasos

### Requisitos previos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) instalado

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Instalacion

```bash
# Clonar el repositorio
git clone https://github.com/Faridsz0605/wiener-API.git
cd wiener-API

# Crear entorno virtual e instalar dependencias
uv sync
```

### Variables de entorno

Copiar el archivo de ejemplo y completar los valores:

```bash
cp .env.example .env
```

| Variable | Descripcion |
|---|---|
| `IMAGEKIT_PUBLIC_KEY` | Clave publica de ImageKit |
| `IMAGEKIT_PRIVATE_KEY` | Clave privada de ImageKit |
| `IMAGEKIT_URL_ENDPOINT` | URL endpoint de ImageKit |
| `SECRET_KEY` | Clave secreta para firmar tokens JWT |
| `DATABASE_URL` | Ruta a la base de datos SQLite (ej. `sqlite+aiosqlite:///./db.sqlite3`) |

### Ejecutar

```bash
python main.py
```

La API estara disponible en `http://localhost:8000`.

Documentacion interactiva: `http://localhost:8000/docs`

---

## Licencia

Distribuido bajo la licencia MIT. Ver [LICENSE](./LICENSE) para mas detalles.

---

## Nota sobre agentes de codigo

> Soy un profesional cuyo objetivo es contribuir a la comunidad, la empresa y el codigo abierto. Siguiendo esa idea, los agentes de codigo se utilizan para tareas esteticas, funcionales, repetitivas o de automatizacion. Aunque el codigo fuente esta completamente escrito por personas (yo).
>
> El objetivo principal es entregar codigo funcional y facil de mantener para proyectos confiables en empresas solidas y consolidadas.

</details>
