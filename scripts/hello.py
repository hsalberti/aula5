#!/usr/bin/env python3
from gettext import gettext as _
from dev_aberto import hello
# Initialize the gettext system
import gettext
gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

# cli é o nome do arquivo em que guardamos nossas traduções
# localedir é o caminho onde estão armazenadas as traduções. Pode ser um caminho relativo. 
if __name__ == '__main__':
    date, name = hello()
    print(_('Último commit feito em:'), date, _(' por'), name)
