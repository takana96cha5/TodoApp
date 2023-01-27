from ....domain.todo import Todo, TodoId
from ...Infra.query_service.todo import TodoRepository

class TodoQueryService:
    """todo の参照系の処理を抽象化する"""
    def __init__(self):
        self.repo = TodoRepository()

    def get_all(self) -> list[Todo]:
        """全ての Todo の一覧を取得する"""
        return self.repo.todo_list

    def get_by_id(self, todo_id: TodoId) -> Todo:
        """id から todo を取得する"""
        for todo in self.repo.todo_list:
            if todo.todo_id.value == todo_id.value:
                return todo
        return None

    def get_new_id(self) -> TodoId:
        """新規作成用の todo_id を取得する"""
        new_id_num =  self.repo.todo_list[-1].get_id_num() + 1
        return TodoId(new_id_num)

    def is_exist_id(self) -> bool:
        """idが存在しているかを確認する"""
