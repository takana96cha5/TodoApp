class TodoId:
    """todo の id の型を表す"""
    def __init__(self, value: int):
        self.value = value

class TodoTitle:
    """todo のタイトルの型を表す"""
    def __init__(self, value: str):
        self.value = value

class TodoDescription:
    """todo の説明の型を表す"""
    def __init__(self, value: str):
        self.value = value

class TodoStatus:
    """todo のステータス（完了かどうか）の型を表す"""
    def __init__(self, value: bool):
        self.value = value

class Todo:
    """todo の一つのタスクを表す"""
    def __init__(self, todo_id: TodoId, title: TodoTitle, description: TodoDescription, completed: TodoStatus):
        self.todo_id = todo_id
        self.title = title
        self.description = description
        self.completed = completed
    
    def get_id_num(self) -> int:
        """todo のID番号を取得"""
        return self.todo_id.value
    
    def edit_title(self, new_title):
        """todo のタイトルを編集"""
        self.title = TodoTitle(new_title)
    
    def edit_description(self, new_description):
        """todo の詳細を編集"""
        self.description = TodoDescription(new_description)

    def done(self):
        """todo のタスクを完了状態に変更"""
        self.completed: TodoStatus = True

    def not_yet(self):
        """todo のタスクを未完了状態に変更"""
        self.completed: TodoStatus = False