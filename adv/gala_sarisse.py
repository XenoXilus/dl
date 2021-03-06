from core.advbase import *

def module():
    return Gala_Sarisse

class Gala_Sarisse(Adv):
    conf = {}
    conf['slots.a'] = [
    'Forest_Bonds',
    'Flash_of_Genius',
    'The_Red_Impulse',
    'From_Whence_He_Comes',
    'Dueling_Dancers'
    ]
    conf['slots.burn.a'] = [
    'Forest_Bonds',
    'Flash_of_Genius',
    'Me_and_My_Bestie',
    'From_Whence_He_Comes',
    'Dueling_Dancers'
    ]
    conf['slots.d'] = 'Gala_Mars'
    conf['acl'] = """
        `dragon, s=1 and not s4.check()
        `s3, not buff(s3)
        `s2
        `s1
        `s4
        `fs, x=5
        `dodge, fscf
        """
    conf['coabs'] = ['Yuya', 'Marth', 'Halloween_Mym']
    conf['share'] = ['Gala_Mym']

    def prerun(self):
        self.ahits = 0
        self.s2stance = 0

    def add_combo(self, name='#'):
        super().add_combo(name)
        if self.condition('always connect hits'):
            if self.hits // 20 > self.ahits:
                self.ahits = self.hits // 20
                Selfbuff('a1_att',0.02,15,'att','buff', source=name).on()
                Selfbuff('a1_crit',0.01,15,'crit','chance', source=name).on()

    # def s1_proc(self, e):
    #     buffcount = min(self.buffcount, 7)
    #     self.dmg_make(e.name,0.95*buffcount)
    #     self.add_hits(buffcount)

    # def s2_proc(self, e):
    #     if self.s2stance == 0:
    #         Teambuff(f'{e.name}_str',0.20,10).on()
    #         self.s2stance = 1
    #     elif self.s2stance == 1:
    #         Teambuff(f'{e.name}_def',0.20,15,'defense').on()
    #         self.s2stance = 0


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
