from PyQt5.QtWidgets import QMessageBox


class WrongValueIn_hex2rgb(Exception):
    pass


class WrongLenIn_hex2rgb(Exception):
    pass


class Error:
    scheme_bd_is_exist = False

    def __init__(self):
        self.error_msg = QMessageBox()

    def scheme_ChangeName(self, _is='None'):
        print('1')
        if Error.scheme_bd_is_exist:
            if _is == 'None':
                self.error_msg.setText('Вы не выбрали имя для изменения.\n'
                                       'Щелкните два раза по имени, которое '
                                       'хотите изменить и только потом '
                                       'нажимайте на кнопку)')
            if _is == 'notNull':
                self.error_msg.setText('Вы выбрали не имя для изменения.\n'
                                       'Щелкните два раза по имени, '
                                       'которое хотите изменить.')
            if _is == 'notStr':
                self.error_msg.setText('Вы ввели неправильное имя!')

            self.error_msg.setWindowTitle('Error')
            self.error_msg.exec_()

    def scheme_seeGrid(self):
        self.error_msg.setText('Извините, пока не работает.')
        self.error_msg.setWindowTitle('Sorry')
        self.error_msg.exec_()

    def scheme_open_db(self):
        if Error.scheme_bd_is_exist:
            self.error_msg.setText('Вы ввели не верное имя для темы!\n'
                                   'Пожалуйста, используйте только буквы '
                                   'и цифры.')
            self.error_msg.setWindowTitle('Error')
            self.error_msg.exec_()

    def scheme_delete(self, _is='None'):
        print(Error.scheme_bd_is_exist)
        if Error.scheme_bd_is_exist:
            if _is == 'None':
                self.error_msg.setText('Вы не выбрали, что удалять.\n'
                                       'Щелкните два раза по элементу '
                                       'строчки, '
                                       'которое хотите удалить и только потом '
                                       'нажимайте на кнопку)')
        else:
            pass

            self.error_msg.setWindowTitle('Error')
            self.error_msg.exec_()

    def scheme_setName(self):
        self.error_msg.setText('Вы ввели не верное имя для темы!\n'
                               'Пожалуйста, используйте только буквы и цифры.')
        self.error_msg.setWindowTitle('Error')
        self.error_msg.exec_()

    def scheme_itDoesnt_do(self):
        self.error_msg.setText('Извините, не работает')
        self.error_msg.setWindowTitle('Error')
        self.error_msg.exec_()

    def config(self):
        self.error_msg.setText('Может работать некорректно')
        self.error_msg.setWindowTitle('Error')
        self.error_msg.exec_()
