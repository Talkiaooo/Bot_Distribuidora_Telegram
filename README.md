Un archivo README.md es fundamental: es la primera impresión que tendrá tu profesora al entrar a tu repositorio. Debe ser profesional, claro y explicar cómo ejecutar el proyecto.

Aquí tienes una estructura lista para copiar y pegar en tu archivo README.md:

🤖 Asistente Conversacional Inteligente (Bot de Telegram)
Este proyecto consiste en el desarrollo de un bot de Telegram diseñado para la atención automatizada en comercios minoristas. El bot utiliza técnicas de Procesamiento de Lenguaje Natural (PLN) para clasificar intenciones de usuario y gestionar una base de conocimientos local.

🚀 Características principales
Gestión de Memoria: Implementación de un gestor de estados para recordar datos del usuario (Nombre, Empresa, Localidad) durante la sesión.

Clasificación de Intenciones: Uso de la librería spaCy con modelos preentrenados (es_core_news_sm) para entender qué desea el usuario (consultar catálogo, promos, o ayuda).

Didáctica y UX: Interfaz amigable que guía al usuario mediante botones interactivos (Inline Keyboards) y mensajes contextuales.

Búsqueda Inteligente: Capacidad de entender variaciones semánticas gracias al análisis de similitud vectorial.

🛠️ Stack Tecnológico
Lenguaje: Python 3.x

API: pyTelegramBotAPI (telebot)

PLN: spaCy (Modelo es_core_news_sm)

Almacenamiento: Formato JSON para la gestión de productos y promociones.

📋 Requisitos previos
Tener instalado Python 3.10+.

Instalar las dependencias:

pip install pyTelegramBotAPI spacy
python -m spacy download es_core_news_sm

⚙️ Configuración
Clona este repositorio.

Asegúrate de tener el archivo productos.json en la carpeta raíz.

Edita el archivo bot.py e ingresa tu token de Telegram en la variable TOKEN.

Ejecuta el bot:

python bot.py
