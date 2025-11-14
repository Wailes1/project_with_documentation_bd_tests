"""
Модуль, содержащий модели данных.

Содержит класс Note, который представляет структуру одной заметки
и методы для её преобразования в словарь и обратно.
"""

import json
from datetime import datetime

class Note:
    """Класс для представления одной заметки.
    
    Attributes:
        id (int, optional): Уникальный идентификатор заметки.
        title (str): Заголовок заметки.
        content (str): Основной текст заметки.
        created_at (str): Дата и время создания в формаite ISO.
    """
    
    def __init__(self, title: str, content: str):
        """Инициализирует новую заметку.
        
        Args:
            title (str): Заголовок новой заметки.
            content (str): Текст новой заметки.
        """
        self.id = None
        self.title = title
        self.content = content
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Преобразует объект заметки в словарь.
        
        Returns:
            dict: Словарь с данными заметки, готовый для сериализации в JSON.
        """
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """Создает объект заметки из словаря.
        
        Args:
            data (dict): Словарь с данными заметки.
            
        Returns:
            Note: Объект заметки, восстановленный из словаря.
        """
        note = cls(data['title'], data['content'])
        note.id = data['id']
        note.created_at = data['created_at']
        return note