"""A Ninja Myca in Jac and Flet"""

import:py flet as ft;

can plan(page: ft.Page) {
    can add_clicked(e: ft.Event);

    new_task = ft.TextField(hint_text="Whats needs to be done?");
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked));
    
    :ability:add_clicked(e: ft.Event) {
        page.add(ft.Checkbox(label=new_task.value));
        new_task.value = "";
        page.update();
    }
}

with entry { ft.app(target=plan); }