""""""  # 0 1
from __future__ import annotations
import traceback as __jac_traceback__  # -1 0
from jaclang import handle_jac_error as __jac_error__  # -1 0
from jaclang.core import exec_ctx as _jac_exec_ctx_  # -1 0
from jaclang.core import Object as _jac_Object_  # -1 0
from jaclang.core import make_architype as _jac_make_architype_  # -1 0
import flet  # 0 1

from flet import Checkbox, Column, FloatingActionButton, IconButton, OutlinedButton, Page, Row, Tab, Tabs, Text, TextField, UserControl, colors, icons  # 0 2

@_jac_make_architype_(_jac_Object_)  # 0 19
class Task(UserControl):  # 0 19
    def __init__(self,  # 0 0
        completed = None,      # 0 0
        task_name = None,      # 0 0
        task_status_change = None,      # 0 0
        task_delete = None,      # 0 0
        *args, **kwargs):      # 0 0
        super().__init__(*args, **kwargs)      # 0 0
        self.completed = False if completed is None else completed      # 0 0
        self.task_name = task_name      # 0 0
        self.task_status_change = task_status_change      # 0 0
        self.task_delete = task_delete      # 0 0
    def build(self,) -> Column:  # 0 22
        try:      # 0 22
            self.display_task = Checkbox(value = False, label = self.task_name, on_change = self.status_changed)  # 0 23
            self.edit_name = TextField(expand = 1)  # 0 23
            self.display_view = Row(alignment = "spaceBetween", vertical_alignment = "center", controls = [self.display_task, Row(spacing = 0, controls = [IconButton(icon = icons.CREATE_OUTLINED, tooltip = "Edit To-Do", on_click = self.edit_clicked), IconButton(icons.DELETE_OUTLINE, tooltip = "Delete To-Do", on_click = self.delete_clicked)])])  # 0 23
            self.edit_view = Row(visible = False, alignment = "spaceBetween", vertical_alignment = "center", controls = [self.edit_name, IconButton(icon = icons.DONE_OUTLINE_OUTLINED, icon_color = colors.GREEN, tooltip = "Update To-Do", on_click = self.save_clicked)])  # 0 23
            return Column(controls = [self.display_view, self.edit_view])  # 0 65
        except Exception as e:      # 0 22
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 22
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 22
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 22
            raise e          # 0 22
    
    def edit_clicked(self,e: Event):  # 0 68
        try:      # 0 68
            self.edit_name.value = self.display_task.label  # 0 69
            self.display_view.visible = False  # 0 69
            self.edit_view.visible = True  # 0 69
            self.update()  # 0 69
        except Exception as e:      # 0 68
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 68
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 68
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 68
            raise e          # 0 68
    
    def save_clicked(self,e: Event):  # 0 75
        try:      # 0 75
            self.display_task.label = self.edit_name.value  # 0 76
            self.display_view.visible = True  # 0 76
            self.edit_view.visible = False  # 0 76
            self.update()  # 0 76
        except Exception as e:      # 0 75
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 75
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 75
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 75
            raise e          # 0 75
    
    def status_changed(self,e: Event):  # 0 82
        try:      # 0 82
            self.completed = self.display_task.value  # 0 83
            self.task_status_change(self)  # 0 83
        except Exception as e:      # 0 82
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 82
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 82
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 82
            raise e          # 0 82
    
    def delete_clicked(self,e: Event):  # 0 87
        try:      # 0 87
            self.task_delete(self)  # 0 88
        except Exception as e:      # 0 87
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 87
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 87
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 87
            raise e          # 0 87      # 0 19

