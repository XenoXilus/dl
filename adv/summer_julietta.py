from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Summer_Julietta

class Summer_Julietta(Adv):
    conf = {}
    conf['slots.a'] = Summer_Paladyns()+Primal_Crisis()
    conf['slots.frostbite.a'] = Summer_Paladyns()+His_Clever_Brother()
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon(c3-s-end)
        `s3
        `s4
        `s1
        `s2, cancel
        `fs, cancel and s1.charged>=s1.sp-self.sp_val('fs')
    """
    conf['coabs'] = ['Blade', 'Hunter_Sarisse', 'Summer_Estelle']
    conf['coabs.frostbite'] = ['Blade', 'Xander', 'Summer_Estelle']
    conf['afflict_res.bog'] = 100
    conf['share'] = ['Gala_Elisanne', 'Ranzal']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
