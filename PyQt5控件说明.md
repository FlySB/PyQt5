# PyQt5控件说明

## 基础控件

### 按钮

* QPushButton
* QCommandLinkButton
* QRadioButton
* QCheckBox

### 输入控件

#### 纯键盘输入

* QLineEdit

  单行文本

* QTextEdit

  多行文本（可输入图片，超链接）

* QPlainTextEdit

  多行文本（仅输入文字）

* QKeySequeneEdit

  采集快捷方式

#### 步长调节

* QDateTimeEdit
  * QDateEdit
  * QTimeEdit
* QSpinBox
* QDoubleSpinBox

#### 组合框

* QComboBox
* QFontComboBox（字体选择）

#### 滑块（鼠标）

* QDial（旋钮）
* QSlider （滑块）
* QScrollBar（滚动轴）

#### 橡皮筋选中

* QRubberBand

#### 对话框

* QColorDialog（颜色选择）
* QFileDialog（文件选择）
* QFontDialog（字体选择）
* QInputDialog（输入对话框）

#### 日期

*  QCalendarWidget

### 展示控件

* QLabel（标签展示：文本、图片、动画、超链接）
* QLCDNumber（LCD效果显示）
* QProgressBar（进度条：用于下载，加载进度）
* QDialog（对话框）
  * QMessageBox（展示各种类型的消息）
  * QErrorMessage（展示错误消息）
  * QProgressDialog（展示进度条）

## 高级控件

### 容器控件

* QToolBox
* QDialogButtonBox（按钮容器）
* QGroupBox（分组控件）
* QMdiArea和QMdiSubWindow（子窗口容器）

### 结构控件

* QMainWindow
  * QMenuBar
    * QMenu
  * QToolBar
    * QToolButton
  * QStatusBar（窗口底部，状态栏）

* QTabWidget（标签结构）
  * QTabBar

* QStackedWidget（栈结构：多个界面，点击按钮进入下一个）
* **QSplitter（分割结构：可VNPY）**
* QDockWidget

### 滚动控件

* QAbstractScrollArea
  * QTextBrowser（文本浏览器）
  * QScrollArea（滚动区域）
  * QAbstractItemView
    * QColumnView（列视图）
    * QHeaderView（头部视图）
    * QListView
      * QListWidget
      * QUndoView
    * QTableView（表格）
    * QTreeView（树结构）
  * QMdiarea
  * QGraphicsView（画图软件）

### 辅助控件

* QFocusFrame（焦点框）
* QSizeGrip（右下角鼠标拖动提示）
* QDesktopWidget（获取桌面信息控件）

### 其他

* QDialog（向导/打印）
  * QWizard（软件安装向导）
  * QAbstractPrintDialog（打印）
    * QPrintDialog
  * QPrintPreviewDialog（打印预览）
    * QPrintPreviewWidget
  * QPageSetupDialog（页面设置）
* QSplashScreen（欢迎界面）
* QVideoWidget（视频播放）
* QCameraViewfinder（相册预览）
* QWebEngineView（浏览器）