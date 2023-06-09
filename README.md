# What is PUI
PUI is a declarative UI framework with two-way data binding

# Installation
```
pip install QPUIQ
```

# Get Started
## Hello World
```python
# example/hello_world.py

from PUI.PySide6 import *

class Example(Application):
    def content(self):
        with Window(title="test", size=(320,240)):
            Label("Hello world")

root = Example()
root.run()
```
![Hello World](https://github.com/buganini/PUI/raw/main/screenshots/hello_world.png)

## State & Data Binding
```python
# example/pyside6_textfield.py

from PUI.PySide6 import *

data = State()
data.var = 0

class QtExample(QtApplication):
    def content(self):
        with QtWindow(title="blah"):
            with QtVBox():
                with QtHBox():
                    QtButton("-", self.on_minus)
                    QtLabel(f"{data.var}")
                    QtButton("+", self.on_plus)

                QtLineEdit(data("var")) # binding

    def on_minus(self):
        data.var -= 1

    def on_plus(self):
        data.var += 1

root = QtExample()
root.run()
```
![State & Data Binding](https://github.com/buganini/PUI/raw/main/screenshots/pyside6_textfield.png)

## View Component
```python
# example/bleak_list.py

....

@PUI # View Component
def DeviceView(device, advertising_data):
    Label(f"{device.address} {device.name} {advertising_data.rssi}")

class GUI(Application):
    def __init__(self, state):
        super().__init__()
        self.state = state

    def content(self):
        with Window(title="BLE List"):
            with VBox():
                Label(f"Found {len(self.state.scanned_devices)} devices")
                for device, advertising_data in self.state.scanned_devices:
                    DeviceView(device, advertising_data)

....
```
![View Component](https://github.com/buganini/PUI/raw/main/screenshots/bleak_list.png)

## Layout & Styling
```python
# example/pyside6_feedparser.py

...
with VBox():
    Label(title).qt(StyleSheet={"font-weight":"bold"}) # QT-specific

    with HBox():
        with Scroll():
            with VBox():
                for i,e in enumerate(entries):
                    Label(e.title).click(self.entry_selected, i)
                Spacer()

        with Scroll().layout(weight=1): # Generic Layout Parameter
            if 0 <= selected and selected < len(entries):
                (Text(entries[selected].description)
                    .layout(padding=10) # Generic Layout Parameter
                    .qt(StyleSheet="background-color:white; color:black")) # QT-specific
...
```
![Layout & Styling](https://github.com/buganini/PUI/raw/main/screenshots/feed_parser_padding.png)


## Canvas
```python
# example/pyside6_canvas.py

from PUI.PySide6 import *

data = State()
data.var = 50

class QtExample(QtApplication):
    def content(self):
        with QtWindow(title="blah", size=(640,480)):
            with QtVBox():
                QtCanvas(self.painter, data.var)
                with QtHBox():
                    QtButton("-", self.on_minus)
                    QtLabel(f"{data.var}")
                    QtButton("+", self.on_plus)

    @staticmethod
    def painter(canvas, var):
        canvas.drawText(var, var/2, f"blah {var}")
        canvas.drawLine(var, var, var*2, var*3)

    def on_minus(self):
        data.var -= 1

    def on_plus(self):
        data.var += 1

root = QtExample()
root.run()
```
![Canvas](https://github.com/buganini/PUI/raw/main/screenshots/pyside6_canvas.gif)

## Cookbook
`python -m cookbook PySide6` (requires pygments for syntax highlight)

![Cookbook 1](https://github.com/buganini/PUI/raw/main/screenshots/cookbook1.png)
![Cookbook 2](https://github.com/buganini/PUI/raw/main/screenshots/cookbook2.png)

`python -m cookbook textual`
![Cookbook textual](https://github.com/buganini/PUI/raw/main/screenshots/cookbook_textual.png)

## Hot-Reload with Reloadium
[![Hot-Reload with Reloadium](https://img.youtube.com/vi/X716rwchPBM/0.jpg)](https://www.youtube.com/watch?v=X716rwchPBM)


# Backends
## Tier-1
* PySide6
## Lower Priority
* tkinter
    * or https://github.com/rdbende/Sun-Valley-ttk-theme
* flet
* textual (Text Mode)
    * no canvas

# Components
|Generic|PySide6|flet|tkinter|textual|
|-------|-------|----|-------|-------|
|Application|QtApplication|FApplication|TkApplication|TApplication|
|Window|QtWindow|FWindow|TkWindow|TWindow|
|HBox|QtHBox|FRow|TkHBox|THorizontal|
|VBox|QtVBox|FColumn|TkVBox|TVertical|
|Label|QtLabel|FLabel|TkLabel|TLabel|
|Button|QtButton|FElevatedButton|TkButton|TButton|
|Checkbox|QtCheckbox|FCheckbox|TkCheckbutton|TCheckbox|
|RadioButton|QtRadioButton|FRadio|TkRadiobutton|TRadioButton|
|Canvas|QtCanvas|FCanvas|TkCanvas|-|
|TextField|QtLineEdit|FTextField|TkEntry|TInput|
|ProgressBar|QtProgressBar|FProgressBar|TkProgressBar|TProgressBar|
|Scroll|QtScrollArea|FScroll|TkScroll|TScroll|
|Spacer|QtSpacerItem|FSpacer|TkSpacer|TSpacer|
|Text|QtText|FText|TkText|TText|
|Html|QtHtml|FHtml|-|-|
|MarkDown|QtMarkDown|FMarkDown|-|-|
|Combobox|QtComboBox|-|-|-|
|ComboboxItem|QtComboBoxItem|-|-|-|
|-|QtMenuBar|-|-|-|
|-|QtMenu|-|-|-|
|-|QtAction|-|-|-|
|-|QtMdiArea|-|-|-|
|-|QtMdiSubWindow|-|-|-|
|-|QtSplitter|-|-|-|

## Interfaces
* Button(text)
    * .click(callback, *cb_args, **cb_kwargs)
* Label(text)
    * .click(callback, *cb_args, **cb_kwargs)
* TextField(binding)
* ProgressBar(progress `0-1`)
* Checkbox(label, model)
* RadioButton(label, value, model)
* Canvas
    * .drawText(x, y, text)
    * .drawLine(x1, y1, x2, y2, color=0xFF0000, width=2)
    * .drawPolyline([x1, y2, ..., xn, yn], color=0xFF0000, width=2)
## Modifiers
* .layout(width=320, height=240, weight=1, padding=, margin=)
* .style(color=0xFF0000, bgColor=0x0, fontSize=16, fontWeight="bold", fontFamily="Arial")
* .qt(HorizontalPolicy=, VerticalPolicy=, SizeConstraint=, StyleSheet={})
* .flet(k=v)

# Hot Reload
Add these lines to your view file and run with [reloadium](https://github.com/reloadware/reloadium)
```python
import reloadium

# reloadium: after_reload
def after_reload(actions):
    PUIView.reload()
```


# TODO
* Lazy List
* StateObject decorator
* UI Flow
    * Navigation Stack
    * View Router
    * Model Window/Dialog
* Layout
    * ZBox
    * Grid
        * Row
        * Column
    * SwiftUI style overlay ??
* Canvas
    * Rect
    * Arc
    * Image
    * ...
* Table
* Tree
* Dialog
* Pydantic State