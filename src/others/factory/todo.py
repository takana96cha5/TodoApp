from ...domain.todo import TodoId, TodoTitle, TodoDescription, TodoStatus, Todo
from ...others.Infra.repository.todo import TodoRepository

class TodoFactory:
    """todo の生成系の処理を抽象化する"""
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create(self, todo_input: dict[TodoId, str, str, TodoStatus]) -> Todo:
        """ユーザーの入力から todo クラスのインスタンスを作成する"""
        id: TodoId                   = todo_input['todo_id']
        title: TodoTitle             = TodoTitle(todo_input['title'])
        description: TodoDescription = TodoDescription(todo_input['description'])
        completed: TodoStatus        = todo_input['completed']

        return Todo(id, title, description, completed)
