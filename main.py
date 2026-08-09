import ast
import contextlib
import io
import json
import os
from functools import partial

from kivy.animation import Animation
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

from lessons_data import DATA


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class SoundManager:
    _cache = {}

    @classmethod
    def play(cls, name):
        try:
            if name not in cls._cache:
                sound = None
                for ext in ("ogg", "mp3", "wav"):
                    path = os.path.join(BASE_DIR, "sounds", f"{name}.{ext}")
                    if os.path.exists(path):
                        sound = SoundLoader.load(path)
                        break
                cls._cache[name] = sound

            sound = cls._cache.get(name)
            if sound:
                sound.play()
        except Exception:
            pass


class RoundButton(Button):
    bg_color = ListProperty([0.24, 0.52, 1.0, 1.0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.bold = True
        self.color = (1, 1, 1, 1)

        with self.canvas.before:
            self._bg_color_instr = Color(*self.bg_color)
            self._bg_rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(16)]
            )

        self.bind(pos=self._sync_rect, size=self._sync_rect)
        self.bind(bg_color=self._sync_color, state=self._sync_color, disabled=self._sync_color)
        self._sync_color()

    def _sync_rect(self, *args):
        self._bg_rect.pos = self.pos
        self._bg_rect.size = self.size

    def _sync_color(self, *args):
        if self.disabled:
            self._bg_color_instr.rgba = (0.18, 0.20, 0.28, 1.0)
        elif self.state == "down":
            r = self.bg_color[0] * 0.7
            g = self.bg_color[1] * 0.7
            b = self.bg_color[2] * 0.7
            self._bg_color_instr.rgba = (r, g, b, 1.0)
        else:
            self._bg_color_instr.rgba = self.bg_color


class NameScreen(Screen):
    pass


class HomeScreen(Screen):
    pass


class LevelsScreen(Screen):
    pass


class LessonScreen(Screen):
    pass


class QuizScreen(Screen):
    pass


class CodeScreen(Screen):
    pass


class ResultScreen(Screen):
    pass


class ProgressScreen(Screen):
    pass


