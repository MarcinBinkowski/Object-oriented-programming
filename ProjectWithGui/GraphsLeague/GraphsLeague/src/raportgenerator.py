#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fpdf import FPDF

class PDFGenerator:
    def generate_raport(self, name, rank_solo, rank_flex, server, lvl, chest_champs):
        """
        This functions is like template: takes arguments and generate pdfs from the data, should be written more simply
        """
        pdf = FPDF()
        pdf.set_author("Marcin Binkowski")
        pdf.add_page()
        pdf.set_font("arial", size=50)
        pdf.cell(0, 20, txt="GraphsLeague",  ln=2, align="C")
        pdf.set_font("arial", size=30)
        pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/icon.png", w=30)
        pdf.cell(0, 15, txt="{}".format(name), ln=2, align="L")
        pdf.set_font("arial","B", size=16,)
        pdf.cell(200, 8, txt="server: {}".format(server), ln=1, align="L")
        pdf.cell(200, 8, txt="level: {}".format(lvl), ln=1, align="L")
        pdf.cell(200, 30, ln=1, align="L")
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/static/icons/base-icons/{}.png".format(rank_solo), w=50, x=60, y=70)
        except:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/static/icons/base-icons/provisional.png".format(rank_solo), w=50, x=60, y=70)
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/static/icons/base-icons/{}.png".format(rank_flex), w=50, x=125, y=70)
        except:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/static/icons/base-icons/provisional.png".format(rank_solo),w=50, x=125, y=70)

        pdf.set_font("arial", size=24)
        pdf.cell(90,8, txt="Ranked", ln=0, align="R")
        pdf.cell(100, 8, txt="Flex", ln=1, align="C")
        pdf.cell(200, 8, ln=1, align="C")
        pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/{}_mastery_distribution.png".format(name), w=90, x=0)
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/top_champ2.png", w=25, x=100, y=160)
        except:
            pass
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/top_champ1.png", w=30, x=127, y=155)
        except:
            pass
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/top_champ3.png", w=20, x=159, y=165)
        except:
            pass
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/{}_solo_duo.png".format(name), w=110, x=2, y=195)
        except:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/blank_graph.png".format(name), w=110, x=2, y=195)
        try:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/{}_flex.png".format(name), w=110, x=98, y=195)
        except:
            pdf.image("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/src/temporary/blank_graph.png".format(name), w=110, x=98, y=195)
        pdf.cell(200, 60, ln=1)
        pdf.set_font("Courier", size=12)
        pdf.cell(200, 8, txt="You can still get chests for playing: {}, {} and {}".format(
                chest_champs[0], chest_champs[1], chest_champs[2]), ln=1, align="L")
        pdf.output("C:/Users/marci/OneDrive/Pulpit/dev/Object-oriented-programming/ProjectWithGui/GraphsLeague/GraphsLeague/raports/{}_raport.pdf".format(name))


