# Variables
APP=app.py
TESTS=test_app.py

# Tarea por defecto
.PHONY: all
all: run

# Instalar dependencias globalmente
.PHONY: install
install:
	pip install -r requirements.txt

# Ejecutar la aplicación
.PHONY: run
run:
	python $(APP)

# Ejecutar pruebas con pytest
.PHONY: test
test:
	pytest $(TESTS)

# Formatear el código con black
.PHONY: format
format:
	black .

# Lint del código con flake8
.PHONY: lint
lint:
	flake8 .

# Limpiar archivos generados
.PHONY: clean
clean:
	rm -rf __pycache__ .pytest_cache
