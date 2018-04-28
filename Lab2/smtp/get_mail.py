import poplib
import sys

print("#########################", file = sys.stderr)
print("#########################", file = sys.stdout)
M = poplib.POP3('mail.intranet', 995)
M.user('bob@mail.intranet')
M.pass_('12345')
sys.stderr.write(M.list())