KV = '''
#:import dp kivy.metrics.dp

<RoundButton>:
    font_size: dp(18)
    halign: 'center'
    valign: 'middle'
    text_size: self.size
    padding: [dp(12), dp(8)]

<NameScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(28)
        spacing: dp(18)

        Label:
            text: 'Python Quest'
            font_size: dp(32)
            bold: True
            size_hint_y: 0.18

        Label:
            text: 'Enter your hero name to start the adventure'
            font_size: dp(17)
            size_hint_y: 0.10
            text_size: self.width, None
            halign: 'center'

        TextInput:
            id: name_input
            size_hint_y: 0.12
            font_size: dp(20)
            multiline: False
            halign: 'left'
            hint_text: 'Hero name'
            background_color: [0.12, 0.14, 0.22, 1.0]
            foreground_color: [1.0, 1.0, 1.0, 1.0]
            cursor_color: [1.0, 1.0, 0.4, 1.0]

        RoundButton:
            text: 'Start Game'
            size_hint_y: 0.14
            on_release: app.save_name()

<HomeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(24)
        spacing: dp(14)

        BoxLayout:
            size_hint_y: 0.16
            spacing: dp(6)

            Label:
                id: home_name
                text: ''
                font_size: dp(16)
                bold: True
                size_hint_x: 0.34
                text_size: self.size
                valign: 'middle'
                halign: 'left'

            Label:
                id: home_xp
                text: ''
                font_size: dp(14)
                size_hint_x: 0.22
                text_size: self.size
                valign: 'middle'
                halign: 'center'

            Label:
                id: home_coins
                text: ''
                font_size: dp(14)
                color: [1, 0.85, 0.3, 1]
                size_hint_x: 0.22
                text_size: self.size
                valign: 'middle'
                halign: 'center'

            Label:
                id: home_hearts
                text: ''
                font_size: dp(14)
                color: [1, 0.4, 0.5, 1]
                size_hint_x: 0.22
                text_size: self.size
                valign: 'middle'
                halign: 'center'

        Label:
            text: 'Game-Based Python Learning'
            font_size: dp(28)
            bold: True
            size_hint_y: 0.16

        Label:
            text: 'Learn, take quizzes, write code and collect coins'
            font_size: dp(16)
            size_hint_y: 0.10
            text_size: self.width, None
            halign: 'center'

        RoundButton:
            text: 'Start Courses'
            size_hint_y: 0.14
            on_release: app.go_levels()

        RoundButton:
            text: 'My Progress'
            size_hint_y: 0.14
            bg_color: [0.18, 0.72, 0.45, 1]
            on_release: app.go_progress()

<LevelsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(12)

        BoxLayout:
            size_hint_y: 0.12
            spacing: dp(8)

            RoundButton:
                text: 'Back'
                size_hint_x: 0.25
                font_size: dp(14)
                on_release: app.go_home()

            Label:
                text: 'Courses & Lessons'
                font_size: dp(24)
                bold: True

        ScrollView:
            GridLayout:
                id: level_grid
                cols: 1
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

<LessonScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(12)

        BoxLayout:
            size_hint_y: 0.12
            spacing: dp(8)

            RoundButton:
                text: 'Back'
                size_hint_x: 0.25
                font_size: dp(14)
                on_release: app.go_levels()

            Label:
                id: lesson_title
                text: 'Lesson'
                font_size: dp(20)
                bold: True

            Label:
                id: xp_label
                text: 'XP 0'
                size_hint_x: 0.25

        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height

                Label:
                    id: lesson_body
                    text: ''
                    font_size: dp(17)
                    size_hint_y: None
                    height: self.texture_size[1]
                    text_size: self.width, None
                    halign: 'left'

        BoxLayout:
            size_hint_y: 0.12
            spacing: dp(8)

            RoundButton:
                text: 'Start Quiz'
                bg_color: [0.95, 0.55, 0.15, 1.0]
                on_release: app.start_quiz()

            RoundButton:
                id: exercise_btn
                text: 'Code Practice'
                bg_color: [0.15, 0.65, 0.75, 1.0]
                on_release: app.open_exercise()

<QuizScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(12)

        Label:
            id: q_num
            text: 'Question 1'
            size_hint_y: 0.08
            font_size: dp(16)

        Label:
            id: q_text
            text: ''
            font_size: dp(20)
            size_hint_y: 0.18
            text_size: self.width, None
            halign: 'left'
            valign: 'middle'

        BoxLayout:
            id: options_box
            orientation: 'vertical'
            spacing: dp(10)
            size_hint_y: 0.50

        Label:
            id: feedback
            text: ''
            size_hint_y: 0.08
            font_size: dp(18)
            bold: True

        RoundButton:
            id: next_btn
            text: 'Next'
            size_hint_y: 0.12
            opacity: 0
            disabled: True
            on_release: app.next_question()

<CodeScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(16)
        spacing: dp(10)

        BoxLayout:
            size_hint_y: 0.12
            spacing: dp(8)

            RoundButton:
                text: 'Back'
                size_hint_x: 0.25
                font_size: dp(14)
                on_release: app.go_lesson_from_code()

            Label:
                id: exercise_title
                text: 'Practice'
                font_size: dp(18)
                bold: True

            Label:
                id: xp_label2
                text: 'XP 0'
                size_hint_x: 0.25

        Label:
            id: task_text
            text: ''
            size_hint_y: 0.12
            font_size: dp(16)
            text_size: self.width, None
            halign: 'left'

        TextInput:
            id: code_input
            size_hint_y: 0.38
            font_size: dp(16)
            background_color: [0.10, 0.12, 0.18, 1.0]
            foreground_color: [0.90, 1.0, 0.90, 1.0]
            cursor_color: [1.0, 1.0, 0.4, 1.0]
            halign: 'left'
            valign: 'top'

        ScrollView:
            size_hint_y: 0.18

            Label:
                id: output_text
                text: ''
                font_size: dp(15)
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                halign: 'left'

        BoxLayout:
            size_hint_y: 0.12
            spacing: dp(8)

            RoundButton:
                text: 'Run'
                bg_color: [0.95, 0.55, 0.15, 1.0]
                on_release: app.run_code(False)

            RoundButton:
                text: 'Check'
                bg_color: [0.18, 0.72, 0.45, 1.0]
                on_release: app.run_code(True)

            RoundButton:
                text: 'Reset'
                bg_color: [0.35, 0.38, 0.48, 1.0]
                on_release: app.reset_code()

<ResultScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(24)
        spacing: dp(18)

        Label:
            id: result_text
            text: ''
            font_size: dp(20)
            text_size: self.width, None
            halign: 'center'

        RoundButton:
            text: 'Continue'
            size_hint_y: 0.14
            on_release: app.go_levels()

<ProgressScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(24)
        spacing: dp(18)

        Label:
            text: 'Your Progress'
            font_size: dp(28)
            bold: True
            size_hint_y: 0.15

        Label:
            id: progress_text
            text: ''
            font_size: dp(18)
            text_size: self.width, None
            halign: 'center'

        RoundButton:
            text: 'Back'
            size_hint_y: 0.14
            on_release: app.go_home()
'''


