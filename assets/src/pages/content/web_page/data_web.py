import flet as ft
from assets.variable import *
# 1 урок html
html_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Добро пожаловать на курс старшего программирования! Вначале будет просто, будет казаться, что ты гений прогарммирования, потом будет невероятно сложно и захочется бросить, и вот потом, если продолжить несмотря ни на что - у тебя получится и ты станешь программистом. Удачи!'),width=700),
        ft.Container(ft.Text('Почему WEB? Потому что это просто, несмотря на то, что программирование - сложная штука. Важно сделать первый шаг, чтобы хоть что-то начало получаться. Идеальная точка входа здесь - это сайты. Рекорд ученика - пробежал html и css за 2 месяца. Вам желаем того же. HTML и CSS строго говоря - даже не языкы программирования. Это язык гипертекстовой разметки и каскадная таблица стилей. Первый язык программирования на вашем пути - это Java Script. Сложность начнется там, а до этого вы уже научитесь верстать сайты. От простого к сложному.'),width=700),
        ft.Container(ft.Text('Хватит болтовни, начинаем. На заняия удобнее ходить со своим ноутбуком (если есть), или как минимум с флешкой, на которую будете сохранять данные. На общих компах хранить не до конца безопасно. Есть жулики, которые могут "случайно" удалить'),width=700),
        ft.Container(ft.Text('Создаем папку на рабочем столе, называем своей именем и фамилией. Правой кнопкой мыши по папке - открыть с помомощью VScode. Vscode - это редактор кода. Код можно писать хоть в блокноте, но в редакторе - удобнее. Есть подсветка кода и много других фишек. Слева в директории правой кнопкой мыши - создать файл, имя - 1.html. Далее в зоне кода - вводим ! и нажимаем enter'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/1.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь зайди в папку и открой свой файл. Увидел? Он открылся в браузере. Винда уже понимает, что файлы с расширением .html - это сайты, и открывать их нужно в браузере. Теперь найди в коде <title></title> и между ними введи что-нибудь. Например, <title>Чебурек</title>. ернись в браузер и обнови страницу своего сайта. Что нибудь изменилось? Да! Название вкладки изменилось на то, что ты написал. Как это работает?'),width=700),
        ft.Container(ft.Text('Какие-то слова внутри <> называются теги. С помощью тегов мы говорим с браузером. Программирование - это общение. Не зря есть языки программирования. Это как языки в реальной жизни. Чтобы говорить с китайцем, нужно знать язык - китайский. А чтобы говорить с бразуром, нужно занть язык - html. Просто, не правда ли? Каждая часть системы говорит на своем языке. Например, айфоны говорят на языке Swift, андроиды - на Котлине, большая часть винды - на языке C.'),width=700),
        ft.Container(ft.Text('Каждый тег что-то говорит браузреу. Разберем, что.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Когда мы ввели ! и нажали enter - мы раскрыли сниппет. Это подсказки от VSCode, чтобы не писать часто используемые конструкции кода самостоятельно каждый раз. Абсолютно каждая страница в интернете включает в себя базу - код, который изображен выше. Можете сами проверить - в браузере перейдите на любой сайт, в пустом месте правой кнопкой мыши - просмотреть код страницы.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/3.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Да, код яндекс музыки может выглядеть пугающе, или даже уродски, но это потому, что его сгенерировал фреймворк, в котором работали люди. Что-это такое, разберем позже. Через пол годика) Но даже в таком коде вы увидите уже знакомые теги - html, head, body.'),width=700),
        ft.Container(ft.Text('Пойдём дальше. Внутри тега body пишется видимая часть сайта. Напишите там любой текст, зайдите в браузер и обновите страницу с сайтом.'),width=700),
        ft.Container(ft.Text('Текст появился нас странице? Прекрасно! Теперь попробуйте поместить введенный текст внутрь тега h1. Должно получиться так - <h1>Текст</h1>. Затем перейдите в браузер и обновите страницу. Текст стал большим и жирным?'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/4.gif',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В структуре сайта html отвечает за скелет сайта. С помощью html добавляется текст и картинки. Никакого дизайна. За дизайн и красоту будет отвечать CSS. Следующие 6 уроков ты будешь учиться работать с разными тегами в html. Их не так много. На самом деле весь html можно пройти часов за 6. Время прохождения зависит только от того, насколько ты будешщь тормозить в процессе.'),width=700),
        ft.Container(ft.Text('Как будет выглядеть обучение дальше? Я даю тебе картинку сайта. Тебе нужно написать код по этой картинке. Чтобы сайт выглядел так же. Начнем? Вот первый сайт, который ты должен сделать.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/5.png',width=700),margin=ft.margin.only(left=0)),
        
        ft.Container(ft.Text('Сайт можно открыть по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_1.html',selectable=True),width=700),
        ft.Container(ft.Text('Для написания сайта нужно узнать о нескольких тегах.'),width=700),
        ft.Container(ft.Text('Теги h1 - h6. Это заголовки. h1 - лавный закголовок и самый большой и жирный. h6 - самый маленький заголовок. Попробуйте подобавлять внутрь текст и посмотрите, как он отобразится'),width=700),
        ft.Container(ft.Text('Тег p - абзац. Если напсиать текст на разных строках, он по умолчанию выведется на одной. Браузеру нужно явно сказать, что это абзац - его с новой строки.'),width=700),
        ft.Container(ft.Text('Помимо тегов, которые уже что-то делают, у них могут быть персональные настройки - атрибуты. Пишутся они так - <p align="center">Текст</p>'),width=700),
        ft.Container(ft.Text('Внтруи открывающего тега, после названия тега. В данном случае align - выровнять, center - по центру. Так же можно выровнять по левому краю (left) и по правому краю (right)'),width=700),
        ft.Container(ft.Text('Сайт пиши сверху вниз, строка за строкой Удачи!'),width=700,margin=ft.margin.only(bottom=40)),
    ])
)
# 2 урок html
html_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('На втором уроке научимся работать со списками.'),width=700),
        ft.Container(ft.Text('Списки бывают 3-х типов - нумерованные, ненумерованные, списки с описанием.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/15.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт, который нужно сделать весьма прост. Создайте новый файл, назовите его 2.html и вперед!'),width=700),
        ft.Container(ft.Text('Сайт доступен по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_2.html',selectable=True),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 3 урок html
html_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Сегодня научимся работать с картинками. Добавлять их на страницу, изменять размер, позиционировать'),width=700),
        ft.Container(ft.Text('Для добавления картинки на страницу, используем тег img. Он одинарный! Закрывающего тега, как у большинства у него нет. <img>'),width=700),
        ft.Container(ft.Text('У тега img есть множество атрибутов. Основной - src (путь). Так же атрибутами можно задать ширину (weight) и высоту (height) изображения'),width=700),
        ft.Container(ft.Text('Путь указывается относительный (относительно файла в котором сейчас работаем), либо абсолютный (от корня операционки). Относительные пути предбпочитительнее, т.к. при занрузке сайта на сервер, корневые каталоги могут измениться, картинки не будут найдены. С относительным путём проблем нет практически никогда.'),width=700),
        ft.Container(ft.Text('Предположим, что картинка находится в папке img, называется - 1.png, на уровне вместе с папкой img находится файл 3.html. Тогда относительный путь будет иметь вид - url="assets/src/pages/content/web_page/img/1.png"'),width=700),
        ft.Container(ft.Text('А весь тег получится таким - <img src="assets/src/pages/content/web_page/img/1.png",width=400,height=400>'),width=700),
        ft.Container(ft.Text('Попробуй добавить какую-нибудь картинку на сайт.'),width=700),
        ft.Container(ft.Text('Кстати, сайт к этому уроку будет выглядет так:'),width=700),
        ft.Container(ft.Text('Поулчить сайт по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_3.html',selectable=True),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Единственный вопрос, который осталось решить - как сделать так, чтобы картинки стояли вокруг текста слева и справа? Для этого используй атрибут выравнивание - align. ПРикол с ним в том, что когда, например картенке прописываешь align="right", то контент, который следует после в коде, будет огибать картинку справа. '),width=700),
        ft.Container(ft.Text('Мы коснулись блочных и строчных элементов. Текст - это блочный элемент. Даже если в теге <p> написать одно слово, это слово займет всю ширину строки, и не позволит другому тексту или картинкам заскочить на свою строку. Align меняет это поведение, и делает блочный элемент - строчным. Строчные элементы занимают ровно столько места, сколько для них выделено.'),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 4 урок html
html_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В 4-ом сайте научимся переходить на другие страницы. Раньше весь сайт у нас состоял из одной страницы. В реальность у сайтов могут быть десятки, а то и сотни страниц, которые связаны между собой ссылками.'),width=700),
        ft.Container(ft.Text('В четвертом сайте будет три страницы - 3 отдельных файла html, каждый из которых будет содержать ссылку на соседний. Создайте папку с названием - 4 сайт (или как-то так) и создайте в ней три файла. (например, 4_1.html,4_2.html,4_3.html)'),width=700),
        ft.Container(ft.Text('За ссылки в html отвечает тег <a>. Атрибут href показывает, куда ссылка должна перевести.'),width=700),
        ft.Container(ft.Text('Так <a href="yandex.ru">Нажми на меня</a> создаст текст/ссылку - нажми на меня, при клике по которой тебя перебросит на сайт яндекса.'),width=700),
        ft.Container(ft.Text('Чтобы сделать многостраничный сайт, ножно прописать относительные ссылки на соседние файлы (по тому же принципу, что и в картинках)'),width=700),
        ft.Container(ft.Text('Вот вся информация, что тебе нужна. В остальном - ничего нового.'),width=700),
        ft.Container(ft.Text('Сайт получишь по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_4.html',selectable=True),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/9.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/10.png',width=700),margin=ft.margin.only(bottom=40)),
    ])
)
# 5 урок html
html_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('5 сайт - это работа с таблицами. В реальности таблицы на html ты, наверное, никогда писать не будешь, однако они закладывают способ мышления, который нужно усвоить.'),width=700),
        ft.Container(ft.Text('Таблицы состоят из строк, внутри которых находятся ячейки. Это принцип многих интерфейсов.'),width=700),
        ft.Container(ft.Text('Таблицу создает тег <table></table>. Но сам по сибе он не даст ничего, ведь в нем нет строк и ячеек.'),width=700),
        ft.Container(ft.Text('Строку создает тег <tr></tr>, ячейку - тек <td></td>'),width=700),
        ft.Container(ft.Text('Вставь к себе на сайт следующий код - <table><tr><td>1</td><td>2</td><td>3</td></tr></table> и посмотри, что получится. А теперь внтурь тега table добавь атрибут border="1". У таблицы появится рамка и станет чуть понятнее, что происходит'),width=700),
        ft.Container(ft.Text('Теперь ты знаешь, как создавать строки и ячейки. Если присмотреться к таблице, то некоторые ячейки объеденены - две в одну. Это делаетс с помощью атрибута colspan="2" или rowspan="2" внутри td. Эти атрибуты объединяют 2 ячейки по горизонтали или вертикали.>'),width=700),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_7.html',selectable=True),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/11.png',width=700),margin=ft.margin.only(left=0)),
    ])
)
# 6 урок html
html_6 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Поздравляю! Ты в выпусконом проекте HTML. Надеюсь, что предидущие 5 уроков пролетели для тебя незаметно.'),width=700),
        ft.Container(ft.Text('Здесь нужно собрать сайт вк на чистом html, состоящий из 3-х страниц.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/12.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/13.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/14.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Подсказка будет всего одна, связанная со структурой страницы. Как сделать такую структуру? С помощью таблицы! Не зря же мы их проходили. Сейчас сайты на таблицах уже ни кто не строит, но лет 20 назад только так и делали, css еще не был настолько развит, а на таблицах неплохо писалась адаптивная структура'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/html/16.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Вся первая страница - это таблица, состоящая из 1 строки и 3 ячеек. В первой ячейке - меню. Так вот меню - это тоже таблица. Таблица 2х8. Получается таблица в таблице. Когда будет много и важно в нем не запутаться. На то это и выпускной проект HTML. Удачи!'),width=700),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_html/lesson_sayt_8.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 1 урок css
css_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Поздравляю! Ты изучил HTML и переходишь к CSS. CSS отвечает за дизайн страницы. Научимся же делать красиво) Код CSS пишется в отдельном файле - style.css. Первым делом нам нужно связать страницу HTML и CSS. Для этого в head HTML страницы подключаем внешний файл с помощью: < link rel="stylesheet" href="style.css" type="text/css"> CSS работает по следующему принципу: тег{Свйоство1; Свойство2; Свойство3;} Например: p{color:red;} - покрсит весь текст, находящийся в p в красный цвет. В конце каждого свойства нужно ставить точку с запятой. Так мы показываем браузеру конец строки. А как быть если мы не хотим красить все теги p в красный, а, например только один? Для этого нужно тегу p даём идентификатор: <p id="text1"> В css: #text1{color:green;} - покарсит текст тега с id="text1" в зелёный цвет. Не может быть два тега с одним id. Чтобы покрасить несколько тегов p в один цвет, используем класс: <p class="text2">. В CSS к классу обращаемся через точку: .text2{color:black;}'),width=700),
        ft.Container(ft.Text('КОРОЧЕ - просто позови учителя, он покажет, как работает css за 5 минут и начнешь делать уроки'),width=700),
        ft.Container(ft.Text('А ниже сайт, который нужно сделать.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/1.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_1.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 2 урок css
css_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Разберёмся, что такое блочные и встроенные элементы. Блочные - занимают всю строку, а встроенные, только то место, которое под них выделенно. Что это значит? Сделайте тег p с небольшим текстом и дайте ему рамку через CSS. Рамка задаётся свойством: border:1px solid black; где 1px - толщина рамки, solid - тип рамки, здесь - сплошная, black - цвет рамки. Вы увидите, что рамка идёт не вокруг текста, а растянута во всю ширину экрана. Она идёт даже там, где нет текста. Это и называется блочный элемент. А что же тогда встроенный элемент? Встроенный элемент, это, например тег span. Напишите такую конструкцию: <span>Текст</span> Далее дайти тегу span id, и в CSS пропишите рамку. Вы увидите, что рамка идёт только вокруг текста. Это и есть встроенный элемент. Чтобы вместо маркера списка поставить картинку, используем свойство CSS: list-style-image: url(img.png);'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/2.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_2.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 3 урок css
css_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В уроке про таблицы HTML я говорил, что ранее таблицы использовались для разметки страницы, но сменились свойствами CSS и тегом DIV. Так вот пора с ним познакомиться. Что же такое DIV? С его братаном - тегом span вы уж езнакомы. Теги DIV и SPAN - это невидимые коробочки, внутрь которых можно положить что угодно, и через CSS задать этим коробочкам любой размер и положение на странице. Синтаксис: <div id="box1"><p>Текст></p><img></div> В css: #box1{width:200px;height:200px;border:1px solid black;margin-top:50px;margin-left:100px;} Получим квадрат 200х200 пикселей с чёрной рамкой, внутри которого лежит текст и картинка. Квадрат находится на расстоянии 50 пикселей от верхнего края и 100 пикселей от левого края.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/3.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_3.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 4 урок css
css_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В данном сайте новых блоков особо нет. Единственное, что нужно знать - это то, что тегам можно давать блочные и встроенные свойства напрямую через CSS Для этого в css для выбранного тега прописываем свойство: display:block; - чтобы сделать элемент блочным display:inline-block; - чтобы сделать элемент встроенным, с вкелючением некоторых свойств блочного элемента display:inline; - чтобы сделать элемент встроенным У свойства display есть ещё несколько значений. Если хотите изучить их подробнее, идите в справочник) В примере сайта вам предложена только одна страница, ваша задача сделать сначала её - главную страницу сайта, а потом самостоятельно придумать и сделать остальные - услуги, цены, контакты в таком же стиле, что и главная.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/4.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_4.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 5 урок css
css_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В уроке объясню только одно - как убрать нижнее подчёркивание у ссылки. Хотя и сами могли это найти в справочнике или в интернете. text-decoration:none; Всё остальное вы и так знаете. На этом всё. Больше ничего вам не расскажу. Будете искать ответы сами. Думаете это шутка?) А вто и нет. На самом деле я серьёзно. Следующее чему вы научитесь - это не новому тегу или атрибуту, а задавать правильные вопросы и искать на них ответы. В данному курсе я вас не смогу обучить вообще всему. Я закладываю фундамент, а вот дом на нём вам предстоит строить самостоятельно. Учитесь.)'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/5.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_5.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 6 урок css
css_6 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Ух ты! До конца CSS осталось всего два сайта. Но каких?) Очень интересных. Эти два сайта - реальны. Я вытащил их из сети. То есть вы повторите процесс разработки какого-то программиста из другой страны. Дерзайте)'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/6.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_6.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 7 урок css
css_7 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Финальный сайт CSS! Сделайте его, и попадёте в нирвану. Станете соколом, который освоил вёрстку сайтов! Сможете собирать свои сайты. Ты очень крутой! Удачи!'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/7.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/8.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/9.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/10.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/11.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/css/12.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сайт можно найти по ссылке - https://robocore-kamensk.ru/courses/web/lesson_css/lesson_sayt_7.html',selectable=True),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)

