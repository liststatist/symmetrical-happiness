#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton, QLabel, QApplication, QGroupBox, QButtonGroup
from random import * 
app = QApplication([])

window = QWidget()
window.resize(250,200)
window.setWindowTitle('Memory Card')

text1 = QLabel('Какой национальности не существует?')
text2 = QLabel('Правильно')
text3 = QLabel('все')
button1 = QPushButton('Ответить')

group1 = QGroupBox('Варианты ответов')
group2 = QGroupBox('Результат теста')
RButton1 = QRadioButton()
RButton2 = QRadioButton()
RButton3 = QRadioButton()
RButton4 = QRadioButton()

RGroup1 = QButtonGroup()
RGroup1.addButton(RButton1)
RGroup1.addButton(RButton2)
RGroup1.addButton(RButton3)
RGroup1.addButton(RButton4)


Vlayout1 = QVBoxLayout()
Vlayout2 = QVBoxLayout()
Vlayout3 = QVBoxLayout()
Hlayout1 = QHBoxLayout()
Hlayout2 = QHBoxLayout()
Hlayout1.addWidget(RButton1)
Hlayout1.addWidget(RButton2)
Hlayout2.addWidget(RButton3)
Hlayout2.addWidget(RButton4)
Vlayout1.addLayout(Hlayout1)
Vlayout1.addLayout(Hlayout2)
Vlayout3.addWidget(text2, alignment = (Qt.AlignLeft | Qt.AlignTop))
Vlayout3.addWidget(text3, alignment = Qt.AlignHCenter)

group1.setLayout(Vlayout1)
group2.setLayout(Vlayout3)

Vlayout2.addWidget(text1, alignment = Qt.AlignHCenter)
Vlayout2.addWidget(group1)
Vlayout2.addWidget(group2)
Vlayout2.addWidget(button1)


class Question():
    def __init__(self,question,right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

        
list_questions = []
list_questions.append(Question('Какой газ преобладает в атмосфере Земли?', 'Азот (N₂)', 'Кислород (O₂)', 'Углекислый газ (CO₂)', 'Аргон (Ar)'))
list_questions.append(Question('Сколько планет в Солнечной системе (по современной классификации)?', '8', '9', '7', '10'))
list_questions.append(Question('Какова химическая формула воды?', 'H₂O', 'H₂O₂', 'CO₂', 'NaCl'))
list_questions.append(Question('Кто автор романа «Евгений Онегин»?', 'А. С. Пушкин', 'М. Ю. Лермонтов', 'Н. В. Гоголь', 'Ф. М. Достоевский'))
list_questions.append(Question('Какая столица у Франции?', 'Париж', 'Берлин', 'Мадрид', 'Рим'))
list_questions.append(Question('Сколько байт в одном килобайте (в компьютерной системе)?', '1024', '1000', '8', '100'))
list_questions.append(Question('Какой химический элемент обозначается символом Fe?', 'Железо', 'Фтор', 'Фосфор', 'Франций'))
list_questions.append(Question('Кто сформулировал закон всемирного тяготения?', 'Исаак Ньютон', 'Галилео Галилей', 'Альберт Эйнштейн', 'Николай Коперник'))
list_questions.append(Question('Сколько сторон у треугольника?', '3', '2', '4', '5'))
list_questions.append(Question('Какой океан является самым большим по площади?', 'Тихий', 'Атлантический', 'Индийский', 'Северный Ледовитый'))
shuffle(list_questions)

def show_r():
    group1.hide()
    group2.show()
    button1.setText('Следующий вопрос')

def show_q():
    group2.hide()
    group1.show()
    button1.setText('Ответить')
    RGroup1.setExclusive(False) 
    RButton1.setChecked(False)
    RButton2.setChecked(False)
    RButton3.setChecked(False)
    RButton4.setChecked(False)
    RGroup1.setExclusive(True) 

answers = [RButton1,RButton2,RButton3,RButton4]


def aXc(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text1.setText(q.question)
    text3.setText(q.right_answer)
    show_q()



def check_a():
    if answers[0].isChecked():
        window.score +=1
        show_c('Правильно')
    else:
        show_c('Неправильно')
        
def show_c(res):
    text2.setText(res)
    show_r()


def next_question():
    window.cur_question +=1
    window.total += 1
    if window.cur_question >= len(list_questions):
        print('- Всего вопросов:',window.total,'\n','- Правильных ответов:',window.score,'\n','- Рейтинг:',window.score/window.total*100)
    else:
        q = list_questions[window.cur_question]
        aXc(q)


def click_ok():
    if button1.text() == 'Ответить':
        check_a()
    else:
        next_question()



button1.clicked.connect(click_ok)


window.score = 0
window.total = 0
window.cur_question = -1
window.setLayout(Vlayout2)
group2.hide()
next_question()

window.show()
app.exec_()