SAFE_BUILTINS = {
    "print": print,
    "len": len,
    "range": range,
    "int": int,
    "float": float,
    "str": str,
    "bool": bool,
    "list": list,
    "dict": dict,
    "set": set,
    "tuple": tuple,
    "abs": abs,
    "max": max,
    "min": min,
    "sum": sum,
    "sorted": sorted,
    "enumerate": enumerate,
    "zip": zip,
    "type": type,
    "isinstance": isinstance,
    "round": round,
    "pow": pow,
    "divmod": divmod,
    "reversed": reversed,
    "map": map,
    "filter": filter,
    "all": all,
    "any": any,
    "Exception": Exception,
    "ValueError": ValueError,
    "TypeError": TypeError,
    "ZeroDivisionError": ZeroDivisionError,
    "IndexError": IndexError,
    "KeyError": KeyError,
    "StopIteration": StopIteration,
}


FORBIDDEN_CALLS = {
    "eval", "exec", "open", "compile", "__import__", "input",
    "globals", "locals", "vars", "getattr", "setattr", "delattr",
    "breakpoint", "exit", "quit",
}


FORBIDDEN_ATTRS = {"system", "popen", "exec", "eval"}


def analyze_code(code):
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return f"Syntax error: {e}", None

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            return "import is not allowed in exercises.", None

        if isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and bool(node.test.value):
                return "Infinite loop with a constant value is not allowed.", None

        if isinstance(node, ast.Name):
            name = node.id
            if name.startswith("__") and name.endswith("__"):
                return "Access denied.", None
            if name in FORBIDDEN_CALLS:
                return f"Using {name} is not allowed.", None

        if isinstance(node, ast.Attribute):
            attr = node.attr
            if attr.startswith("__") and attr.endswith("__"):
                return "Access denied.", None
            if attr in FORBIDDEN_ATTRS:
                return "Access denied.", None

        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in FORBIDDEN_CALLS:
                return f"Function {node.func.id} is not allowed.", None

    return None, tree


def run_user_code(code):
    code = code.replace("\r\n", "\n")

    error, tree = analyze_code(code)
    if error:
        return error

    safe_globals = {"__builtins__": SAFE_BUILTINS}
    safe_locals = {}
    output = io.StringIO()

    try:
        compiled = compile(tree, "<exercise>", "exec")
        with contextlib.redirect_stdout(output):
            exec(compiled, safe_globals, safe_locals)
        return output.getvalue()
    except Exception as e:
        return output.getvalue() + f"\nError: {type(e).__name__}: {e}"


def normalize_output(text):
    return " ".join(str(text).split())


def load_save(path):
    default = {
        "name": "",
        "xp": 0,
        "coins": 0,
        "hearts": 5,
        "completed": [],
        "completed_exercises": []
    }

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for key in default:
            data.setdefault(key, default[key])
        return data
    except Exception:
        return default


