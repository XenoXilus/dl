import adv_test
import adv

def module():
    return Luca

class Luca(adv.Adv):
    def init(this):
        this.dmg_make("o_s1_paralysis",2.65)
        this.dmg_make("o_s1_paralysis",2.65)
        this.dmg_make("o_s1_paralysis",2.65)


    def pre(this):
        if this.condition('hp100'):
            this.conf['mod_a'] = ('att' , 'passive' , 0.13) 
        if this.condition('c4+fs'):
            this.conf['acl'] = """
                `s1, fsc
                `s2, fsc
                `s3, fsc
                `fs, seq=4
                """



if __name__ == '__main__':
    module().comment = 'paralysis 3 times'
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5 
        """
    adv_test.test(module(), conf, verbose=0)
