import locale


def get_system_language():
    """
    This method is to detect the system language, in this way, we can avoid to use hard code to refer
    to title or program. We can add different languages, but for now we are going to use Eng and Spanish
    :return: the specific language
    """
    language = locale.getdefaultlocale()[0]

    if 'en' in language or 'EN' in language:
        return 'english'
    else:
        return 'spanish'


def get_app_titles(language):
    """
    This method is to return the right name of the actual programs according to the system language,
    in this way, we avoid future possible issues.
    :param language: system language
    :return: the right dict
    """
    if language == 'english':
        return {
            'calc': 'Calculator',
            'notepad': 'Notepad'
        }
    # spanish
    else:
        return {
            'calc': 'Calculadora',
            'notepad': 'Bloc de notas'
        }