def save_game(path, data):
    try:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Save error:", e)


class PyQuestApp(App):
    def build(self):
        Builder.load_string(KV)

        Window.clearcolor = (0.05, 0.06, 0.10, 1)

        self.save_path = os.path.join(self.user_data_dir, "pyquest_save.json")
        self.save = load_save(self.save_path)

        self.data = DATA
        self.current_level = 0
        self.current_lesson = 0
        self.current_question = 0
        self.correct_count = 0

        sm = ScreenManager(transition=SlideTransition())

        sm.add_widget(NameScreen(name="name"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(LevelsScreen(name="levels"))
        sm.add_widget(LessonScreen(name="lesson"))
        sm.add_widget(QuizScreen(name="quiz"))
        sm.add_widget(CodeScreen(name="code"))
        sm.add_widget(ResultScreen(name="result"))
        sm.add_widget(ProgressScreen(name="progress"))

        self.sm = sm

        if not self.save.get("name", "").strip():
            self.sm.current = "name"
        else:
            self.refresh_home()
            self.sm.current = "home"

        return sm

    def animate_flash(self, widget):
        Animation.cancel_all(widget)
        widget.opacity = 0
        Animation(opacity=1, duration=0.25).start(widget)

    def refresh_home(self):
        home = self.sm.get_screen("home")

        home.ids.home_name.text = self.save.get("name", "Hero")
        home.ids.home_xp.text = f"XP {self.save.get('xp', 0)}"
        home.ids.home_coins.text = f"Coins {self.save.get('coins', 0)}"
        home.ids.home_hearts.text = f"Hearts {self.save.get('hearts', 5)}"

    def save_name(self):
        SoundManager.play("click")

        name = self.sm.get_screen("name").ids.name_input.text.strip()
        if not name:
            name = "Hero"

        self.save["name"] = name
        save_game(self.save_path, self.save)

        self.refresh_home()
        self.sm.current = "home"

    def go_home(self):
        SoundManager.play("click")
        self.refresh_home()
        self.sm.current = "home"

    def go_levels(self):
        SoundManager.play("click")

        grid = self.sm.get_screen("levels").ids.level_grid
        grid.clear_widgets()

        for li, level in enumerate(self.data):
            header = Label(
                text=level["title"],
                font_size=dp(22),
                bold=True,
                size_hint_y=None,
                height=dp(42),
                color=(1, 1, 1, 0.9),
                halign="left"
            )
            header.text_size = (Window.width - dp(70), None)
            grid.add_widget(header)

            for si, lesson in enumerate(level["lessons"]):
                unlocked = self.is_lesson_unlocked(li, si)
                completed = self.is_completed(li, si)

                if completed:
                    prefix = "[Done] "
                elif not unlocked:
                    prefix = "[Locked] "
                else:
                    prefix = ""

                color = list(level.get("color", [0.24, 0.52, 1.0, 1.0]))
                if not unlocked:
                    color = [0.20, 0.22, 0.30, 1.0]

                btn = RoundButton(
                    text=prefix + lesson["title"],
                    size_hint_y=None,
                    height=dp(62),
                    bg_color=color,
                    halign="left"
                )
                btn.text_size = (Window.width - dp(90), None)
                btn.bind(on_release=partial(self.open_lesson, li, si))
                grid.add_widget(btn)

            grid.add_widget(Widget(size_hint_y=None, height=dp(10)))

        self.sm.current = "levels"

    def go_progress(self):
        SoundManager.play("click")

        total = sum(len(level["lessons"]) for level in self.data)
        lessons_done = len(set(self.save.get("completed", [])))
        exercises_done = len(set(self.save.get("completed_exercises", [])))

        text = (
            f"Hero: {self.save.get('name', 'Hero')}\n"
            f"XP: {self.save.get('xp', 0)}\n"
            f"Coins: {self.save.get('coins', 0)}\n"
            f"Hearts: {self.save.get('hearts', 5)}\n"
            f"Lessons completed: {lessons_done} of {total}\n"
            f"Exercises done: {exercises_done} of {total}\n"
        )

        if lessons_done == total:
            text += "Great! You finished all courses."
        else:
            text += "Pass quizzes to unlock new lessons."

        self.sm.get_screen("progress").ids.progress_text.text = text
        self.sm.current = "progress"

    def is_completed(self, level_index, lesson_index):
        key = f"{level_index}-{lesson_index}"
        return key in self.save.get("completed", [])

    def is_lesson_unlocked(self, level_index, lesson_index):
        if level_index == 0 and lesson_index == 0:
            return True

        if lesson_index > 0:
            return self.is_completed(level_index, lesson_index - 1)

        if level_index > 0:
            prev_count = len(self.data[level_index - 1]["lessons"])
            if prev_count == 0:
                return True
            return self.is_completed(level_index - 1, prev_count - 1)

        return True

    def get_current_lesson(self):
        return self.data[self.current_level]["lessons"][self.current_lesson]

    def open_lesson(self, level_index, lesson_index, *args):
        SoundManager.play("click")

        if not self.is_lesson_unlocked(level_index, lesson_index):
            return

        self.current_level = level_index
        self.current_lesson = lesson_index

        lesson = self.get_current_lesson()
        lesson_screen = self.sm.get_screen("lesson")

        lesson_screen.ids.lesson_title.text = lesson["title"]
        lesson_screen.ids.lesson_body.text = lesson["content"]
        lesson_screen.ids.xp_label.text = f"XP {self.save.get('xp', 0)}"
        lesson_screen.ids.exercise_btn.disabled = not bool(lesson.get("exercise"))

        self.sm.current = "lesson"

    def start_quiz(self):
        SoundManager.play("click")

        lesson = self.get_current_lesson()

        if not lesson.get("quiz"):
            self.show_result("This lesson has no quiz yet.")
            return

        self.current_question = 0
        self.correct_count = 0

        self.show_question()
        self.sm.current = "quiz"

    def show_question(self):
        lesson = self.get_current_lesson()
        quiz = lesson.get("quiz", [])

        if self.current_question >= len(quiz):
            self.finish_quiz()
            return

        q = quiz[self.current_question]
        quiz_screen = self.sm.get_screen("quiz")

        quiz_screen.ids.q_num.text = f"Question {self.current_question + 1} of {len(quiz)}"
        quiz_screen.ids.q_text.text = q["q"]
        quiz_screen.ids.feedback.text = ""
        quiz_screen.ids.next_btn.opacity = 0
        quiz_screen.ids.next_btn.disabled = True

        box = quiz_screen.ids.options_box
        box.clear_widgets()

        for i, option in enumerate(q["options"]):
            btn = RoundButton(
                text=option,
                size_hint_y=None,
                height=dp(56),
                bg_color=[0.20, 0.24, 0.36, 1.0],
                halign="left"
            )
            btn.text_size = (Window.width - dp(80), None)
            btn.bind(on_release=partial(self.answer_question, i, btn))
            box.add_widget(btn)

    def answer_question(self, selected_index, selected_button, *args):
        lesson = self.get_current_lesson()
        quiz = lesson.get("quiz", [])

        if self.current_question >= len(quiz):
            return

        q = quiz[self.current_question]
        quiz_screen = self.sm.get_screen("quiz")
        feedback = quiz_screen.ids.feedback
        box = quiz_screen.ids.options_box

        if selected_index == q["answer"]:
            selected_button.bg_color = [0.15, 0.65, 0.35, 1.0]
            self.correct_count += 1

            self.save["coins"] = self.save.get("coins", 0) + 5
            save_game(self.save_path, self.save)

            feedback.text = "Correct! +5 coins"
            feedback.color = (0.2, 0.9, 0.4, 1)
            SoundManager.play("correct")
        else:
            selected_button.bg_color = [0.75, 0.20, 0.25, 1.0]

            old_hearts = self.save.get("hearts", 0)
            new_hearts = max(0, old_hearts - 1)
            self.save["hearts"] = new_hearts
            save_game(self.save_path, self.save)

            lost = old_hearts - new_hearts
            feedback.text = "Wrong."
            if lost:
                feedback.text += f" -{lost} heart"

            feedback.color = (1.0, 0.35, 0.35, 1)
            SoundManager.play("wrong")

        self.animate_flash(feedback)

        children = list(reversed(box.children))

        for i, child in enumerate(children):
            child.disabled = True
            if i == q["answer"]:
                child.bg_color = [0.15, 0.65, 0.35, 1.0]

        quiz_screen.ids.next_btn.opacity = 1
        quiz_screen.ids.next_btn.disabled = False

    def next_question(self):
        SoundManager.play("click")
        self.current_question += 1
        self.show_question()

    def finish_quiz(self):
        lesson = self.get_current_lesson()
        quiz_len = len(lesson.get("quiz", []))

        key = f"{self.current_level}-{self.current_lesson}"

        passed = self.correct_count * 10 >= quiz_len * 6
        xp_gain = self.correct_count * 10
        new_completion = False

        if passed and key not in self.save.get("completed", []):
            self.save["completed"].append(key)
            xp_gain += 30
            self.save["coins"] = self.save.get("coins", 0) + 20
            self.save["hearts"] = min(5, self.save.get("hearts", 5) + 1)
            new_completion = True

        self.save["xp"] = self.save.get("xp", 0) + xp_gain
        save_game(self.save_path, self.save)

        message = f"Correct answers: {self.correct_count} of {quiz_len}\n"

        if passed:
            SoundManager.play("correct")
            message += "Great! "
            if new_completion:
                message += "Lesson completed and you got 20 coins."
            else:
                message += "This lesson was already completed."
        else:
            SoundManager.play("wrong")
            message += "Not passed yet. Try again."

        self.show_result(message)

    def show_result(self, text):
        self.sm.get_screen("result").ids.result_text.text = text
        self.sm.current = "result"

    def open_exercise(self):
        SoundManager.play("click")

        lesson = self.get_current_lesson()
        exercise = lesson.get("exercise")

        if not exercise:
            self.show_result("This lesson has no code practice.")
            return

        code_screen = self.sm.get_screen("code")

        code_screen.ids.exercise_title.text = "Practice: " + lesson["title"]
        code_screen.ids.task_text.text = exercise.get("task", "")
        code_screen.ids.code_input.text = exercise.get("code", "")
        code_screen.ids.output_text.text = ""
        code_screen.ids.xp_label2.text = f"XP {self.save.get('xp', 0)}"

        self.sm.current = "code"

    def go_lesson_from_code(self):
        SoundManager.play("click")
        self.sm.current = "lesson"

    def reset_code(self):
        SoundManager.play("click")

        lesson = self.get_current_lesson()
        exercise = lesson.get("exercise", {})
        code_screen = self.sm.get_screen("code")

        code_screen.ids.code_input.text = exercise.get("code", "")
        code_screen.ids.output_text.text = ""

    def run_code(self, check=False):
        SoundManager.play("click")

        code_screen = self.sm.get_screen("code")
        code = code_screen.ids.code_input.text

        result = run_user_code(code)
        display = result if result.strip() else "(no output)"

        if check:
            lesson = self.get_current_lesson()
            exercise = lesson.get("exercise", {})
            expected = exercise.get("expected", "")

            if normalize_output(result) == normalize_output(expected):
                display += "\n\nGreat! Output is correct."
                self.award_exercise()
                SoundManager.play("correct")
            else:
                display += f"\n\nExpected output:\n{expected}"
                SoundManager.play("wrong")

        self.animate_flash(code_screen.ids.output_text)
        code_screen.ids.output_text.text = display

    def award_exercise(self):
        key = f"{self.current_level}-{self.current_lesson}"

        if key not in self.save.get("completed_exercises", []):
            self.save["completed_exercises"].append(key)
            self.save["coins"] = self.save.get("coins", 0) + 20
            save_game(self.save_path, self.save)

        code_screen = self.sm.get_screen("code")
        code_screen.ids.xp_label2.text = f"XP {self.save.get('xp', 0)}"


if __name__ == "__main__":
    PyQuestApp().run()