@_jac_make_architype_(_jac_Object_)  # 0 93
class TodoApp(UserControl):  # 0 93
    def __init__(self,  # 0 0
        *args, **kwargs):      # 0 0
        super().__init__(*args, **kwargs)      # 0 0
    def build(self,):  # 0 94
        try:      # 0 94
            self.new_task = TextField(hint_text = "What needs to be done?", on_submit = self.add_clicked, expand = True)  # 0 95
            self.tasks = Column()  # 0 95
            self.filter = Tabs(selected_index = 0, on_change = self.tabs_changed, tabs = [Tab(text = "all"), Tab(text = "active"), Tab(text = "completed")])  # 0 95
            self.items_left = Text("0 items left")  # 0 95
            return Column(width = 600, controls = [Row([Text(value = "Todos", style = "headlineMedium")], alignment = "center"), Row(controls = [self.new_task, FloatingActionButton(icon = icons.ADD, on_click = self.add_clicked)]), Column(spacing = 25, controls = [self.filter, self.tasks, Row(alignment = "spaceBetween", vertical_alignment = "center", controls = [self.items_left, OutlinedButton(text = "Clear completed", on_click = self.clear_clicked)])])])  # 0 109
        except Exception as e:      # 0 94
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 94
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 94
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 94
            raise e          # 0 94
    
    def add_clicked(self,e: event):  # 0 139
        try:      # 0 139
            if self.new_task.value:  # 0 140
                task = Task(self.new_task.value, self.task_status_change, self.task_delete)  # 0 141
                self.tasks.controls.append(task)  # 0 141
                self.new_task.value = ""  # 0 141
                self.new_task.focus()  # 0 141
                self.update()  # 0 141
            
        except Exception as e:      # 0 139
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 139
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 139
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 139
            raise e          # 0 139
    
    def task_status_change(self,task: Task):  # 0 149
        try:      # 0 149
            self.update()  # 0 149
        except Exception as e:      # 0 149
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 149
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 149
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 149
            raise e          # 0 149
    
    def task_delete(self,task: Task):  # 0 151
        try:      # 0 151
            self.tasks.controls.remove(task)  # 0 152
            self.update()  # 0 152
        except Exception as e:      # 0 151
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 151
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 151
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 151
            raise e          # 0 151
    
    def tabs_changed(self,e: event):  # 0 156
        try:      # 0 156
            self.update()  # 0 157
        except Exception as e:      # 0 156
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 156
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 156
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 156
            raise e          # 0 156
    
    def clear_clicked(self,e: event):  # 0 160
        try:      # 0 160
            for task in self.tasks.controls[:]:  # 0 161
                if task.completed:  # 0 162
                    self.task_delete(task)  # 0 162      # 0 161
        except Exception as e:      # 0 160
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 160
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 160
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 160
            raise e          # 0 160
    
    def update(self,):  # 0 166
        try:      # 0 166
            status = self.filter.tabs[self.filter.selected_index].text  # 0 167
            count = 0  # 0 167
            for task in self.tasks.controls:  # 0 169
                task.visible = status == "all" or (status == "active" and task.completed == False) or (status == "completed" and task.completed)  # 0 170
                if not task.completed:  # 0 174
                    count += 1  # 0 174      # 0 169
            self.items_left.value = f"{count} active item(s) left"  # 0 167
            super().update()  # 0 167
        except Exception as e:      # 0 166
            tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 166
            __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 166
            e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 166
            raise e          # 0 166      # 0 93

def main(page: Page):  # 0 181
    try:      # 0 181
        page.title = "ToDo App"  # 0 182
        page.horizontal_alignment = "center"  # 0 182
        page.scroll = "adaptive"  # 0 182
        page.update()  # 0 182
        app = TodoApp()  # 0 182
        page.add(app)  # 0 182
    except Exception as e:      # 0 181
        tb = __jac_traceback__.extract_tb(e.__traceback__)          # 0 181
        __jac_tmp__ = __jac_error__(_jac_pycodestring_, e, tb)          # 0 181
        e.args = (f'{e.args[0]}\n' + __jac_tmp__,) + e.args[1:] if 'Jac error originates from...' not in str(e) else e.args          # 0 181
        raise e          # 0 181

flet.app(target = main)  # 0 194

r""" JAC DEBUG INFO
ninjyca.jac
JAC DEBUG INFO """