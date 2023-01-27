from ....domain.todo import Todo, TodoId, TodoTitle, TodoDescription, TodoStatus

class TodoRepository:
    """todo 更新系の処理を抽象化する"""
    def __init__(self):
        self.todo_list: list[Todo] = []

    def save(self, todo: Todo) -> None:
        """Todo を保存する"""
        self.todo_list.append(todo)

    def modify(self, todo: Todo, title: TodoTitle, description: TodoDescription, status: TodoStatus) -> None:
        """Todo を更新する"""
        todo.title = title
        todo.description = description
        todo.completed = status

    def remove(self, todo_id: TodoId) -> None:
        """Todo を削除する"""
        self.todo_list = [todo for todo in self.todo_list if todo.todo_id.value != todo_id.value]
