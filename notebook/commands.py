"""
Модуль, содержащий логику команд.

Содержит класс NoteCommands, который инкапсулирует все действия
над заметками: добавление, вывод списка, поиск и удаление.
"""

from datetime import datetime
from .models import Note
from .storage import NoteStorage

class NoteCommands:
    """Класс для обработки команд пользователя.
    
    Attributes:
        storage (NoteStorage): Объект для работы с хранилищем заметок.
    """
    
    def __init__(self, storage: NoteStorage):
        """Инициализирует обработчик команд.
        
        Args:
            storage (NoteStorage): Объект для работы с хранилищем.
        """
        self.storage = storage
    
    def add_note(self, title: str, content: str):
        """Добавляет новую заметку.
        
        Args:
            title (str): Заголовок заметки.
            content (str): Текст заметки.
            
        Raises:
            ValueError: Если заголовок или содержание пустые.
        """
        if not title or not content:
            raise ValueError("Заголовок и содержание обязательны!")
        
        note = Note(title=title, content=content)
        saved_note = self.storage.save_note(note)
        print(f"✅ Заметка добавлена успешно! (ID: {saved_note.id})")
    
    def list_notes(self, date_filter: str = None):
        """Показывает все заметки с возможностью фильтрации по дате.
        
        Args:
            date_filter (str, optional): Фильтр по дате. По умолчанию None.
        """
        notes = self.storage.get_all_notes()
        
        if date_filter:
            notes = self.storage.filter_notes_by_date(notes, date_filter)
        
        if not notes:
            if date_filter:
                print(f"📝 Заметок за {date_filter} не найдено.")
            else:
                print("📝 Заметок пока нет. Создайте первую!")
            return
        
        if date_filter:
            print(f"📋 Я нашёл {len(notes)} заметок за {date_filter}:")
        else:
            print(f"📋 Я нашёл {len(notes)} заметок:")
            
        for note in notes:
            print(f"ID: {note.id}")
            print(f"Заголовок: {note.title}")
            print(f"Содержание: {note.content}")
            print(f"Создана: {note.created_at[:16]}")
            print("-" * 30)
    
    def search_notes(self, query: str, date_filter: str = None):
        """Ищет заметки по тексту в заголовке или содержании.
        
        Args:
            query (str): Текст для поиска.
            date_filter (str, optional): Фильтр по дате. По умолчанию None.
        """
        if not query:
            print("Введите текст для поиска!")
            return
        
        notes = self.storage.search_notes(query)
        
        if date_filter:
            notes = self.storage.filter_notes_by_date(notes, date_filter)
        
        if not notes:
            if date_filter:
                print(f"По запросу '{query}' за {date_filter} я ничего не нашёл (")
            else:
                print(f"По запросу '{query}' я ничего не нашёл (")
            return
        
        if date_filter:
            print(f"Я нашёл {len(notes)} заметок по запросу '{query}' за {date_filter}:")
        else:
            print(f"Я нашёл {len(notes)} заметок по запросу '{query}':")
            
        for note in notes:
            print(f"ID: {note.id} - {note.title}")
            print(f"   {note.content[:60]}...")
    
    def delete_note(self, note_id: int):
        """Удаляет заметку по ID.
        
        Args:
            note_id (int): ID заметки для удаления.
        """
        if self.storage.delete_note(note_id):
            print(f"Заметка ID {note_id} удалена")
        else:
            print(f"Заметка с ID {note_id} не найдена")