from core.advbase import *

def module():
    return Melsa

class Melsa(Adv):
    conf = {}
    conf['slots.a'] = ['Twinfold_Bonds', 'Levins_Champion']
    conf['acl'] = """
        `dragon,s
        `s3, not buff(s3) and x=5
        `s4
        `s1, cancel
        `s2,s=1
        `fs, x=5
    """
    conf['coabs'] = ['Blade', 'Wand', 'Marth']
    conf['share'] = ['Kleimann']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
