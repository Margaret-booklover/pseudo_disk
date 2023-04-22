# pseudo_disk
Что работает:
реализовать проверку логина и пароля пользователя с формы авторизации
Должна быть таблица с данными пользователей
Поля файла: имя, MIME-тип, размер, дата изменения и пр.
должно быть дерево папок
в таблице с файлами есть поле foreignId - указатель на пользователя - и предусмотреть что-то для папок
создать отдельно модель “Папка” с ссылкой на владельца и родителя
реализовать загрузку файла
только владелец файла/папки может изменять ее
другим пользователям не должны быть видны чужие файлы
Чего нет:
при добавлении файла/папки в выпадушке для поля “родительская папка” отображаются все папки из БД, а не те которые доступны пользователю
с CORS даже не разбиралась, так что его вообще нет
полный путь до файла? не, не слышали
по-хорошему, я хотела сделать так, чтобы null-директория была корнем файловой системы и в ней были видны только те файлы и папки, у которых родитель - null. Но сейчас в этой директории отображаются все доступные объекты
кстати об объектах, файлы лежат отдельно от папок, а надо бы чтобы они были по одному пути
про валидацию тоже можно не вспоминать. Хотя что здесь валидировать? Там из свободных полей только имя папки
проверка существующего пользователя происходит на стороне приложения, а создание - командой create superuser в консоли
