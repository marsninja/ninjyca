import:py flet;
import:py from flet,
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Row,
    Tab,
    Tabs,
    Text,
    TextField,
    UserControl,
    colors,
    icons;


object Task:UserControl {
    has completed:bool=False, task_name:str, task_status_change: callable, task_delete: callable;

    can build -> Column{
        <self>.display_task = Checkbox(
            value=False, label=<self>.task_name, on_change=<self>.status_changed
        );
        <self>.edit_name = TextField(expand=1);

        <self>.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                <self>.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=<self>.edit_clicked
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=<self>.delete_clicked
                        )
                    ]
                )
            ]
        );

        <self>.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                <self>.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=<self>.save_clicked
                )
            ]
        );
        return Column(controls=[<self>.display_view, <self>.edit_view]);
    }

    can edit_clicked(e: Event) {
        <self>.edit_name.value = <self>.display_task.label;
        <self>.display_view.visible = False;
        <self>.edit_view.visible = True;
        <self>.update();
    }

    can save_clicked(e: Event) {
        <self>.display_task.label = <self>.edit_name.value;
        <self>.display_view.visible = True;
        <self>.edit_view.visible = False;
        <self>.update();
    }

    can status_changed(e: Event) {
        <self>.completed = <self>.display_task.value;
        <self>.task_status_change(self);
    }

    can delete_clicked(e: Event) {
        <self>.task_delete(self);
    }
}


object TodoApp:UserControl {
    can build {
        <self>.new_task = TextField(
            hint_text="What needs to be done?", on_submit=<self>.add_clicked, expand=True
        );
        <self>.tasks = Column();

        <self>.filter = Tabs(
            selected_index=0,
            on_change=<self>.tabs_changed,
            tabs=[Tab(text="all"), Tab(text="active"), Tab(text="completed")]
        );

        <self>.items_left = Text("0 items left");

        # application's root control (i.e. "view") containing all other controls
        return Column(
            width=600,
            controls=[
                Row([Text(value="Todos", style="headlineMedium")], alignment="center"),
                Row(
                    controls=[
                        <self>.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=<self>.add_clicked)
                    ]
                ),
                Column(
                    spacing=25,
                    controls=[
                        <self>.filter,
                        <self>.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                <self>.items_left,
                                OutlinedButton(
                                    text="Clear completed", on_click=<self>.clear_clicked
                                )
                            ]
                        )
                    ]
                )
            ]
        );
    }
    can add_clicked(e: event){
        if <self>.new_task.value{
            task = Task(<self>.new_task.value, <self>.task_status_change, <self>.task_delete);
            <self>.tasks.controls.append(task);
            <self>.new_task.value = "";
            <self>.new_task.focus();
            <self>.update();
        }
    }

    can task_status_change(task: Task){ <self>.update(); }

    can task_delete(task: Task) {
        <self>.tasks.controls.remove(task);
        <self>.update();
    }

    can tabs_changed(e: event){
        <self>.update();
    }

    can clear_clicked(e: event){
        for task in <self>.tasks.controls[:] {
            if task.completed {<self>.task_delete(task);}
        }
    }

    can update {
        status = <self>.filter.tabs[<self>.filter.selected_index].text;
        count = 0;
        for task in <self>.tasks.controls {
            task.visible = 
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed);
            if not task.completed {count += 1;}
        }
        <self>.items_left.value = f"{count} active item(s) left";
        super().update();
    }
}

can main(page: Page) {
    page.title = "ToDo App";
    page.horizontal_alignment = "center";
    page.scroll = "adaptive";
    page.update();

    # create application instance
    app = TodoApp();

    # add application's root control to the page
    page.add(app);
}

with entry {flet.app(target=main);}
