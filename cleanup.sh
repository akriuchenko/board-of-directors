#!/bin/bash

# Clean up old dependencies and install new ones
echo "🧹 Очищаю старі залежності..."

pip uninstall crewai crewai-tools openai pydantic requests -y

echo "✨ Встановлюю нові версії..."

pip install -r requirements.txt

echo "✅ Готово! Все оновлено на новіші версії"
