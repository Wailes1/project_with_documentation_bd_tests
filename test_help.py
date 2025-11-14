# 3. Проверить корректность докстрингов с помощью help(). Убедиться, что документация отображается корректно
from notebook.models import Note
from notebook.commands import NoteCommands
from notebook.storage import NoteStorage

def test_documentation():
    """Тестирует отображение документации."""
    
    print("ДОКУМЕНТАЦИЯ КЛАССА Note")
    print("=" * 60)
    help(Note)
    
    print("ДОКУМЕНТАЦИЯ КЛАССА NoteStorage")
    print("=" * 60)
    help(NoteStorage)
    
    print("ДОКУМЕНТАЦИЯ КЛАССА NoteCommands")
    print("=" * 60)
    help(NoteCommands)
    
    print("ДОКУМЕНТАЦИЯ МЕТОДОВ NoteCommands")
    print("=" * 60)
    commands = NoteCommands(NoteStorage())
    help(commands.add_note)
    help(commands.list_notes)

if __name__ == "__main__":
    test_documentation()