from ..domain.todo import Todo, TodoId, TodoTitle, TodoDescription, TodoStatus
from ..others.factory.todo import TodoFactory
from ..others.repository.todo import TodoRepository
from ..others.query_service.todo import TodoQueryService

class TodoApplication:
    def __init__(self, fact: TodoFactory ,repo: TodoRepository, qs: TodoQueryService):
        self.repo = repo()
        self.qs = qs()
        self.fact = fact(self.repo)

    def create_todo(self, init_input: dict[str, str]) -> None:
        """todo を作成する"""
        new_id: TodoId = self.qs.get_new_id()
        todo_input = {
            'todo_id': new_id,
            **init_input,
            'completed': TodoStatus(False)
            }
        new_todo: Todo = self.fact.create(todo_input)
        self.repo.save(new_todo)

    def read_todo(self, id_num: int) -> Todo | None:
        """todo を取得する"""
        id_to_read: TodoId = TodoId(id_num)
        if self.qs.is_exist_id(id_to_read):
            return self.qs.get_by_id(id_to_read)
        else:
            return None

    def update_todo(self, edit_input: dict[str, str]) -> None:
        """todo を更新する"""
        id = TodoId(edit_input['todo_id'])
        todo = self.qs.get_by_id(id)
        if todo is not None:
            title = TodoTitle(edit_input['title'])
            description = TodoDescription(edit_input['description'])
            status = TodoStatus(edit_input['completed'])
            self.repo.modify(todo, title, description, status)

    def delete_todo(self, id_num: int) -> None:
        """todo を削除する"""
        id_to_delete: TodoId = TodoId(id_num)
        if self.qs.is_exist_id(id_to_delete):
            self.repo.remove(id_to_delete)

    def index_todo(self) -> list[Todo]:
        """todo の一覧を取得する"""
        return self.qs.get_all()

        # init_input
        #     'title': str
        #     'description': str

        # edit_input
        #     'todo_id': int
        #     'title': str
        #     'description': str
        #     'completed': bool

if __name__ == '__main__':
    app = TodoApplication(TodoFactory, TodoRepository, TodoQueryService)
    init_input1 = {
        'title': "タイトル1", 
        'description': "詳細1"
        }
    app.create_todo(init_input1)
    