# 1 урок js
js_1 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('УРА! Начало Java Scrit. Первый урок. Управялем html',text_align='center'),width=700),
        ft.Container(ft.Text('Java Script - это первый полноценный язык программирования в вебе, с которым вы сталкиваетесь. Html - язык гипертекстовой разметки, css- каскадная таблица стелей. Оба этих языка не являются языками программирования в полной мере. Прежде всего, в них нет логики, переменных, уловия и прочего, что так необходимо настоящим языкам программирования.'),width=700),
        ft.Container(ft.Text('В течение следующих 6 уроков ты узнаешь в полной мере, что такое фронтенд и бэкенд. Если коротко, фронтенд - это часть сайта, с которой пользователь взаимодействуем напряму. Может увидеть ее, поторогать руками, понажимать кнопки. Код фронтенда полностью загружается в браузер, при запросе к сайту. И в нем можно покапаться. Бэкенд же, наоборот, часть сайта - которую пользователь ни как не может потрогать. Она полностью недосигаема для него. Максимум, что он может - это общаться с бэкендом через запросы. Делаешь запрос к какому-либо серверу, он возвращает ответ. Например, '),width=700),
        ft.Container(ft.Text('Например, перейди в браузере по ссылке - https://jsonplaceholder.typicode.com/todos',selectable=True),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-38-42.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Сервер вернул данные спсиком. Это и есть взаимодействие с бэкендом. Ты у него что-то просишь, он тебе это дает. В данном случае сервис вернул список задач. jsonplaceholder - это сервис фейкового api. То есть у него есть сервер, который по определенным запросам отдает определенные данные. Нужен этот сервис как раз для обучения.'),width=700),
        ft.Container(ft.Text('Основная задача java script - это как раз просить у сервера данные, и как то их отрисовывать. Конечно, у него есть и множество вспомогательных задач. Например, рисовать активный дизайн, слайдеры, делать красивые анимации, обрабатывать и валидировать формы. С этим он справляется без проблем. '),width=700),
        ft.Container(ft.Text('Давайте что-нибудь наконец напишем. Для этого создайте новую папку, назовите её - JS. В ней будете хранить все сайты моделя по js. Js, как и css, сам по себе существовать не может. html всему голова. Поэтому для начала создайте простенький проект - файл html, добавтье в нем пару p с текстом, заголовок. ПОдключите к нему css и дайте стили тексту, который написали. Дайте, например, размер, цвет, курсив. Это вы уже умеете и проблем возникнуть не должно.'),width=700),
        ft.Container(ft.Text('Теперь тут же создайте файл script.js, пока оставим его пусты. Для начала подключим файл script.js к html файлу. Делается это с помощью тега <script></script>, которому нужно задать путь к файлу - src. Причем т.к. это тег рабочей среды, пишется он внутри body. Правильно будет подключать скрипты внизу body. Логически для браузера, они должны загружаться и подключаться в полседнюю очередь - когда html и css уже загружены. Полный код проекта будет выглядеть так:'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-45-17.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-45-46.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь перейдите в файл скриптов (script.js) и напишите там всего одну строку - \nalert("Лолоолололо")\nОткройте сайт в браузере и посмотрите, тчо будет. '),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-48-26.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Если вы увидели уведомление - поздравляю, js подключился и все работает.'),width=700),
        ft.Container(ft.Text('Вначале убедимся, что js - это дейтсвительно язык программирования. Для этого создадим пару переменных, поскладываем их и выведем в консоль.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-52-25.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('В последней редакции JS, в конце строки не обязательно ставить точку с запятой. Ранее она была обязательна, без нее выводилась ошибка. После того, как написали скрипт, перейдите на сайт в браузере, откройти инструменты разработчика. Вы ими пользовались на этапе css. И перейдите во вкладку console. Сюда и будет выволится информация по js. То, что мы захотим вывести сами - через console.log(), либо ошибки js, если они будут.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-52-41.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь давайте создадим простую форму, два инпута, куда можно вводить информацию и кнопку. Сделаем мини проект - калькулятор. С него же все вроде начинают. '),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_08-59-20.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-00-08.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Добавьте каких-нибудь стилей, чтобы смотрелось красиво. Сейчас, если вводить числа и жать кнопку, естетсвенно, ничего не произойдет. Нет логики работы. Не скрипта. Напишем его.'),width=700),
        ft.Container(ft.Text('Первое, что нужно сделать - научится получать данные, которые ввели в инпуты внутри js. '),width=700),
        ft.Container(ft.Text('document.getElementsByClassName("input_1") - эта штука ищет в дереве html элемент с классом input_1, но прикол в том, что классов на странице может быть много, поэтому getElementsByClassName всегда возвращает список. Нам в нем нужно взять первый элемент (нумерация индексов в массиве начинается с нуля, поэтому нулевой элемент) - document.getElementsByClassName("input_1")[0].value, ну и вконце получаем его значение - value. Но чтобы это сработало, нам нужно вначале нажать на кнопку. Для этого вешаем на кнопку обработчик - функцию, которая будет вызываться при нажатии.'),width=700),
        ft.Container(ft.Text('СОздадим в js функцию, обзовём её "click_sum", внутри получим значения, введенные в инпуты и выыведем в консоль их сумму. Так же повесим обработчик -onclick на кнопку. То, что напишем в onclick у кнопки, будет вызвано при клике на кнопку. Функцию туда и запишем. Весь код будет выглядеть так:'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-23-22.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-24-11.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Зайдите на сайт, введите значения в инпуты и нажмите кнопку. Посмотрите, что получится.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-26-02.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ошибок нет, все сработало. Однако тип ввода в инпута у нас - текст. Значит, при сложении у нас складываюся два числа, записанные как текст. Сами узнайте, как преобразовать текстовое число в число. Если совсем не получится, зовите препода.'),width=700),
        ft.Container(ft.Text('Следующий шаг - полученный ответ нам нужно из js записать в html, то есть в тег <p> с текстом Ответ: '),width=700),
        ft.Container(ft.Text('Для этого так же вначале нужно получить это элемент через getElementByClassName, после чего через свойство textContent зададим то, что должно лежать внутри пэшки. Весь код выглядит так:'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-32-51.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-33-21.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('У вас должно выводить всё правильно, то есть 1+2=3, а не 12. Разберитесь с этим сами.'),width=700),
        ft.Container(ft.Text('Вводная часть урока закончена. Вот так просто можно получать элементы в java script из html, а так же манипулировать html с помощью js. У каждого тега есть набор свойств, которыми мы можем управлять. В течение следующих 6 уроков, вы познакомитесь с онсовными свойствами и научитесь ими пользоваться'),width=700),
        ft.Container(ft.Text('Что же дальше? Дальше сделайте полноценный калькулятор. Он должен выглядить примерно вот так:'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_09-38-34.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ну и , конечно, он должен работать! Удачи.'),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text(''),width=700),
        
    ])
)
# 2 урок js
js_2 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('Запросы в js',text_align='center'),width=700),
        ft.Container(ft.Text('Сегодня научимся стучаться по разным ссылкам с помощью js и парсить ответ.'),width=700),
        ft.Container(ft.Text('Один из самых правильных и простых спососбов делать запросы и получать ответ в js - это fetch. Работает он следующим образом :'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_10-45-24.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Для примера, сделаем запрос по ссылке с первого урока, где нам возвращают спсок задач'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_10-46-04.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('fetch("https://jsonplaceholder.typicode.com/todos") - это тело запроса. Через точку говорим, что будем делать потом:\n.then(res => res.ok ? res.json() : console.log("Завершено с ошибкой")) - если резульата пришел с кодом ответа 200, все ок и мы преобразуем джейсон, который пришел в объект. Если код ответа не 200, то выводим текст с ошибкой'),width=700),
        ft.Container(ft.Text('.then(data => console.log(data)) - распечатываем в консоль данные, которые пришли в ответе'),width=700),
        ft.Container(ft.Text('Что такое код ответа? Слышали про ошибку 404? Когда пытаетесь попасть на страницу, которой не сущетсвует. Так вот это и есть коды ответа. Код ответа 200 - все хорошо. 400 - ошибки на стороне клиента, 500 - ошибки на стороне сервера. Давайте, к примеру попробуем изменить ссылку, сделаем ее неправильной:'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_10-52-00.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('И посмотрим, какой ответ вернет сервер.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_10-53-03.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('И вот вопрос, ну получили мы эти данные, дальше то с ними что делать? Отрисовать в HTML. Вот мы и начинаем делать полноценный фронтенд. Попробуем для начала, как есть отрисовать все данные в каком-нибудь диве.'),width=700),
        ft.Container(ft.Text('Для этого начнем писать более правильный код. Данные, которые нам возвращает fetch, засунем в функцию, из которой уже и будем работать.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-15-28.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Убедитесь, что все работает как и прежде в браузере. Теперь мым ожем управлять данными из изолированной функции'),width=700),
        ft.Container(ft.Text('Создадим див в html, дадим ему класс - content, получим его в js и засунем туда ответ от сервера. Посмотрим, что получится.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-22-24.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-25-58.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Ответ приходит в виде массива объектов. Чтобы отрисовать каждую задачу отдельно, нам нужно итерироваться по этому самому массиву. Сделаем это с помощью старого доброго for'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-29-47.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-30-01.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Теперь мы получили каждый объект в отдельности. Осталось только получить нужные нам значения ключей объекта. В первую очередь нас интересует title, в нем и хранится текст самой задачи. Получим его.'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-33-04.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-33-22.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Отлично! Мы добрались до тех данных, что нам нужны. Теперь остается отрисовать их на странице. Сделаем это, добавив внутрь див - пешки с текстом задачь. Внутрь тега можно вставить код через js. Это делается с помощью свойства - .innerHTML'),width=700),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-38-43.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Image(src='assets/src/pages/content/web_page/img/js/2024-11-15_11-38-56.png',width=700),margin=ft.margin.only(left=0)),
        ft.Container(ft.Text('Готово! Мы отрисовали данные, полученные серез запрос. Ответ от сервера обычно бывает двух видов. Это либо единичные данные, тогда возвращается обычный джейсон объект. Если же мы запрашивает сет данных, то чаще всего они вернутся массивом объектов.'),width=700),
        ft.Container(ft.Text('Если что-то в процессе не получилось, проси препода помочь. Когда дойдешь до этой строчки, значит теория урока кончилась, теперь будет практика. Попроси препода дать тебе задание к уроку. Там нужно будет распечатать данные не списком, а в виде красивых карточках, которые имеют адаптив через flex. У тебя всё получится. Ты сильный. Удачи.'),width=700),
        ft.Container(ft.Text(''),width=700),
        ft.Container(ft.Text(''),width=700),
    ])
)
# 3 урок js
js_3 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)
# 4 урок js
js_4 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)
# 5 урок js
js_5 = ft.Container(
    ft.Column(controls=[
        ft.Container(ft.Text('В РАЗРАБОТКЕ',text_align='center'),width=700,margin=ft.margin.only(top=300)),
        ft.Container(ft.Text('У нас лапки, но мы работаем. Скоро здесь что-то появится.',text_align='center'),width=700),
    ])
)


less_print = {
    'HTML 1': html_1,
    'HTML 2': html_2,
    'HTML 3': html_3,
    'HTML 4': html_4,
    'HTML 5': html_5,
    'HTML 6': html_6,
     'CSS 1':  css_1,
     'CSS 2':  css_2,
     'CSS 3':  css_3,
     'CSS 4': css_4,
     'CSS 5': css_5,
     'CSS 6': css_6,
     'CSS 7': css_7,
      'JS 1':  js_1,
      'JS 2':  js_2,
      'JS 3':  js_3,
      'JS 4':  js_4,
      'JS 5':  js_5,
}