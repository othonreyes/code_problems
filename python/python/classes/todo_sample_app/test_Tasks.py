import string

import pytest

from python.python.classes.todo_sample_app.Meta import Project, TasksDao, Storage, Task, InMemoryStorage


@pytest.fixture
def supply_project() -> Project:
    return Project('Dragon Ball Z')

def test_add_task(supply_project):
    project = supply_project
    assert project
    assert project.name
    assert project.name == 'Dragon Ball Z'

# def test_dao(mocker):
#     """
#     Doens't work as the mocker.patch for find and insert are not doing anything
#     """
#     mocker.patch('python.python.classes.todo_sample_app.Meta.Storage.find', None) useless
#     mocker.patch('python.python.classes.todo_sample_app.Meta.Storage.insert')     useless
#     storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
#     spy = mocker.spy(storage, 'insert')
#
#     dao = TasksDao(storage)
#     assert dao
#     task = Task('Train with Piccollo', 1)
#     dao.saveTask(task)
#
#     spy.assert_called_once_with(task)

def test_dao2(mocker):
    """
    Doens't work
    """
    storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
    storage.find.return_value = None # The problem was that the logic in the task was wrong
    spy = mocker.spy(storage, 'insert')

    dao = TasksDao(storage)
    assert dao
    task = Task('Train with Piccollo', 1)
    dao.saveTask(task)

    spy.assert_called_once_with(task)

def test_dao_find_returns_None_update_never_called(mocker):
    """
    This works!
    """
    storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
    mocker.patch.object(storage, 'find')
    storage.find.return_value = None

    spy_insert = mocker.spy(storage, 'insert')
    spy_update = mocker.spy(storage, 'update')

    dao = TasksDao(storage)
    assert dao
    task = Task('Train with Piccollo', 1)
    dao.saveTask(task)

    spy_insert.assert_called_once_with(task)
    spy_update.assert_not_called()

def test_dao(mocker):
    storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
    # ~doesn't work~/ Works! The problem was on the logic of the Task test
    find_method = mocker.patch.object(storage, 'find')
    find_method.return_value = None

    spy = mocker.spy(storage, 'insert')

    dao = TasksDao(storage)
    assert dao

    task = Task('Train with Piccollo', 1)
    dao.saveTask(task)

    spy.assert_called_once_with(task)



def test_in_memory(supply_project):
    in_memory_storage = InMemoryStorage()
    dao = TasksDao(in_memory_storage)
    # task = Task("Train with the kaiosama", 2)
    task = Task('Train with Piccollo', 1)
    result = dao.saveTask(task)
    assert result



# Tests scenarios:
# - When task doesn't exist THEN should be inserted
# - When task exist THEN should be updated
# - When storage doesn't fail, should send notification and metric should be recorded with a success
# - When storage fail, should not send notification and throw exception and metric should be recorded with a success


def test_failures_Exception(mocker):
    storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
    mocker.patch.object(storage, 'find')
    storage.find.side_effect = Exception('Boom!') # = ZeroDivisionError('buu')

    task = Task("Train with the kaiosama", 2)

    with pytest.raises(Exception) as e:
        dao = TasksDao(storage)
        assert dao.saveTask(task)
    assert str(e.value) == 'Boom!'
    print(f"\n{str(e.value)}")

def test_failures_Exception_simplified(mocker):
    storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
    storage.find.side_effect = Exception('Boom!') # = ZeroDivisionError('buu')

    task = Task("Train with the kaiosama", 2)

    # with pytest.raises(ZeroDivisionError) as e:
    with pytest.raises(Exception) as e:
        dao = TasksDao(storage)
        assert dao.saveTask(task)
    assert str(e.value) == 'Boom!'
    print(f"\n{str(e.value)}")

def test_failures_Exception_simplified(mocker):
    """
    Additionally check for the exception message
    """
    storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
    storage.find.side_effect = ArithmeticError('Boom!') # = ArithmeticError('buu')

    task = Task("Train with the kaiosama", 2)

    with pytest.raises(ArithmeticError) as e:
        dao = TasksDao(storage)
        assert dao.saveTask(task)
    assert str(e.value) == 'Boom!'
    print(f"\n{str(e.value)}")


# def test_failures(mocker):
#     # method that we want to fake
#     in_memory_storage = InMemoryStorage()
#     mocker.patch.object(in_memory_storage, 'insert', ZeroDivisionError('buu'))
#     # mocker.patch('python.python.classes.todo_sample_app.Meta.Storage.insert', side_effect= ZeroDivisionError('buu'))
#     # storage = mocker.patch('python.python.classes.todo_sample_app.Meta.Storage')
#     # spy = mocker.spy(storage, 'insert')
#
#     dao = TasksDao(in_memory_storage)
#     task = Task("Train with the kaiosama", 2)
#     with pytest.raises(ZeroDivisionError) as e:
#         assert dao.saveTask(task)
#     # spy.assert_called_once_with(task)
#     # assert str(e.value) == 'buu'