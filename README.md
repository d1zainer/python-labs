# python-labs

Лабораторные работы по Python.

## Структура проекта

```
python-labs/
├── homework/       # Практические задания
│   ├── 1/
│   └── 2/
└── case/           # Кейсы
    ├── 1/
    └── 2/
```

## Настройка окружения

### 1. Активация виртуального окружения

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Запуск Jupyter

```bash
jupyter lab
```